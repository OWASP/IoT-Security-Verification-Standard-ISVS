# Mapping policy: applicability, verdicts, versions, and evidence

Read this before reviewing the `review` queue. It mirrors the decision
discipline of Appendix B itself: every tailored verdict must be traceable,
versioned, and honest about uncertainty.

## Applicability verdicts

For each canonical ISVS requirement, the build script emits one of:

| Verdict | Criterion |
|---------|-----------|
| `in_scope` | The product context clearly exercises the requirement (e.g. personal-data handling for a camera, OTA update controls for an OTA product, radio requirements for a radio product). |
| `out_of_scope` | The product context clearly does not exercise the requirement (e.g. payment-fraud controls for a provably non-payment product, privacy-erasure flows for a product with no personal data). The reason must name the context field that excludes it. |
| `review` | The context is unknown (`null`), ambiguous, or the requirement needs a human to confirm product behavior. Carries a reviewer prompt naming the exact question to answer. |

Rules are intentionally conservative: unknown context produces `review`, not
`out_of_scope`. Nothing is silently dropped — every canonical requirement
appears in the output.

## Framework alignment handling

- Framework cells are **copied verbatim** from Appendix B Table 1, including
  `Partial` qualifiers and `—` (no alignment). The tailored file never edits
  an alignment to fit the product.
- A context note may be appended alongside a preserved cell (e.g. "RED
  3.3(f) preserved from Appendix B; not applicable by context because
  `payment_capable` is false"), but the original cell value stays intact.
- Any alignment not present in Appendix B and not verifiable against a cited
  source is recorded as `TBD` with a reason and reviewer prompt. `TBD` items
  must not be presented as mappings.
- Confidence per row is **High** (decided from explicit context fields),
  **Medium** (decided from notes plus context fields), or **Low** (inference
  only — always `review`).

## Version and source preservation

Every tailored output records:

- ISVS ref: branch/tag/commit plus fetch date and, for local builds, the
  SHA-256 of each chapter file used.
- Framework versions covered by the base Appendix B: EU CRA Regulation
  (EU) 2024/2847, RED Delegated Regulation (EU) 2022/30 (EN 18031-1/-2/-3),
  NIST SP 800-213A, ETSI EN 303 645 v2.1.1.
- Source URLs: ISVS raw chapter URLs, the Appendix B file or URL, and the
  framework source URLs carried over from the base mapping.
- The exact context file (inline JSON or hash) so the run is reproducible.

If a framework is amended after the base Appendix B, do not silently
remap — record the newer version as "not tracked by base mapping, human
review required".

## Framework-specific caveats

Carried over from Appendix B practice:

- **CRA 2(i)** (impact on other devices/networks) is legitimately `—` for
  most device-level requirements. That is not a content gap.
- **CRA 2(g)** is data minimization, not generic confidentiality (which is
  2(e)). Do not conflate them when reviewing context notes.
- **RED 3.3(f)** applies to payment or monetary-transfer capable equipment
  only. For non-payment products the column is preserved but flagged not
  applicable by context.
- **RED EN 18031-1/-2/-3** clause-level texts are paywalled. Qualifier-level
  verdicts from Appendix B are preserved as-is; anything needing
  clause-level confirmation stays in the human-review queue.
- **NIST SP 800-213A** identifiers use `AREA (SUB)` form (e.g. `DP (KEY)`).
  Preserve them exactly; do not shorten or expand.
- **ETSI EN 303 645** provisions use `5.N-M` form. Check mandatory versus
  recommendation status before treating a context note as decisive.

## Banned language

Tailored outputs must not contain compliance claims. The validator rejects
phrases such as "compliant", "certified", "satisfies CRA", "meets RED", or
"proves conformity" when applied to the product. Acceptable phrasing is
"supports", "partially addresses at device level", or "no meaningful
alignment", each tied to a specific ISVS requirement and framework clause.
The informative-only disclaimer must appear verbatim in every tailored file.
