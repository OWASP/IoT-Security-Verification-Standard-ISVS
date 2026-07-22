# Mapping decision heuristics

Read this before performing the semantic verification step (SKILL.md Step 5).

## Decision criteria

For each (ISVS requirement × framework clause) pair, compare the **canonical
ISVS requirement text** (never the appendix's shortened summary) with the
**actual clause text** fetched from the source in `framework_clauses.json`.

| Verdict | Criterion |
|---|---|
| **Direct** (clause listed without qualifier) | Implementing the ISVS requirement substantively fulfils the technical intent of the clause at device level. |
| **Partial** | The ISVS requirement addresses a real subset of the clause, but the clause also demands organizational/process measures or additional technical controls the requirement does not cover. |
| **—** | No meaningful technical alignment, OR the clause operates at ecosystem/network/process level outside a device-level standard's scope (record which of the two reasons applies). |

## Framework-specific guidance

**CRA Annex I Part I (2(a)–2(m))** — clause-level mapping. Read the actual
Annex I text on EUR-Lex; do not rely on the short descriptions in the
appendix's Table 2. Typical pitfalls: 2(g) is data *minimization* (not
generic confidentiality — that is 2(e)); 2(i) is impact on *other* devices
and networks and is legitimately `—` for almost every device-level
requirement; 2(k) is exploitation-mitigation mechanisms (memory safety
features, code signing at execution time).

**CRA Annex I Part II** — obligations, not numbered clauses. Table 1 uses
labels such as `Part II (SBOM)`, `Part II (CVD)`, `Part II`. Keep that
labeling convention; verify the obligation actually exists in Part II text.

**RED 3.3(d)/(e)/(f)** — the harmonized EN 18031-1/-2/-3 texts are paywalled.
Verdicts here can be made at the level of the delegated regulation's
objectives (network protection / privacy / fraud), which justifies `Partial`
or `—` but rarely a confident `Direct`. Anything needing EN 18031 clause-level
confirmation goes to "Items requiring human decision". Remember 3.3(f) only
applies to payment/monetary-transfer capable equipment.

**NIST SP 800-213A** — map to sub-capability identifiers, format
`AREA (SUB)`, e.g. `DP (KEY)`. The catalog PDF/DOI is freely accessible.
A mapping is justified when the requirement implements one of the
sub-capability's listed device capabilities. Prefer the 1–3 most specific
sub-capabilities over long lists.

**ETSI EN 303 645 v2.1.1** — map to provision identifiers `5.N-M`. The PDF is
freely downloadable from ETSI. Check whether the provision is mandatory
("shall") or a recommendation ("should") — both may be mapped, but if the
alignment hinges on a conditional provision, prefer `Partial` and say so.

## Evidence rules for the decision log

- Cite: framework name, clause/provision ID, source URL, and access date.
- Paraphrase clause content in your own words; keep any direct quotation
  under ~10 words.
- State the comparison explicitly: "ISVS 4.5.6 requires random generation of
  the Zigbee network key; ETSI 5.4-2 concerns unique critical security
  parameters — alignment is partial because …".
- Assign a confidence: **High** (clause text read from source), **Medium**
  (decided from regulation-level text where the harmonized standard is
  paywalled), **Low** (inference only — must go to human review, and must NOT
  be applied as a change).

## Consistency obligations when editing

- Any change to a Table 1 cell must be mirrored in Table 2 (and vice versa),
  including the Partial/(P) qualifier. Rerun `cross_check_tables.py` to prove
  reciprocity after editing.
- When renumbering a requirement ID, carry its mappings with it, then
  re-verify that the mappings still match the *canonical* text of the new ID
  (renumbering often reveals the mappings belonged to the neighbour).
- When adding a brand-new requirement row (in-scope omission), populate every
  framework column with a verified verdict or `—`; never leave cells blank.
