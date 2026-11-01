#!/usr/bin/env python3
"""
Design Framework — doctor

Checks the framework for the kind of rot that fails silently. Everything here
exists because it actually went wrong once and nothing said so for months.

    ./doctor.py             full report
    ./doctor.py --quiet     print only problems (used by the session-start hook)
    ./doctor.py --json      machine-readable
    ./doctor.py --repo-only skip machine-local checks (for CI and the cloud audit,
                            which have their own checkout and no ~/.claude)
    ./doctor.py --errors-only
                            suppress warnings; for a global session hook, where
                            only "your agents are broken right now" earns an
                            interruption during unrelated work

Exit codes: 0 clean · 1 warnings · 2 errors.

The guiding rule: prefer failing loud on something unrecognised over validating
against a list of known-good values. A list of known-good values is itself a
thing that goes stale, and a validator that silently accepts a key the harness
silently ignores is worse than no validator at all.
"""

import glob
import json
import os
import re
import subprocess
import sys
import time

ROOT = os.path.dirname(os.path.abspath(__file__))
HOME_CLAUDE = os.path.expanduser("~/.claude")

# Reference: https://code.claude.com/docs/en/sub-agents  (field table)
# /audit refreshes this. An unknown key is reported, never silently accepted —
# `allowed-tools` and `model: creative` sat here for four months doing nothing.
AGENT_KEYS = {
    "name", "description", "tools", "disallowedTools", "model", "permissionMode",
    "maxTurns", "autoCompactWindow", "skills", "mcpServers", "hooks", "memory",
    "background", "omitClaudeMd", "effort", "isolation", "color", "initialPrompt",
    "experimental",
}
MODEL_VALUES = {"sonnet", "opus", "haiku", "fable", "inherit"}
SKILL_KEYS = {"name", "description", "allowed-tools", "metadata", "disable-model-invocation", "license"}

# Reference: https://code.claude.com/docs/en/hooks  (lifecycle table)
# A misspelled event name never fires and is never reported — the same silent
# class as an unrecognised agent key. /audit refreshes this.
HOOK_EVENTS = {
    "SessionStart", "Setup", "UserPromptSubmit", "UserPromptExpansion", "PreToolUse",
    "PermissionRequest", "PermissionDenied", "PostToolUse", "PostToolUseFailure",
    "PostToolBatch", "Notification", "MessageDisplay", "SubagentStart", "SubagentStop",
    "TaskCreated", "TaskCompleted", "Stop", "StopFailure", "TeammateIdle",
    "InstructionsLoaded", "ConfigChange", "CwdChanged", "DirectoryAdded", "FileChanged",
    "WorktreeCreate", "WorktreeRemove", "PreCompact", "PostCompact", "PreModelSwitch",
    "PostModelSwitch", "Elicitation", "ElicitationResult", "SessionEnd",
}
HOOK_TYPES = {"command", "http", "mcp_tool", "prompt", "agent"}
# Events whose matcher filters a tool name. Elsewhere a matcher is either a
# different axis entirely or silently ignored.
TOOL_MATCHER_EVENTS = {
    "PreToolUse", "PostToolUse", "PostToolUseFailure", "PermissionRequest", "PermissionDenied",
}

STALE_GUARD_DAYS = 90   # a guarded path nobody writes to is a dead guard
STALE_AUDIT_DAYS = 60   # vendor drift outruns this
STALE_TASTE_DAYS = 180  # taste only compounds if something updates it

problems = []   # (level, area, message)


def err(area, msg):
    problems.append(("error", area, msg))


def warn(area, msg):
    problems.append(("warn", area, msg))


def frontmatter(path):
    """Return the raw frontmatter block, or None if the file has none."""
    text = open(path, encoding="utf-8").read()
    if not text.startswith("---\n"):
        return None
    end = text.find("\n---\n", 4)
    return None if end == -1 else text[4:end + 1]


