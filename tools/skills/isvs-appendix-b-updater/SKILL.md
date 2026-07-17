---
name: isvs-appendix-b-updater
description: >
  Audit and update Appendix B (Compliance Mapping) of the OWASP IoT Security
  Verification Standard (ISVS). Use this skill whenever the user asks to check,
  fix, regenerate, or update the ISVS compliance mapping, verify that Appendix B
  matches the ISVS requirement numbering, validate or complete mappings to the
  EU Cyber Resilience Act (CRA), the Radio Equipment Directive (RED / EN 18031),
  NIST SP 800-213A, or ETSI EN 303 645 — even if they only say "update the ISVS
  appendix", "check the compliance table", or mention an OWASP IoT mapping table.
  Produces an annotated, human-reviewable markdown file with a full decision log.
---

# ISVS Appendix B Updater

Audits OWASP ISVS Appendix B (Compliance Mapping) against (1) the canonical ISVS
requirement list and (2) the mapped frameworks, then produces an updated,
annotated markdown file in which **every change is traceable to evidence**.

The deliverable is a single markdown file containing:
1. The corrected Appendix B (both tables), with an inline HTML comment
   `<!-- [CHG-nnn] ... -->` on every changed row.
2. A **Change Log & Decision Record** section below the tables documenting, for
   each change: what changed, why, which sources were consulted (with URLs and
   clause references), and whether human review is recommended.

## Core principles

- **Deterministic before judgment.** Scripts handle everything mechanical
  (parsing, ID comparison, cross-table reciprocity, clause-format validation).
  You only apply judgment to *semantic* questions: "does ISVS req X really
  align with CRA 2(e)?" — and every judgment must cite a source.
- **Never invent a mapping.** A new mapping is only added when you can point to
  specific clause text in the framework source that aligns with the ISVS
  requirement text. If you cannot fetch or verify the clause, do not add the
  mapping — record it in the decision log as "candidate, unverified, human
  review required" instead.
- **Everything traceable.** Every change gets a CHG-ID, appears both inline
  (comment) and in the decision log, and lists its evidence. A reviewer must be
  able to reject any single change independently.
- **Missing-mapping symbol.** Every cell with no meaningful alignment carries an
  explicit dash — never leave a cell blank. Follow the appendix's existing
  convention (the published appendix uses `—`); if the user asks for a plain
  ASCII `-`, apply it consistently across both tables and note the convention
  once in the decision log header, not as per-row changes.
- **Token economy.** Do the mechanical work in the scripts, not in context:
  never paste whole reports or the full appendix into your reasoning — query
  the JSON with short python one-liners for exactly the fields you need, and
  fetch each framework source at most once per run.
- **The scope note is law.** Appendix B may deliberately exclude requirements
  (e.g. "requirements added after v1.0 will be mapped in a future update").
  Requirements excluded by an explicit scope note are reported as
  `out_of_scope`, not as missing rows — unless the user asks to expand scope.
  Confirm with the user before mapping out-of-scope requirements.

## Workflow

Work in a scratch directory (e.g. `/home/claude/isvs-work/`). Run all scripts
from the skill's `scripts/` directory.

### Step 0 — Obtain inputs

1. **The appendix under audit.** If the user uploaded a markdown file, use it.
   Otherwise fetch the published page
   (`https://owasp.org/IoT-Security-Verification-Standard-ISVS/en/Appendix_B-Compliance_Mapping.html`)
   with your web-fetch tool and save the markdown content to
   `appendix_b.md`. Preserve the tables exactly as published — the parser is
   tolerant of both raw markdown and HTML-to-markdown conversions.
2. **Determine the ISVS reference version.** Read the appendix scope note: it
   states which ISVS release the mapping targets (e.g. "v1.0 release (master
   branch)"). Ask the user if ambiguous. This decides the `--ref` used below.

### Step 1 — Fetch canonical ISVS requirements

```bash
python3 scripts/fetch_isvs_requirements.py --ref master --out isvs_requirements.json
```

Pulls chapter markdown (V1–V5) from
`raw.githubusercontent.com/OWASP/IoT-Security-Verification-Standard-ISVS/<ref>/en/`
and extracts every requirement ID, its full text, and its L1/L2/L3 levels.
Use `--ref <tag>` for a pinned release. If the network blocks the fetch, ask
the user for the chapter files or fetch them with your web-fetch tool and use
`--local-dir <dir>` instead. The JSON records the exact source URL and a
SHA-256 of each fetched file — these go into the decision log.

### Step 2 — Parse the appendix

```bash
python3 scripts/parse_appendix.py appendix_b.md --out appendix_parsed.json
```

Extracts Table 1 (per-requirement rows with all framework columns), Table 2
(per-clause reverse mappings), and the scope-note exclusions it can detect.

### Step 3 — Numbering & completeness check (user goal 1)

```bash
python3 scripts/consistency_check.py isvs_requirements.json appendix_parsed.json --out consistency_report.json
```

