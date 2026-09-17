#!/usr/bin/env python3
"""Validate a tailored custom mapping JSON from build_custom_mapping.py.

Checks: schema, coverage, versions, sources, verdict domains, no blank
framework cells, no compliance-claim language, review items carry prompts.

Usage:
  python3 validate_custom_mapping.py custom_mapping.json --out validation_report.json
"""
import argparse
import json
import re
from pathlib import Path

ALLOWED_APPLICABILITY = {"in_scope", "out_of_scope", "review"}
ALLOWED_CONFIDENCE = {"High", "Medium", "Low"}
FRAMEWORK_KEYS = ["cra1", "cra2", "redd", "rede", "redf", "nist", "etsi"]
BANNED_PHRASES = [
    r"\bcompliant\b", r"\bcertified\b", r"\bsatisfies cra\b", r"\bmeets red\b",
    r"\bproves conformity\b", r"\bguarantees compliance\b", r"\bfully compliant\b",
]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("mapping_json")
    ap.add_argument("--out", default="validation_report.json")
    args = ap.parse_args()

    data = json.loads(Path(args.mapping_json).read_text(encoding="utf-8"))
    errors, warnings = [], []

    for key in ["generated", "isvs_ref", "base_mapping", "framework_versions",
                "sources", "context", "counts", "mappings"]:
        if key not in data:
            errors.append(f"missing top-level key: {key}")

    for skey in ["cra", "red", "nist", "etsi", "isvs_repo"]:
        if "sources" in data and skey not in data["sources"]:
            errors.append(f"missing source URL: {skey}")

    if "framework_versions" in data and "CRA" not in data["framework_versions"]:
        errors.append("framework_versions does not mention CRA")

    seen = set()
    for m in data.get("mappings", []):
        rid = m.get("id", "<missing>")
        if rid in seen:
            errors.append(f"duplicate requirement id: {rid}")
        seen.add(rid)
        if m.get("applicability") not in ALLOWED_APPLICABILITY:
            errors.append(f"{rid}: bad applicability {m.get('applicability')}")
        if m.get("confidence") not in ALLOWED_CONFIDENCE:
            errors.append(f"{rid}: bad confidence {m.get('confidence')}")
        if not m.get("reason"):
            errors.append(f"{rid}: empty reason")
        fw = m.get("frameworks", {})
        for fk in FRAMEWORK_KEYS:
            if fk not in fw or str(fw[fk]).strip() == "":
                errors.append(f"{rid}: blank framework cell {fk}")
        if m.get("applicability") == "review" and not m.get("reviewer_prompt"):
            errors.append(f"{rid}: review without reviewer_prompt")
        blob = f"{m.get('reason','')} {m.get('context_note','')}".lower()
        for pat in BANNED_PHRASES:
            if re.search(pat, blob):
                errors.append(f"{rid}: banned compliance-claim language matching {pat}")

    counts = data.get("counts", {})
    actual = {
        "total": len(data.get("mappings", [])),
        "in_scope": sum(1 for m in data.get("mappings", []) if m.get("applicability") == "in_scope"),
        "out_of_scope": sum(1 for m in data.get("mappings", []) if m.get("applicability") == "out_of_scope"),
        "review": sum(1 for m in data.get("mappings", []) if m.get("applicability") == "review"),
    }
    if counts != actual:
        errors.append(f"counts mismatch: header {counts} vs actual {actual}")

    # ID order check (warning only)
    ids = [m.get("id", "") for m in data.get("mappings", [])]
    def key(r):
        try:
            return tuple(int(p) for p in r.split("."))
        except Exception:
            return (9999,)
    ordered = sorted(ids, key=key)
    if ids != ordered:
        warnings.append("mappings not in ascending ID order")

    report = {"errors": errors, "warnings": warnings, "counts": actual,
              "total_mappings": actual["total"]}
    Path(args.out).write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, indent=2))
    raise SystemExit(1 if errors else 0)


if __name__ == "__main__":
    main()