def keys_of(fm):
    return dict(re.findall(r"^([A-Za-z][\w-]*):[ \t]*(.*)$", fm, re.M))


def age_days(path):
    return (time.time() - os.path.getmtime(path)) / 86400


def walk(*exts, skip=()):
    """Every file in the repo with one of these extensions.

    Deliberately not glob('**'): glob skips dotted directories, which silently
    hid the entire .claude tree — the agents, the skills, and settings.json —
    from three checks in this file's first version. The bug this tool exists to
    catch, committed by the tool itself.
    """
    for base, dirs, files in os.walk(ROOT):
        dirs[:] = [d for d in dirs if d not in (".git", "node_modules")]
        rel_base = os.path.relpath(base, ROOT)
        if any(rel_base == s or rel_base.startswith(s + os.sep) for s in skip):
            continue
        for f in files:
            if f.endswith(exts):
                yield os.path.join(base, f)


# ---------------------------------------------------------------- agents
def check_agents():
    files = sorted(glob.glob(f"{ROOT}/.claude/agents/*.md"))
    if not files:
        err("agents", "no agent definitions found")
        return 0
    for f in files:
        base = os.path.basename(f)
        fm = frontmatter(f)
        if fm is None:
            err("agents", f"{base}: no frontmatter — this file will not load as an agent")
            continue
        k = keys_of(fm)

        unknown = set(k) - AGENT_KEYS
        if unknown:
            err("agents", f"{base}: unrecognised key(s) {sorted(unknown)} — "
                          "Claude Code ignores these silently, so the setting does nothing")

        if "name" not in k or "description" not in k:
            err("agents", f"{base}: missing required name/description")
        elif k["name"] != base[:-3]:
            warn("agents", f"{base}: name '{k['name']}' does not match the filename")

        m = k.get("model", "")
        if m and m not in MODEL_VALUES and not m.startswith("claude-"):
            err("agents", f"{base}: model '{m}' is not a valid value — agent silently falls back to inherit")

        if "tools" in k and "\n" not in k["tools"] and "," not in k["tools"] and k["tools"].strip() == "":
            warn("agents", f"{base}: empty tools list — the agent would launch with zero tools")
    return len(files)


# ---------------------------------------------------------------- skills
def check_skills():
    files = sorted(glob.glob(f"{ROOT}/.claude/skills/**/SKILL.md", recursive=True))
    if not files:
        err("skills", "no skills found")
        return 0, []
    names = []
    for f in files:
        d = os.path.basename(os.path.dirname(f))
        fm = frontmatter(f)
        if fm is None:
            err("skills", f"{d}: no frontmatter — this skill will not load")
            continue
        k = keys_of(fm)
        unknown = set(k) - SKILL_KEYS
        if unknown:
            warn("skills", f"{d}: unrecognised key(s) {sorted(unknown)}")
        name = k.get("name", "").strip()
        if not name:
            err("skills", f"{d}: missing name")
        elif name != d:
            err("skills", f"{d}: name '{name}' does not match its directory — "
                          "skills resolve by directory, so this will not be found")
        else:
            names.append(name)
        if not k.get("description", "").strip():
            warn("skills", f"{d}: missing description — nothing will know when to invoke it")
    return len(files), names


# ---------------------------------------------------------------- install
def check_install(agent_count, skill_names):
    linked_a = linked_s = broken = 0
    for d, expect in ((f"{HOME_CLAUDE}/agents", "agent"), (f"{HOME_CLAUDE}/skills", "skill")):
        for entry in glob.glob(f"{d}/*"):
            if not os.path.islink(entry):
                continue
            target = os.readlink(entry)
            if not target.startswith(ROOT):
                continue
            if not os.path.exists(entry):
                err("install", f"dead symlink: {entry} -> {target}")
                broken += 1
            elif expect == "agent":
                linked_a += 1
            else:
                linked_s += 1

    if linked_a == 0 and linked_s == 0:
        warn("install", "framework is not installed to ~/.claude — its agents and skills "
                        "only load when Claude Code runs from this directory. Run ./install.sh")
    else:
        if linked_a < agent_count:
            warn("install", f"{linked_a} of {agent_count} agents linked — run ./install.sh to refresh")
        if linked_s < len(skill_names):
            warn("install", f"{linked_s} of {len(skill_names)} skills linked — run ./install.sh to refresh")
    return linked_a, linked_s, broken


