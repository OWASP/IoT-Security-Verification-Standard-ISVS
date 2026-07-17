# Skills

## Overview

This directory holds "skills" used to maintain and audit parts of the ISVS —
self-contained bundles of instructions, reference material, and plain Python
scripts for a specific maintenance task.

Each skill is written so it can be used **with or without an AI assistant**.
The scripts do the mechanical work (parsing, comparison, validation) and
require nothing but `python3` from the standard library. The `SKILL.md` file
in each skill is a step-by-step playbook that a human contributor can follow
directly, or that an AI coding assistant can follow on a contributor's
behalf.

This directory is mirrored at `.claude/skills/` in a format
([Claude Code Skills](https://docs.claude.com/en/docs/claude-code/skills))
that lets Claude Code auto-discover and invoke a skill by name (e.g.
`/isvs-appendix-b-updater`). That auto-discovery mechanism is specific to
Claude Code — other AI tools (ChatGPT, Gemini CLI, Cursor, etc.) don't
recognize it. Contributors using a different tool, or no AI assistant at
all, should instead open the skill's own `README.md` (not `SKILL.md`, which
targets Claude Code's project search directly) for tool-agnostic
instructions.

If you edit a skill, update both copies (`tools/skills/...` and
`.claude/skills/...`) so they stay identical — everyone should be working
from the same playbook regardless of what tool they use.

## Available skills

- [`isvs-appendix-b-updater/`](isvs-appendix-b-updater/README.md) — audits
  `en/Appendix_B-Compliance_Mapping.md` against the canonical ISVS
  requirement list and cross-checks its two internal tables for numbering
  and reciprocity errors.
