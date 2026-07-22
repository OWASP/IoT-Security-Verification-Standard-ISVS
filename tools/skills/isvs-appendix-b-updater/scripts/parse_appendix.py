#!/usr/bin/env python3
"""Parse ISVS Appendix B (Compliance Mapping) markdown into structured JSON.

Handles both the repo markdown and HTML->markdown conversions of the
published page. Extracts:

* table1: one record per ISVS requirement row, with every framework column
  kept verbatim plus a normalized token list per cell.
* table2: framework -> clause -> list of ISVS refs (with partial flags),
  detected per framework section heading.
* scope_exclusions: ID prefixes / topics the scope note declares out of scope
  (best-effort textual detection; review manually).

Usage:
  python3 parse_appendix.py appendix_b.md --out appendix_parsed.json
"""
import argparse
import json
import re
from pathlib import Path

REQ_ID = re.compile(r"\b(\d+\.\d+\.\d+)\b")
T1_ROW = re.compile(r"^\|\s*\*\*(\d+\.\d+\.\d+)\*\*\s*(.*?)\s*\|(.*)\|\s*$")
CHAPTER_ROW = re.compile(r"^\|\s*\*\*V(\d)\b")
HEADING = re.compile(r"^#{2,4}\s*(?:\[[^\]]*\]\([^)]*\)\s*)?(.+?)\s*$")

# Table 2 section heading -> framework key (matched by substring, lowercase)
T2_SECTIONS = [
    ("annex i, part ii", "cra_part2"),
    ("annex i part ii", "cra_part2"),
    ("annex i, part i", "cra_part1"),
    ("annex i part i", "cra_part1"),
    ("3.3(d)", "red_d"),
    ("18031-1", "red_d"),
    ("3.3(e)", "red_e"),
    ("18031-2", "red_e"),
    ("3.3(f)", "red_f"),
    ("18031-3", "red_f"),
    ("800-213a", "nist"),
    ("303 645", "etsi"),
]

T1_COLUMNS = ["cra_part1", "cra_part2", "red_d", "red_e", "red_f",
              "nist", "etsi"]


def strip_md(s: str) -> str:
    s = re.sub(r"<!--.*?-->", "", s, flags=re.S)
    s = s.replace("**", "").replace("\\_", "_")
    return re.sub(r"\s+", " ", s).strip()


def cell_tokens(cell: str, framework: str):
    """Normalize a Table 1 cell into a list of clause tokens with flags."""
    c = strip_md(cell)
    if c in ("", "—", "-", "–", "N/A"):
        return []
    if framework in ("red_d", "red_e", "red_f"):
        # RED columns hold qualifiers, not clause IDs
        return [{"clause": "RED", "qualifier": c}]
    if framework == "cra_part2":
        return [{"clause": c, "qualifier": None}]
    toks = []
    for part in re.split(r",\s*(?![^()]*\))", c):
        part = part.strip()
        if not part:
            continue
        partial = bool(re.search(r"\bpartial\b|\(P\)", part, re.I))
        clause = re.sub(r"\s*\(P\)|\bpartial\b", "", part, flags=re.I).strip(" ,")
        toks.append({"clause": clause, "qualifier": "Partial" if partial else None})
    return toks


def parse_table1(lines):
    rows, order = [], 0
    for ln in lines:
        if CHAPTER_ROW.match(ln):
            continue
        m = T1_ROW.match(ln.rstrip())
        if not m:
            continue
        rid, desc, rest = m.group(1), strip_md(m.group(2)), m.group(3)
        cells = [c for c in rest.split("|")]
        # pad/truncate to expected column count
        cells = (cells + [""] * len(T1_COLUMNS))[:len(T1_COLUMNS)]
        mappings = {fw: cell_tokens(cell, fw)
                    for fw, cell in zip(T1_COLUMNS, cells)}
        rows.append({"order": order, "id": rid, "summary": desc,
                     "raw_cells": [strip_md(c) for c in cells],
                     "mappings": mappings, "raw_line": ln.rstrip()})
        order += 1
    return rows


def parse_table2(text: str):
    """Return {framework: [{clause, description, refs:[{id, partial}]}]}"""
    out = {}
    current = None
    for ln in text.splitlines():
        h = HEADING.match(ln)
        if h:
            title = h.group(1).lower()
            current = None
            for needle, key in T2_SECTIONS:
                if needle in title:
                    current = key
                    out.setdefault(current, [])
                    break
            continue
        if current is None or not ln.strip().startswith("|"):
            continue
        cells = [strip_md(c) for c in ln.strip().strip("|").split("|")]
        if len(cells) < 2 or set(cells[0]) <= set("- :"):
            continue  # separator row
        clause = cells[0]
        refs_cell = cells[-1]
        if not clause or clause.lower().startswith(("cra annex", "red 3.3",
                                                    "sp 800-213a", "en 303 645",
                                                    "clause", "provision")):
            continue  # header row
        refs = []
        for m in re.finditer(r"(\d+\.\d+\.\d+)(\s*\*{0,2}\(P\)\*{0,2})?", refs_cell):
            refs.append({"id": m.group(1), "partial": bool(m.group(2))})
        # skip pure section-label rows like "**Device Identification (DI)**"
        if not refs and ("—" not in refs_cell and refs_cell.strip() != "-"
                         and not refs_cell.strip()):
            continue
        out[current].append({
            "clause": clause,
            "description": cells[1] if len(cells) > 2 else "",
            "refs": refs,
            "raw_line": ln.rstrip(),
        })
    return out


def detect_scope_exclusions(text: str):
    notes = []
    for para in re.split(r"\n\s*\n", text):
        p = strip_md(para)
        if re.search(r"scope note|future update|will be incorporated|"
                     r"subsequent release", p, re.I):
            notes.append(p)
    return notes


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("appendix", help="Appendix B markdown file")
    ap.add_argument("--out", default="appendix_parsed.json")
    args = ap.parse_args()

    text = Path(args.appendix).read_text(encoding="utf-8", errors="replace")

    # Table 1 = everything before the Table 2 heading
    t2_split = re.split(r"^#{2,3}.*Table 2.*$", text, maxsplit=1, flags=re.M)
    t1_text = t2_split[0]
    t2_text = t2_split[1] if len(t2_split) > 1 else ""

    table1 = parse_table1(t1_text.splitlines())
    table2 = parse_table2(t2_text)

    out = {
        "source_file": args.appendix,
        "table1_row_count": len(table1),
        "table1": table1,
        "table2": table2,
        "scope_notes": detect_scope_exclusions(text),
    }
    Path(args.out).write_text(json.dumps(out, indent=2, ensure_ascii=False))
    t2_counts = {k: len(v) for k, v in table2.items()}
    print(f"Table 1: {len(table1)} requirement rows")
    print(f"Table 2 sections: {json.dumps(t2_counts)}")
    print(f"Scope notes detected: {len(out['scope_notes'])}")
    print(f"-> {args.out}")


if __name__ == "__main__":
    main()
