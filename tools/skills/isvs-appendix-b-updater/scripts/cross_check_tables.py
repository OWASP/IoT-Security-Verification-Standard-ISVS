#!/usr/bin/env python3
"""Structural validation of Appendix B mappings.

Checks (no semantic judgment):
1. Clause identifiers used in Table 1 / Table 2 exist in the framework
   registry (references/framework_clauses.json). ETSI sub-provisions beyond
   the registry's known maximum are soft-flagged 'verify_against_source'.
2. Reciprocity between Table 1 and Table 2:
   - every (req -> clause) in Table 1 appears as (clause -> req) in Table 2
   - every (clause -> req) in Table 2 appears in Table 1
   - Partial / (P) qualifiers agree.
   RED and CRA Part II columns in Table 1 carry qualifiers rather than exact
   clause IDs, so for those frameworks reciprocity is checked at
   presence/absence level only.

Usage:
  python3 cross_check_tables.py appendix_parsed.json \
      --registry references/framework_clauses.json --out crosscheck_report.json
"""
import argparse
import json
import re
from pathlib import Path


def norm_clause(fw: str, clause: str) -> str:
    c = clause.strip()
    if fw == "nist":
        m = re.match(r"(?:Non-tech|DI|DC|DP|LA|SU|CS|DS)\s*\((\w+)\)", c, re.I)
        prefix = re.match(r"(Non-tech|DI|DC|DP|LA|SU|CS|DS)", c, re.I)
        if m and prefix:
            return f"{prefix.group(1).upper() if prefix.group(1).lower() != 'non-tech' else 'Non-tech'} ({m.group(1).upper()})"
    if fw == "etsi":
        m = re.match(r"(5\.\d+-\d+[A-Za-z]?)", c)
        if m:
            return m.group(1)
        m = re.match(r"5\.(\d+)\b", c)  # Table 2 uses provision level "5.6 (Provision 6)"
        if m:
            return f"5.{m.group(1)}"
    if fw == "cra_part1":
        m = re.search(r"\(?([1-9]|2\([a-m]\))\)?", c)
        m2 = re.match(r"2\(([a-z])\)", c)
        if m2:
            return f"2({m2.group(1)})"
    return c


