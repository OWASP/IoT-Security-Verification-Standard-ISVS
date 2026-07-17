# isvs-appendix-b-updater

Audits `en/Appendix_B-Compliance_Mapping.md` (the ISVS-to-framework
compliance mapping for CRA, RED/EN 18031, NIST SP 800-213A, and ETSI EN 303
645) against the canonical ISVS requirement list, and cross-checks the
appendix's two internal tables (Table 1: ISVS → Frameworks, Table 2:
Frameworks → ISVS) for numbering and reciprocity errors.

This skill works **with any AI assistant, or with none at all** — see
[Model-agnostic use](#model-agnostic-use) below.

## What it checks

1. **Numbering & completeness** — every canonical ISVS requirement ID should
   appear exactly once in Table 1, in order, with no drift between an
   appendix row's summary and the canonical requirement text it claims to
   represent.
2. **Structural mapping** — every ISVS ↔ framework-clause pairing in Table 1
   must appear in Table 2 and vice versa, including matching Partial
   qualifiers.
3. **Missing mappings** — requirements with no mapping in some framework
   column are checked against that framework's clause list for plausible
   matches before accepting `—` (no alignment) as correct.

Anything the scripts can decide mechanically (numbering gaps, missing/unknown
IDs, reciprocity mismatches, invalid clause IDs) is reported with zero
judgment involved. Deciding whether an ISVS requirement's alignment to a
specific framework clause is Direct, Partial, or `—` is a semantic judgment
call that requires reading the actual framework clause text — see
`references/mapping_heuristics.md`.

## Model-agnostic use

`SKILL.md` in this directory is written as Claude Code's entry point — it's
what Claude Code loads when you invoke `/isvs-appendix-b-updater`. That
invocation mechanism only works in Claude Code. Everything it tells Claude
Code to do, you (or any other AI assistant) can do directly:

### 1. Run the mechanical checks

From this directory:

```bash
python3 scripts/fetch_isvs_requirements.py --local-dir ../../../en --out /tmp/isvs_requirements.json
python3 scripts/parse_appendix.py ../../../en/Appendix_B-Compliance_Mapping.md --out /tmp/appendix_parsed.json
python3 scripts/consistency_check.py /tmp/isvs_requirements.json /tmp/appendix_parsed.json --out /tmp/consistency_report.json
python3 scripts/cross_check_tables.py /tmp/appendix_parsed.json --registry references/framework_clauses.json --out /tmp/crosscheck_report.json
```

Use `--ref <tag-or-branch>` instead of `--local-dir` on
`fetch_isvs_requirements.py` to pull requirement chapters straight from
GitHub rather than a local checkout. Read the JSON reports with any tool —
`jq`, Python, or by eye.

### 2. Do the semantic review

For each requirement × framework pairing flagged by step 1 (or, for a full
audit, every pairing):

1. Read `references/mapping_heuristics.md` for the Direct/Partial/`—`
   decision criteria, and the framework-specific pitfalls (e.g. which CRA
   Annex I letter means what).
2. Look up the framework's source URL in `references/framework_clauses.json`
   and read the actual clause text — don't rely on a paraphrase from memory.
3. Compare it against the **canonical** ISVS requirement text (not the
   appendix's shortened summary) and decide Direct, Partial, or `—`.

This step is genuinely a judgment call and benefits from a second reader —
but it doesn't require any particular AI tool. A human contributor with the
framework texts open in two tabs can do exactly this.

### 3. Write up the change

Follow `references/output_format.md`: annotate every changed table row with
an inline `<!-- [CHG-nnn] <type>: <description> -->` comment, and add a
"Change Log & Decision Record" section below the tables listing, per change,
the before/after, rationale, sources (with URLs and access dates), and a
confidence level. This keeps the result reviewable by anyone, regardless of
who or what produced it.

### 4. Verify

Re-run the four scripts from step 1 against your edited file and confirm
zero in-scope missing IDs, zero unknown IDs, zero reciprocity errors, and
zero invalid clause IDs (except any pre-existing issues you deliberately
left for a follow-up — document those explicitly rather than silently
leaving them unmentioned).

## Files

- `SKILL.md` — Claude Code's entry point; a step-by-step playbook (same
  content as this README's workflow, phrased as direct instructions to an
  agent).
- `scripts/fetch_isvs_requirements.py` — extracts canonical requirement IDs,
  text, and levels from the V1–V5 chapter files.
- `scripts/parse_appendix.py` — parses the appendix's two tables into
  structured JSON.
- `scripts/consistency_check.py` — numbering/completeness diff between the
  canonical list and the parsed appendix.
- `scripts/cross_check_tables.py` — Table 1 ↔ Table 2 reciprocity and
  clause-ID validity check.
- `references/mapping_heuristics.md` — Direct/Partial/`—` decision criteria
  and per-framework pitfalls.
- `references/framework_clauses.json` — registry of valid clause/provision
  IDs per framework, with source URLs.
- `references/output_format.md` — exact format for the annotated output
  file and its Change Log & Decision Record.
