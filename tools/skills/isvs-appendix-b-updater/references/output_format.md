# Output format: annotated Appendix B

The deliverable is ONE markdown file (`updated_appendix_b.md`) with three
layers: (1) the corrected appendix, (2) inline change annotations, (3) a
decision record. A reviewer must be able to accept/reject each change
independently without consulting anything outside this file.

## 1. Inline annotations

Every changed table row gets an HTML comment **inside its first cell**,
appended after the cell content. HTML comments inside a cell are invisible
when rendered but visible in source — and they keep GFM tables intact.
NEVER place a comment on its own line between table rows (it breaks the
table in most renderers).

Comment format: `<!-- [CHG-nnn] <type>: <one-line description> -->`

Types: `RENUMBER`, `ADD-ROW`, `REMOVE-ROW`, `ADD-MAPPING`, `REMOVE-MAPPING`,
`QUALIFIER` (Partial <-> direct), `WORDING`, `RECIPROCITY` (Table 2 sync).

Examples:

```markdown
| **3.3.3** Verify Linux kernel capabilities configured with minimal set for elevated access <!-- [CHG-004] RENUMBER: was 3.3.4; ISVS master numbers this requirement 3.3.3 --> | 2(j), 2(k) | — | — | — | — | DS (EXE), LA (ROL) | 5.6-3 |
```

```markdown
| **3.4.13** Verify firmware update signing supports post-quantum or hybrid signatures <!-- [CHG-011] ADD-ROW: requirement present in ISVS master but absent from appendix; mappings verified per decision log --> | 2(c), 2(f) | — | — | — | — | SU (UPD), DP (CRY) | 5.3-4 |
```

For a removed row, no inline comment is possible; annotate the nearest
surviving row: `<!-- [CHG-007] REMOVE-ROW: former 3.3.6 removed, see decision log -->`
and rely on the decision log for the full before-state.

Table 2 edits are annotated the same way, in the clause cell of the changed
row.

## 2. Change Log & Decision Record

Placed **below Table 2**, above the appendix's original References section.

```markdown
---

## Change Log & Decision Record

Generated: <ISO date> · ISVS reference: <repo ref + commit/tag> ·
Appendix source: <URL or file + hash> · Method: isvs-appendix-b-updater skill

### Summary

| ID | Location | Type | Change | Confidence | Human review |
|----|----------|------|--------|------------|--------------|
| CHG-001 | Table 1, §3.3 | RENUMBER | 3.3.4→3.3.3, 3.3.5→3.3.4, 3.3.6→3.3.5 | High | No |
| CHG-002 | Table 1, 4.5.7 | REMOVE-MAPPING | ETSI 5.4-3 → 5.4-2 | High | No |
| ... | | | | | |

### CHG-001 — Renumber section 3.3 rows

- **Before:** rows 3.3.4 (kernel capabilities), 3.3.5 (seccomp), 3.3.6 (LSM); 3.3.3 absent.
- **After:** 3.3.3, 3.3.4, 3.3.5 respectively.
- **Rationale:** ISVS publication numbers these requirements 3.3.3–3.3.5.
  Text similarity confirms a one-position shift (consistency_report.json,
  shift_suspects, similarity 0.9+ for each row). Mappings carried over and
  re-verified against the canonical text.
- **Sources:**
  - ISVS V3 chapter, master branch, fetched 2026-07-08,
    https://raw.githubusercontent.com/OWASP/IoT-Security-Verification-Standard-ISVS/master/en/V3-Software_Platform_Requirements.md
    (sha256: <hash from isvs_requirements.json>)
- **Confidence:** High. **Human review:** not required.
```

Every entry must contain: Before / After / Rationale / Sources (URL + access
date + hash where available) / Confidence / Human review flag. For mapping
decisions, the rationale must name the clause and paraphrase why it does or
does not align (see mapping_heuristics.md evidence rules).

### Items requiring human decision

List anything not applied because it could not be verified:

```markdown
### Items requiring human decision

1. **RED 3.3(e) column for 3.4.13** — EN 18031-2 clause-level text is
   paywalled; regulation-level reading suggests `—`, confidence Low, not
   applied. A reviewer with EN 18031-2 access should confirm.
```

### Verification runs

Reproducibility block — the exact commands run and headline results:

```markdown
### Verification runs

| Step | Command | Result |
|------|---------|--------|
| Canonical fetch | fetch_isvs_requirements.py --ref master | 127 requirements, 5 chapters |
| Pre-audit consistency | consistency_check.py ... | 4 missing (3 out-of-scope), 3 unknown |
| Post-edit consistency | consistency_check.py ... (final) | 0 in-scope missing, 0 unknown |
| Post-edit reciprocity | cross_check_tables.py ... (final) | 0 errors, 0 qualifier mismatches |
```

## 3. Things that must survive unchanged

- The appendix's own Overview, Important Notes, and References sections stay,
  updated only where a change makes them factually wrong (e.g. scope note if
  the user asked to expand scope) — and any such edit is itself a CHG entry.
- Column order and header wording of both tables.
- The informative-status disclaimer. Never present the output as legal advice.