def etsi_provision(clause: str) -> str:
    m = re.match(r"5\.(\d+)", clause)
    return f"5.{m.group(1)}" if m else clause


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("appendix", help="output of parse_appendix.py")
    ap.add_argument("--registry", required=True,
                    help="framework_clauses.json from the skill references/")
    ap.add_argument("--out", default="crosscheck_report.json")
    args = ap.parse_args()

    data = json.loads(Path(args.appendix).read_text())
    reg = json.loads(Path(args.registry).read_text())

    invalid, soft_flags = [], []

    # --- 1. validate clause identifiers -----------------------------------
    def check_clause(fw, clause, where):
        c = norm_clause(fw, clause)
        if fw == "cra_part1":
            if c not in reg["cra_part1"]["clauses"]:
                invalid.append({"framework": fw, "clause": clause, "where": where,
                                "reason": "not a CRA Annex I Part I clause"})
        elif fw == "nist":
            if c not in reg["nist"]["subcapabilities"]:
                invalid.append({"framework": fw, "clause": clause, "where": where,
                                "reason": "unknown SP 800-213A sub-capability"})
        elif fw == "etsi":
            m = re.match(r"5\.(\d+)(?:-(\d+))?", c)
            if not m or not (1 <= int(m.group(1)) <= 13):
                invalid.append({"framework": fw, "clause": clause, "where": where,
                                "reason": "not an EN 303 645 provision (5.1-5.13)"})
            elif m.group(2):
                known_max = reg["etsi"]["known_max_subprovision"].get(
                    f"5.{m.group(1)}", 0)
                if int(m.group(2)) > known_max:
                    soft_flags.append({
                        "framework": fw, "clause": clause, "where": where,
                        "reason": (f"sub-provision exceeds registry max "
                                   f"({known_max}) - verify against ETSI text")})

    for row in data["table1"]:
        for fw, toks in row["mappings"].items():
            for t in toks:
                if fw in ("red_d", "red_e", "red_f", "cra_part2"):
                    continue  # qualifier columns, no clause IDs
                check_clause(fw, t["clause"], f"Table1 {row['id']}")
    for fw, entries in data.get("table2", {}).items():
        if fw in ("cra_part2",):
            continue
        for e in entries:
            if e["refs"] or "—" in e.get("raw_line", ""):
                check_clause(fw, e["clause"], f"Table2 {fw}")

    # --- 2. reciprocity ----------------------------------------------------
    t1 = {}   # (fw, req, clause_or_fw) -> partial flag  (clause-level fws)
    t1_presence = {}  # (fw, req) -> True for qualifier-only fws
    for row in data["table1"]:
        rid = row["id"]
        for fw, toks in row["mappings"].items():
            for t in toks:
                if fw in ("red_d", "red_e", "red_f", "cra_part2"):
                    t1_presence[(fw, rid)] = True
                elif fw == "etsi":
                    t1[(fw, rid, etsi_provision(norm_clause(fw, t["clause"])))] = \
                        t["qualifier"] == "Partial"
                else:
                    t1[(fw, rid, norm_clause(fw, t["clause"]))] = \
                        t["qualifier"] == "Partial"

    t2 = {}
    t2_presence = {}
    for fw, entries in data.get("table2", {}).items():
        for e in entries:
            clause = norm_clause(fw, e["clause"])
            for ref in e["refs"]:
                if fw in ("red_d", "red_e", "red_f", "cra_part2"):
                    t2_presence[(fw, ref["id"])] = True
                    t2[(fw, ref["id"], clause)] = ref["partial"]
                else:
                    t2[(fw, ref["id"], clause)] = ref["partial"]

    clause_fws = ("cra_part1", "nist", "etsi")
    missing_in_t2 = [
        {"framework": fw, "requirement": rid, "clause": cl,
         "partial_in_table1": p}
        for (fw, rid, cl), p in sorted(t1.items())
        if fw in clause_fws and (fw, rid, cl) not in t2]
    missing_in_t1 = [
        {"framework": fw, "requirement": rid, "clause": cl,
         "partial_in_table2": p}
        for (fw, rid, cl), p in sorted(t2.items())
        if fw in clause_fws and (fw, rid, cl) not in t1]
    qualifier_mismatch = [
        {"framework": fw, "requirement": rid, "clause": cl,
         "table1_partial": t1[(fw, rid, cl)], "table2_partial": t2[(fw, rid, cl)]}
        for (fw, rid, cl) in sorted(set(t1) & set(t2))
        if fw in clause_fws and t1[(fw, rid, cl)] != t2[(fw, rid, cl)]]
    presence_gaps = []
    for fw in ("red_d", "red_e", "red_f", "cra_part2"):
        a = {r for (f, r) in t1_presence if f == fw}
        b = {r for (f, r) in t2_presence if f == fw}
        for rid in sorted(a - b):
            presence_gaps.append({"framework": fw, "requirement": rid,
                                  "issue": "in Table 1 but not in Table 2"})
        for rid in sorted(b - a):
            presence_gaps.append({"framework": fw, "requirement": rid,
                                  "issue": "in Table 2 but not in Table 1"})

    report = {
        "invalid_clause_ids": invalid,
        "soft_flags_verify_against_source": soft_flags,
        "reciprocity": {
            "table1_pairs_missing_in_table2": missing_in_t2,
            "table2_pairs_missing_in_table1": missing_in_t1,
            "partial_qualifier_mismatches": qualifier_mismatch,
            "presence_gaps_qualifier_frameworks": presence_gaps,
        },
        "note": ("ETSI reciprocity is checked at provision level (5.N) because "
                 "Table 2 aggregates sub-provisions. Every listed asymmetry is "
                 "a mechanical defect: fix the side contradicted by evidence "
                 "and log the change. Note that published appendices often "
                 "mark Partial only in Table 2 ((P)) and not in Table 1 cells; "
                 "each qualifier mismatch still needs a decision (usually: add "
                 "the qualifier to Table 1) recorded in the change log."),
    }
    Path(args.out).write_text(json.dumps(report, indent=2, ensure_ascii=False))
    print(f"invalid_clause_ids={len(invalid)} soft_flags={len(soft_flags)}")
    print(f"t1->t2 missing={len(missing_in_t2)} t2->t1 missing={len(missing_in_t1)} "
          f"qualifier_mismatches={len(qualifier_mismatch)} "
          f"presence_gaps={len(presence_gaps)}")
    print(f"-> {args.out}")


if __name__ == "__main__":
    main()