# ---------------------------------------------------------------- syntax
def check_syntax():
    for f in walk(".json"):
        try:
            json.load(open(f, encoding="utf-8"))
        except Exception as e:
            err("syntax", f"{os.path.relpath(f, ROOT)}: invalid JSON — {e}")
    for f in walk(".sh"):
        if subprocess.run(["bash", "-n", f], capture_output=True).returncode:
            err("syntax", f"{os.path.relpath(f, ROOT)}: shell syntax error")


# ---------------------------------------------------------------- hooks
def check_hooks():
    """Validate settings.json hooks against the current Claude Code reference.

    A hook is the framework's only real enforcement mechanism, and every way it
    can be wrong is silent: an unknown event name never fires, an unknown
    handler type never runs, and a tool matcher that doesn't match any live tool
    name enforces nothing while looking entirely correct. The 2026-11 audit
    found exactly that — a matcher pinned to `mcp__figma` that cannot match a
    server registered as `Figma`.
    """
    p = f"{ROOT}/.claude/settings.json"
    if not os.path.exists(p):
        return
    try:
        cfg = json.load(open(p, encoding="utf-8"))
    except Exception:
        return  # check_syntax already reported it

    for event, groups in (cfg.get("hooks") or {}).items():
        if event not in HOOK_EVENTS:
            err("hooks", f"settings.json: '{event}' is not a Claude Code hook event — "
                         "it will never fire, and nothing reports that")
            continue
        if not isinstance(groups, list):
            err("hooks", f"settings.json: {event} must be a list of matcher groups")
            continue
        for group in groups:
            if not isinstance(group, dict):
                continue
            matcher = group.get("matcher", "")

            if matcher and event not in TOOL_MATCHER_EVENTS and event != "SessionStart":
                warn("hooks", f"settings.json: {event} matcher '{matcher}' — confirm this "
                              "event filters on the axis you think it does; an unsupported "
                              "matcher is silently ignored")

            # A tool matcher naming an MCP server pins that server's exact
            # spelling. The same server is registered as both `figma` and
            # `Figma` depending on how it was added, and the matcher is a
            # case-sensitive regex, so one spelling silently enforces nothing.
            if event in TOOL_MATCHER_EVENTS and "mcp__" in matcher:
                for server in re.findall(r"mcp__([A-Za-z0-9_]+)", matcher):
                    if "[" not in matcher:
                        warn("hooks", f"settings.json: {event} matcher pins MCP server "
                                      f"'{server}' in one casing. Matchers are "
                                      "case-sensitive regexes and the same server is "
                                      "registered as both 'figma' and 'Figma' — use a "
                                      "character class like mcp__[Ff]igma")
                        break

            for h in group.get("hooks") or []:
                if not isinstance(h, dict):
                    continue
                t = h.get("type")
                if t not in HOOK_TYPES:
                    err("hooks", f"settings.json: {event} has a hook of type '{t}', which "
                                 f"Claude Code does not recognise — valid: {sorted(HOOK_TYPES)}")
                    continue
                if t == "command" and not h.get("command"):
                    err("hooks", f"settings.json: {event} command hook has no command")
                # Prompt hooks default to a 30s timeout; one that must read a
                # file and verify against it can exceed that and be cancelled.
                if t == "prompt" and "timeout" not in h and len(h.get("prompt", "")) > 400:
                    warn("hooks", f"settings.json: {event} prompt hook is long but sets no "
                                  "timeout — the default is 30s, after which it is cancelled")


