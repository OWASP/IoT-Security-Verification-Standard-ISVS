# Output format: tailored custom mapping

The deliverable is a pair of files with identical content in two shapes:
`custom_mapping.json` (machine-readable) and `custom_mapping.md`
(human-reviewable). A reviewer must be able to accept or question each
applicability verdict independently without consulting anything outside the
markdown file.

## 1. Markdown header

```markdown
# Custom ISVS Mapping — <product_name>

> **Informative only.** This tailored mapping is a scoping aid. It does not
> constitute legal or conformity advice. Satisfying ISVS requirements does
> not constitute compliance with any listed regulation, and compliance with a
> framework cannot be claimed solely based on this mapping.

- Generated: <ISO date>
- ISVS reference: <branch/tag/commit + fetch date>
- Base mapping: en/Appendix_B-Compliance_Mapping.md (<hash or ref>)
- Framework versions: CRA (EU) 2024/2847; RED (EU) 2022/30 (EN 18031-1/-2/-3);
  NIST SP 800-213A; ETSI EN 303 645 v2.1.1
- Context: <inline context JSON or its SHA-256 plus key fields>
- Method: isvs-custom-mapping-builder skill
```

## 2. Applicability table

One row per canonical ISVS requirement, in ascending ID order. Framework
columns preserve Appendix B Table 1 order and cell values verbatim.

```markdown
| ISVS Req | Applicability | Reason | CRA-I | CRA-II | RED-d | RED-e | RED-f | NIST 800-213A | ETSI 303 645 | Context note | Confidence |
|----------|---------------|--------|-------|--------|-------|-------|-------|---------------|--------------|--------------|------------|
| **1.1.5** | in_scope | handles personal data and public disclosure duty | — | Part II (CVD) | — | — | — | Non-tech (BUG) | 5.2-1, 5.2-2 | context note if any | High |
| **9.9.9** | review | update_mechanism is null | ... | ... | ... | ... | ... | ... | ... | confirm update path before scoping | Low |
```

Rules: no blank framework cells (use `—` or the preserved Appendix B value,
`TBD` only with a reason); applicability in
`{in_scope, out_of_scope, review}`; every `review` row names its question in
Context note; confidence in `{High, Medium, Low}`.

## 3. Decision log

Below the table, one entry per non-trivial scoping decision plus a summary
of rule applications:

```markdown
## Decision Log

- **1.1.5 → in_scope (High).** Reason: context handles personal data.
  Sources: context.json; ISVS V1 chapter; Appendix B Table 1 cell preserved.
- **RED-f column → not applicable by context (payment_capable false).**
  Cells preserved verbatim; context note added. No alignment edited.
```

Every entry lists: verdict, reason tied to a context field, sources (ISVS
ref, Appendix B source, framework source URLs where consulted), and
confidence. Low-confidence entries must point at the human-review queue.

## 4. Items requiring human decision

```markdown
## Items Requiring Human Decision

1. **Update-related requirements (e.g. 1.2.9)** — update_mechanism is null.
   Confirm the update path, then rerun the build with a completed context.
2. **Payment-adjacent RED-f notes** — payment_capable is null. Confirm
   whether the product can initiate monetary transfer.
```

## 5. Verification runs

```markdown
## Verification Runs

| Step | Command | Result |
|------|---------|--------|
| Build | build_custom_mapping.py --local-dir ... | N requirements, X in_scope, Y out_of_scope, Z review |
| Validate | validate_custom_mapping.py ... | 0 errors |
```

## 6. Things that must survive unchanged

- The informative-only disclaimer above, verbatim.
- ISVS requirement IDs and canonical text references.
- Appendix B framework cell values, order, and header wording.
- Framework source URLs and version labels.
