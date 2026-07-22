#!/usr/bin/env python3
"""Check Appendix B Table 1 against the canonical ISVS requirement list.

Covers user goal 1: numbering consistency + completeness (no items left out).

Outputs JSON with:
  missing_in_appendix   canonical IDs absent from Table 1
  unknown_in_appendix   Table 1 IDs not in the publication
  numbering_gaps        holes inside a section's sequence in Table 1
  order_violations      rows out of ascending order
  text_drift            rows whose summary poorly matches canonical text
  shift_suspects        unknown IDs whose text matches a *different*
                        canonical ID (classic off-by-one renumbering)

Usage:
  python3 consistency_check.py isvs_requirements.json appendix_parsed.json \
      --out consistency_report.json [--drift-threshold 0.35]
"""
import argparse
import json
import re
from pathlib import Path

STOP = {"verify", "that", "the", "a", "an", "is", "are", "and", "or", "of",
        "to", "for", "on", "in", "with", "using", "used", "not", "be", "can"}


def toks(s: str):
    return {w for w in re.findall(r"[a-z0-9]+", s.lower()) if w not in STOP}


def jaccard(a: str, b: str) -> float:
    ta, tb = toks(a), toks(b)
    if not ta or not tb:
        return 0.0
    return len(ta & tb) / len(ta | tb)


def key(rid: str):
    return tuple(int(p) for p in rid.split("."))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("canonical", help="output of fetch_isvs_requirements.py")
    ap.add_argument("appendix", help="output of parse_appendix.py")
    ap.add_argument("--out", default="consistency_report.json")
    ap.add_argument("--drift-threshold", type=float, default=0.35,
                    help="Jaccard similarity below which a row is flagged")
    args = ap.parse_args()

    canonical = json.loads(Path(args.canonical).read_text())
    appendix = json.loads(Path(args.appendix).read_text())

    canon = {r["id"]: r for r in canonical["requirements"]}
    rows = appendix["table1"]
    app_ids = [r["id"] for r in rows]
    app_set = set(app_ids)

    missing = sorted(set(canon) - app_set, key=key)
    unknown = sorted(app_set - set(canon), key=key)
    duplicates = sorted({i for i in app_ids if app_ids.count(i) > 1}, key=key)

    order_violations = [
        {"position": i, "id": app_ids[i], "previous": app_ids[i - 1]}
        for i in range(1, len(app_ids)) if key(app_ids[i]) <= key(app_ids[i - 1])
    ]

    # gaps within each section actually present in the appendix
    numbering_gaps = []
    by_section = {}
    for rid in app_ids:
        c, s, n = key(rid)
        by_section.setdefault((c, s), []).append(n)
    for (c, s), nums in by_section.items():
        nums = sorted(set(nums))
        for a, b in zip(nums, nums[1:]):
            for gap in range(a + 1, b):
                numbering_gaps.append({
                    "section": f"{c}.{s}", "missing": f"{c}.{s}.{gap}",
                    "exists_in_publication": f"{c}.{s}.{gap}" in canon,
                })

    text_drift, paraphrase_notes, shift_suspects = [], [], []
    for r in rows:
        if r["id"] in canon:
            sim = jaccard(r["summary"], canon[r["id"]]["text"])
            if sim < args.drift_threshold:
                best = max(canonical["requirements"],
                           key=lambda c: jaccard(r["summary"], c["text"]))
                best_sim = jaccard(r["summary"], best["text"])
                entry = {
                    "id": r["id"], "similarity": round(sim, 2),
                    "appendix_summary": r["summary"],
                    "canonical_text": canon[r["id"]]["text"],
                    "best_matching_canonical_id": best["id"],
                    "best_similarity": round(best_sim, 2),
                }
                # Actionable drift: the summary matches a DIFFERENT canonical
                # requirement noticeably better -> likely renumbering error.
                if best["id"] != r["id"] and best_sim - sim >= 0.15:
                    text_drift.append(entry)
                else:
                    # Same-ID low similarity is usually just a shortened
                    # summary; informational only.
                    paraphrase_notes.append(entry)
        else:
            best = max(canonical["requirements"],
                       key=lambda c: jaccard(r["summary"], c["text"]))
            shift_suspects.append({
                "appendix_id": r["id"],
                "appendix_summary": r["summary"],
                "likely_canonical_id": best["id"],
                "similarity": round(jaccard(r["summary"], best["text"]), 2),
                "canonical_text": best["text"],
            })

    scope_notes = appendix.get("scope_notes", [])
    report = {
        "canonical_count": len(canon),
        "appendix_row_count": len(rows),
        "missing_in_appendix": missing,
        "unknown_in_appendix": unknown,
        "duplicates_in_appendix": duplicates,
        "order_violations": order_violations,
        "numbering_gaps": numbering_gaps,
        "text_drift_renumber_suspects": text_drift,
        "paraphrase_notes_informational": paraphrase_notes,
        "shift_suspects": shift_suspects,
        "scope_notes_for_manual_scope_decision": scope_notes,
        "note": ("Classify each missing ID as in-scope or out-of-scope using "
                 "the scope notes before treating it as an omission. "
                 "shift_suspects with high similarity usually indicate "
                 "renumbering, not new requirements."),
    }
    Path(args.out).write_text(json.dumps(report, indent=2, ensure_ascii=False))
    print(f"canonical={len(canon)} appendix_rows={len(rows)}")
    print(f"missing={len(missing)} unknown={len(unknown)} "
          f"dupes={len(duplicates)} gaps={len(numbering_gaps)} "
          f"order_violations={len(order_violations)} "
          f"drift_renumber_suspects={len(text_drift)} "
          f"paraphrase_notes={len(paraphrase_notes)} "
          f"shift_suspects={len(shift_suspects)}")
    print(f"-> {args.out}")


if __name__ == "__main__":
    main()
