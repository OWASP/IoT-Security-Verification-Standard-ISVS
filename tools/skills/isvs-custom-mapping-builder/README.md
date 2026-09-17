# isvs-custom-mapping-builder

Builds a **product-context-specific** mapping from ISVS requirements to other
standards (EU CRA, RED/EN 18031, NIST SP 800-213A, ETSI EN 303 645) by
filtering the generalized Appendix B mapping.

Appendix B is a useful generalized mapping, but it is not equally applicable
to every business or product context. This skill takes a short product
context and produces a tailored, human-reviewable mapping that says, per ISVS
requirement: in scope, out of scope, or needs human review — carrying over
the Appendix B framework alignments verbatim, with versions, sources, and
uncertain items preserved.

This skill works **with any AI assistant, or with none at all** — see
[Model-agnostic use](#model-agnostic-use) below.

## What it does

1. **Parses** canonical ISVS requirements (V1–V5 chapters) and Appendix B
   Table 1 (ISVS → Frameworks).
2. **Filters** by product context (device type, connectivity, personal data,
   payment capability, target markets, update mechanism) using deterministic
   rules — see `references/mapping_policy.md`.
3. **Emits** a tailored markdown file plus a machine-readable JSON file. Both
   record ISVS and framework versions, source URLs, per-requirement
   applicability with reasons, preserved framework alignments, confidence,
   and a human-review queue.

Anything the scripts cannot decide from context alone becomes `review` or
`TBD` with a reason and reviewer prompt. The skill never invents new
framework equivalence and never claims compliance.

## Model-agnostic use

`SKILL.md` in this directory is written as Claude Code's entry point — it's
what Claude Code loads when you invoke `/isvs-custom-mapping-builder`. That
invocation mechanism only works in Claude Code. Everything it tells Claude
Code to do, you (or any other AI assistant) can do directly:

### 1. Describe the product context

Create `context.json` following the schema and archetypes in
`references/context_profiles.md`. Unknown fields must be `null`, not guessed.
Example minimal context:

```json
{
  "product_name": "Example Wi-Fi camera",
  "device_type": "consumer_camera",
  "connectivity": ["wifi"],
  "handles_personal_data": true,
  "payment_capable": false,
  "target_markets": ["EU"],
  "safety_critical": false,
  "update_mechanism": "ota",
  "notes": "Cloud-backed video, mobile app onboarding"
}
```

### 2. Run the mechanical build

From this directory:

```bash
python3 scripts/build_custom_mapping.py \
  --local-dir ../../../en \
  --context /tmp/isvs-custom/context.json \
  --out-json /tmp/isvs-custom/custom_mapping.json \
  --out-md /tmp/isvs-custom/custom_mapping.md
python3 scripts/validate_custom_mapping.py \
  /tmp/isvs-custom/custom_mapping.json \
  --out /tmp/isvs-custom/validation_report.json
```

Use `--isvs-ref <tag-or-branch>` to pin versions in the output header instead
of the default local-checkout label. Read the JSON reports with any tool —
`jq`, Python, or by eye.

### 3. Do the semantic review

For each `review` item in the generated markdown:

1. Read `references/mapping_policy.md` for the applicability decision
   criteria and the framework-specific caveats (e.g. RED 3.3(f) only applies
   to payment-capable equipment; CRA 2(i) is legitimately out of scope for
   most device-level requirements).
2. Compare the **canonical** ISVS requirement text against the actual product
   behavior and, where a framework alignment is in doubt, the cited clause
   text — don't rely on paraphrase from memory.
3. Update the context file (not the generated output) when the product
   description was incomplete, then rerun the build so the decision log stays
   reproducible.

Framework alignments themselves must not be edited in the tailored copy. If
an alignment looks wrong, report it against Appendix B instead.

### 4. Write up the change

Follow `references/output_format.md`: version header with ISVS ref and
framework versions, applicability table with preserved framework columns,
decision log with sources and confidence, human-review queue, verification
runs, and Appendix B's informative-status disclaimer verbatim.

### 5. Verify

Re-run the validator against the final JSON and confirm zero errors before
submitting. Include the ISVS ref, Appendix B source, context summary, and
validation headline in the PR description.

## Files

- `SKILL.md` — Claude Code's entry point; step-by-step playbook (same content
  as this README's workflow, phrased as direct instructions to an agent).
- `scripts/build_custom_mapping.py` — parses requirements and Appendix B,
  applies context rules, writes tailored JSON + markdown.
- `scripts/validate_custom_mapping.py` — schema, coverage, version, source,
  and no-compliance-claim checks on the generated JSON.
- `references/context_profiles.md` — context JSON schema plus three worked
  product archetypes used for validation.
- `references/mapping_policy.md` — applicability and verdict criteria,
  version and source preservation rules, framework caveats.
- `references/output_format.md` — exact format for the tailored mapping file
  and its decision log.
- `examples/` — sample context files and expected validation headlines.

## Limitations

- The tailored file inherits Appendix B's coverage and versions. It does not
  add mappings for ISVS requirements introduced after the Appendix B scope
  note, and it does not track framework revisions beyond the versions stated
  in its header.
- RED EN 18031 clause-level text is paywalled; RED verdicts carried over from
  Appendix B stay at qualifier level and anything needing clause confirmation
  stays in the human-review queue.
- Output is a scoping aid only. It is informative, not legal or conformity
  advice, and must not be presented as a compliance claim.