# ---------------------------------------------------------------- references
def check_references():
    pattern = re.compile(r"`((?:templates|hooks|docs|projects|audit)/[\w./ -]+|\.claude/(?:skills|agents)/[\w./-]+)`")
    seen = set()
    for f in walk(".md", ".json"):
        rel_file = os.path.relpath(f, ROOT)
        for ref in pattern.findall(open(f, encoding="utf-8").read()):
            ref = ref.rstrip(". ")
            if ref.endswith("/") or "<" in ref or "*" in ref:
                continue
            if not os.path.exists(os.path.join(ROOT, ref)) and (ref, rel_file) not in seen:
                seen.add((ref, rel_file))
                warn("references", f"{rel_file} points at `{ref}`, which does not exist")


# ---------------------------------------------------------------- projects
def check_projects(repo_only=False):
    """Validate project configuration.

    Some of this is about the repo and some is about the machine. A project's
    `canonicalDocs` and `hostProjectPath` point at directories on the
    designer's own computer, so a cloud or CI checkout cannot judge them: every
    one reads as missing, which is exactly the noise `--repo-only` exists to
    suppress. The structural checks below still run everywhere; only the
    does-this-path-exist ones are skipped.
    """
    cfgs = sorted(glob.glob(f"{ROOT}/projects/*/project.json"))
    dirs = [d for d in sorted(glob.glob(f"{ROOT}/projects/*/")) if os.path.isdir(d)]
    for d in dirs:
        if not os.path.exists(os.path.join(d, "project.json")):
            warn("projects", f"{os.path.basename(d.rstrip('/'))}: no project.json — "
                             "the framework cannot tell what this project is")

    for cfg in cfgs:
        name = os.path.basename(os.path.dirname(cfg))
        try:
            d = json.load(open(cfg))
        except Exception:
            continue
        for label, p in (d.get("canonicalDocs") or {}).items():
            if label.startswith("_") or not isinstance(p, str):
                continue
            if repo_only:
                continue  # host path — not judgeable from a checkout
            if not os.path.exists(os.path.expanduser(p)):
                warn("projects", f"{name}: canonicalDocs.{label} points at {p}, which does not exist")

    for cfg in sorted(glob.glob(f"{ROOT}/projects/*/prototype.json")):
        name = os.path.basename(os.path.dirname(cfg))
        try:
            d = json.load(open(cfg))
        except Exception:
            continue
        host = os.path.expanduser(d.get("hostProjectPath", ""))
        if not host:
            warn("projects", f"{name}: prototype.json has no hostProjectPath")
            continue
        if repo_only:
            continue  # host path — not judgeable from a checkout
        if not os.path.isdir(host):
            err("projects", f"{name}: hostProjectPath {d['hostProjectPath']} does not exist — "
                            "the drift check can never fire and /prototype cannot run")
            continue
        if d.get("mode") == "prototype-first":
            continue
        # A guard nobody writes to is a guard that is not guarding anything.
        for pat in d.get("verbatimPaths", []):
            hits = glob.glob(os.path.join(host, pat))
            if not hits:
                warn("projects", f"{name}: verbatimPaths '{pat}' matches no files — dead guard")
                continue
            newest = min(age_days(h) for h in hits)
            if newest > STALE_GUARD_DAYS:
                warn("projects", f"{name}: nothing under '{pat}' has changed in {int(newest)} days. "
                                 "If the work moved, the guard is decorative — repoint verbatimPaths "
                                 "or set mode to prototype-first")


