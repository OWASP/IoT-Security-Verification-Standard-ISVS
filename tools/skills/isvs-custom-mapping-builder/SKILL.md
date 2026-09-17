---
name: isvs-custom-mapping-builder
description: >
  Build a product-context-specific mapping from OWASP ISVS requirements to
  other standards (EU CRA, RED/EN 18031, NIST SP 800-213A, ETSI EN 303 645).
  Use this skill whenever the user asks for a custom ISVS mapping, a
  business or product specific requirements view, to tailor Appendix B to a
  device type, or to scope ISVS to a deployment context — even if they only
  say "map ISVS to our product", "which ISVS requirements apply to us", or
  mention a custom compliance mapping. Filters the generalized Appendix B
  mapping by product context and produces a human-reviewable tailored file
  with versions, sources, and uncertain items preserved.
---

# ISVS Custom Mapping Builder

Builds a **product-context-specific** view of ISVS requirements and their
alignment to other standards, starting from the generalized Appendix B
mapping.

The generalized Appendix B mapping is useful but not equally applicable to
every business or product context. This skill takes a short product context
(device type, connectivity, data sensitivity, deployment, target regulations)
and produces a tailored mapping that says, per ISVS requirement: in scope,
out of scope, or needs human review — with the Appendix B framework
alignments carried over verbatim, plus versions, sources, and confidence.

The deliverable is a pair of files:
1. A tailored mapping markdown file with a version header, an applicability
   table, and a decision log.
2. A machine-readable JSON file with the same content for downstream tooling.

## Core principles

- **Filter, do not invent.** Framework alignments come verbatim from
  Appendix B Table 1. This skill never creates new ISVS-to-framework
  equivalence. Anything not verifiable in Appendix B or the cited sources is
  recorded as `TBD` with a reason and a reviewer prompt.
- **Versions and sources survive.** Every output records the ISVS ref
  (branch/tag/commit), the framework versions covered by Appendix B, and the
  source URLs. Uncertain mappings stay uncertain.
- **Informative only.** The output is a scoping aid, not legal or conformity
  advice. It must never claim compliance, certification, or satisfaction of a
  regulation. Appendix B's own disclaimer applies to every tailored file.
- **Nothing silently dropped.** Every canonical ISVS requirement appears in
  the output with an applicability verdict. Out-of-scope items are listed
  with a reason, not deleted.
- **Deterministic before judgment.** Scripts handle parsing, ID coverage,
  and rule-based applicability. Human or assistant judgment is limited to
  reviewing `TBD` and `review` items against actual product and clause text.
- **Token economy.** Do the mechanical work in the scripts. Never paste whole
  chapters or the full appendix into reasoning — query the JSON outputs with
  short python one-liners for exactly the fields needed.

## Workflow

Work in a scratch directory (e.g. `/tmp/isvs-custom/`). Run all scripts from
the skill's `scripts/` directory. See `README.md` for the same workflow
phrased for tool-agnostic use.

### Step 0 — Obtain inputs

1. **Product context file.** Ask the user for a context JSON, or create one
   from their description using the schema in
   `references/context_profiles.md`. Minimal fields: product name, device
   type, connectivity, whether it handles personal data, whether it is
   payment capable, target markets or regulations, update mechanism, and free
   text notes. Save as `context.json`. If any field is unknown, set it to
   `null` rather than guessing — unknown fields produce `review` verdicts,
   not assumptions.
2. **Canonical ISVS requirements.** Either reuse
   `isvs_requirements.json` from the `isvs-appendix-b-updater` skill, or
   parse the local checkout directly (the build script supports
   `--local-dir ../../../en`).
3. **Appendix B base mapping.** Either reuse `appendix_parsed.json` from the
   `isvs-appendix-b-updater` skill, or parse
   `../../../en/Appendix_B-Compliance_Mapping.md` directly.

### Step 1 — Build the tailored mapping

```bash
python3 scripts/build_custom_mapping.py \
  --local-dir ../../../en \
  --context /tmp/isvs-custom/context.json \
  --out-json /tmp/isvs-custom/custom_mapping.json \
  --out-md /tmp/isvs-custom/custom_mapping.md
```

This parses canonical requirements and Appendix B Table 1, applies the
context rules in `references/mapping_policy.md`, and writes both outputs.
Framework cells are copied verbatim from Appendix B. Applicability is one of
`in_scope`, `out_of_scope`, or `review`, each with a one-line reason. Items
that cannot be decided from context alone become `review` with a reviewer
prompt — never a silent guess.

To pin versions instead of using a local checkout, add
`--isvs-ref <tag-or-branch>` and `--appendix-ref <tag-or-branch>`; the
chosen refs are recorded in the output header.

### Step 2 — Validate the output

```bash
python3 scripts/validate_custom_mapping.py \
  /tmp/isvs-custom/custom_mapping.json \
  --out /tmp/isvs-custom/validation_report.json
```

Checks: every canonical requirement present exactly once, versions and
sources present, verdicts in the allowed set, no blank framework cells, no
banned compliance-claim language, every `TBD` or `review` item carries a
reason and reviewer prompt. Fix the context file or the inputs — never
hand-edit the generated JSON to silence the validator — and rerun Step 1.

### Step 3 — Semantic review of uncertain items

Read `references/mapping_policy.md`, then work through the `review` queue in
the generated markdown:

1. Open the canonical ISVS requirement text (not the appendix summary) and
   the cited framework clause text from its source URL.
2. Decide whether the applicability verdict should change. Framework
   alignments themselves must not be changed — if an alignment looks wrong,
   file it as a correction against Appendix B instead of editing the
   tailored copy.
3. Record the decision in the file's Decision Log section with sources,
   access date, and confidence (High/Medium/Low). Low-confidence items stay
   flagged for a second reviewer.

See `references/context_profiles.md` for three worked archetypes
(consumer camera, industrial gateway, BLE wearable) showing how the same
ISVS requirement can be in scope in one context and out of scope in another
without changing its framework alignments.

### Step 4 — Write up per output format

Follow `references/output_format.md`: version header, applicability table,
preserved framework columns, context notes, decision log, human-review
queue, and verification runs. Keep Appendix B's informative-status
disclaimer verbatim in every tailored file.

### Step 5 — Verify before submitting

Re-run the validator against the final JSON and confirm zero errors. Include
the validation report headline in the PR description along with the ISVS ref,
the Appendix B source, and the context file used.