Reports, with zero judgment required:
- `missing_in_appendix`: canonical IDs absent from Table 1 (split into
  `in_scope_missing` vs `out_of_scope` using the scope note).
- `unknown_in_appendix`: Table 1 IDs that do not exist in the publication
  (typo, renumbering drift, or removed requirement).
- `numbering_gaps` and `order_violations` inside Table 1.
- `text_drift`: rows whose summary no longer resembles the canonical
  requirement text (token-overlap heuristic) — these often reveal *shifted*
  numbering (row N carries the text of requirement N±1). Inspect every one.

When `unknown_in_appendix` and `missing_in_appendix` IDs are adjacent (e.g.
appendix has 3.3.4–3.3.6 but publication has 3.3.3–3.3.5), treat it as a
**renumbering** fix: keep the row content aligned to the matching canonical
text, correct the ID, and annotate. Do not blindly delete-and-add.

### Step 4 — Structural mapping check (part of user goal 2)

```bash
python3 scripts/cross_check_tables.py appendix_parsed.json --registry references/framework_clauses.json --out crosscheck_report.json
```

Reports:
- Invalid clause identifiers per framework (e.g. `CRA 2(n)` does not exist;
  ETSI sub-provision beyond the known range → flagged `verify_against_source`).
- **Table 1 ↔ Table 2 reciprocity**: every Table 1 cell must appear in the
  corresponding Table 2 clause list and vice versa, including matching
  Partial/(P) qualifiers. Asymmetries are mechanical errors — fix whichever
  side the evidence supports and log it.

### Step 5 — Semantic mapping verification (user goals 2 & 3)

This is the judgment step. Read `references/mapping_heuristics.md` first.

1. Build the review queue: rows flagged by steps 3–4, rows you corrected the
   numbering of, plus rows with suspiciously empty framework columns.
   For a full audit, review every row; for a targeted update, review the queue.
2. For each queued (ISVS req × framework) pair, fetch the framework source
   listed in `references/framework_clauses.json` (`sources` block) with your
   web-fetch tool. Compare the actual clause text with the canonical ISVS
   requirement text.
3. Decide: **direct**, **Partial**, or **—**, per the criteria in
   `mapping_heuristics.md`. Record a one-line justification plus the clause
   citation and URL for the decision log. Paraphrase clause text — do not
   quote at length.
4. Missing mappings (goal 3): for every requirement lacking a mapping in some
   framework column, check the framework's clause list for plausible matches
   before accepting `—` as correct. `—` is a valid, deliberate answer for
   ecosystem-/process-level clauses (see the appendix's own note 7); confirm,
   don't assume.
5. Apply every accepted change to both Table 1 and Table 2 — reciprocity must
   hold in the final output. Rerun `cross_check_tables.py` on the edited
   result to prove it.

### Step 6 — Produce the annotated output

Read `references/output_format.md` and follow it exactly. In short:

- Full corrected Appendix B document.
- Each changed table row carries `<!-- [CHG-nnn] <short description> -->`
  appended inside its first cell (HTML comments inside a cell keep GFM tables
  intact — never place a comment on its own line between table rows).
- Below the tables, a `## Change Log & Decision Record` section: one entry per
  CHG-ID with location, type, before → after, rationale, evidence (sources +
  clause refs + fetch dates + file hashes where applicable), confidence, and a
  `Human review:` flag.
- A `### Items requiring human decision` subsection for anything you could not
  verify (unreachable paywalled standards like the full ETSI/EN 18031 text,
  ambiguous scope questions, candidate mappings without confirmed clause text).
- A `### Verification runs` subsection listing the script commands executed and
  their headline results, so the audit is reproducible.

### Step 7 — Final self-check before delivering

```bash
python3 scripts/parse_appendix.py updated_appendix_b.md --out final_parsed.json
python3 scripts/consistency_check.py isvs_requirements.json final_parsed.json --out final_consistency.json
python3 scripts/cross_check_tables.py final_parsed.json --registry references/framework_clauses.json --out final_crosscheck.json
```

The final reports must show zero in-scope missing IDs, zero unknown IDs, zero
reciprocity errors, and zero invalid clause IDs (soft ETSI range flags are
acceptable if logged). Include this in "Verification runs". Then deliver
`updated_appendix_b.md` to the user.

## Failure & edge handling

- **Paywalled standards** (ETSI EN 303 645 PDF is free; EN 18031-x and some
  NIST detail may be hard to fetch): never guess. Use the freely available
  source where one exists; otherwise mark the mapping decision as unverified
  and route it to "Items requiring human decision".
- **Framework structure changed** (e.g. a CRA amendment): update
  `references/framework_clauses.json` locally for the run, cite the source of
  the new structure in the decision log.
- **Conflicting duplicates** (same ISVS ID twice in Table 1): keep the row
  matching canonical text, log the removal.
- **User provides a modified/internal fork of ISVS**: use their files via
  `--local-dir`; record file hashes instead of URLs as provenance.