# ---------------------------------------------------------------- currency
def check_currency():
    a = f"{ROOT}/audit/latest-audit.md"
    if not os.path.exists(a):
        warn("currency", "no audit on record — run /audit")
    elif age_days(a) > STALE_AUDIT_DAYS:
        warn("currency", f"last framework audit was {int(age_days(a))} days ago — "
                         "vendor tooling moves faster than that. Run /audit")

    t = f"{ROOT}/taste-profile.md"
    if os.path.exists(t) and age_days(t) > STALE_TASTE_DAYS:
        warn("currency", f"cross-project taste memory unchanged in {int(age_days(t))} days. "
                         "It only compounds if /retro updates it")

    # Every hardcoded vendor tool name is a maintenance liability. Not an error —
    # sometimes one is genuinely needed — but the count should stay near zero.
    names = set()
    for f in walk(".md", ".json", skip=("projects", "audit")):
        names |= set(re.findall(r"mcp__[a-zA-Z0-9_]+", open(f, encoding="utf-8").read()))
    if len(names) > 12:
        warn("currency", f"{len(names)} distinct vendor tool names hardcoded in the framework layer. "
                         "Each one goes stale on its own schedule — prefer describing intent")
    return sorted(names)


# ---------------------------------------------------------------- README
def check_readme(agent_count, skill_count):
    p = f"{ROOT}/README.md"
    if not os.path.exists(p):
        return
    text = open(p, encoding="utf-8").read()
    wf = len([d for d in glob.glob(f"{ROOT}/.claude/skills/workflows/*/") if os.path.isdir(d)])
    for claimed, actual, label in (
        (re.search(r"(\d+)\s+specialist agents", text), agent_count, "specialist agents"),
        (re.search(r"(\d+)\s+workflow skills", text), wf, "workflow skills"),
    ):
        if claimed and int(claimed.group(1)) != actual:
            warn("readme", f"README says {claimed.group(1)} {label}, repo has {actual}")


# ---------------------------------------------------------------- main
def main():
    quiet = "--quiet" in sys.argv
    as_json = "--json" in sys.argv
    repo_only = "--repo-only" in sys.argv
    errors_only = "--errors-only" in sys.argv

    n_agents = check_agents()
    n_skills, skill_names = check_skills()
    # The install check is about this machine, not this repo. A cloud or CI
    # checkout has no ~/.claude and would fail it on every single run, which is
    # the fastest way to teach someone to ignore the output.
    la, ls, broken = (0, 0, 0) if repo_only else check_install(n_agents, skill_names)
    check_syntax()
    check_hooks()
    check_references()
    check_projects(repo_only)
    tool_names = check_currency()
    check_readme(n_agents, n_skills)

    if errors_only:
        problems[:] = [p for p in problems if p[0] == "error"]
    errors = [p for p in problems if p[0] == "error"]
    warns = [p for p in problems if p[0] == "warn"]
    code = 2 if errors else (1 if warns else 0)

    if as_json:
        print(json.dumps({
            "agents": n_agents, "skills": n_skills,
            "linked": {"agents": la, "skills": ls, "broken": broken},
            "hardcodedToolNames": tool_names,
            "problems": [{"level": l, "area": a, "message": m} for l, a, m in problems],
        }, indent=2))
        return code

    if quiet:
        if problems:
            print(f"\n  design-framework doctor: {len(errors)} error(s), {len(warns)} warning(s)")
            for level, area, msg in problems[:6]:
                print(f"    {'!' if level == 'error' else '·'} [{area}] {msg}")
            if len(problems) > 6:
                print(f"    … {len(problems) - 6} more — run ./doctor.py")
            print()
        return code

    print(f"\nDesign Framework — doctor\n{'=' * 25}\n")
    linked = "install not checked (--repo-only)" if repo_only else f"{la}+{ls} linked into ~/.claude"
    print(f"  {n_agents} agents · {n_skills} skills · {linked}")
    print(f"  {len(tool_names)} vendor tool names hardcoded in the framework layer\n")

    if not problems:
        print("  No problems found.\n")
        return 0

    for level in ("error", "warn"):
        rows = [p for p in problems if p[0] == level]
        if not rows:
            continue
        print(f"  {'ERRORS' if level == 'error' else 'WARNINGS'}")
        for _, area, msg in rows:
            print(f"    [{area}] {msg}")
        print()
    return code


if __name__ == "__main__":
    sys.exit(main())
