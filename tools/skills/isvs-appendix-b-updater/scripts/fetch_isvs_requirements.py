#!/usr/bin/env python3
"""Fetch canonical ISVS requirements from the OWASP ISVS repository.

Extracts every requirement ID (e.g. 3.4.13), its full text, and its
L1/L2/L3 applicability from the chapter markdown files (V1-V5).

Provenance (source URL or local path + SHA-256 of each file) is recorded in
the output JSON so the decision log can cite exactly what was compared.

Usage:
  python3 fetch_isvs_requirements.py --ref master --out isvs_requirements.json
  python3 fetch_isvs_requirements.py --local-dir ./isvs_chapters --out isvs_requirements.json
"""
import argparse
import datetime
import hashlib
import json
import re
import sys
import urllib.request
from pathlib import Path

CHAPTER_FILES = [
    "V1-IoT_Ecosystem_Requirements.md",
    "V2-User_Space_Application_Requirements.md",
    "V3-Software_Platform_Requirements.md",
    "V4-Communication_Requirements.md",
    "V5-Hardware_Platform_Requirements.md",
]
RAW_BASE = ("https://raw.githubusercontent.com/OWASP/"
            "IoT-Security-Verification-Standard-ISVS/{ref}/en/{name}")

# Requirement row: | **1.2.3** | Verify ... | ✓ | ✓ | ✓ |
REQ_ROW = re.compile(
    r"^\|\s*\*\*(\d+\.\d+\.\d+)\*\*\s*\|\s*(.*?)\s*\|(.*)$")


def fetch(url: str) -> bytes:
    req = urllib.request.Request(url, headers={"User-Agent": "isvs-appendix-audit"})
    with urllib.request.urlopen(req, timeout=60) as r:
        return r.read()


def parse_chapter(text: str, source: str):
    reqs = []
    for line in text.splitlines():
        m = REQ_ROW.match(line.strip())
        if not m:
            continue
        rid, desc, rest = m.group(1), m.group(2), m.group(3)
        cols = [c.strip() for c in rest.split("|")]
        # levels are the next up-to-3 columns; a checkmark or 'x' marks applicability
        lvl = [bool(re.search(r"[✓xX✔]", c)) for c in cols[:3]] + [False] * 3
        reqs.append({
            "id": rid,
            "text": re.sub(r"\s+", " ", desc).strip(),
            "levels": {"L1": lvl[0], "L2": lvl[1], "L3": lvl[2]},
            "source": source,
        })
    return reqs


def sort_key(rid: str):
    return tuple(int(p) for p in rid.split("."))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--ref", default="master",
                    help="git ref (branch/tag) of the ISVS repo, e.g. master or v1.0")
    ap.add_argument("--local-dir",
                    help="directory containing the V1-V5 chapter .md files "
                         "(used instead of fetching from GitHub)")
    ap.add_argument("--out", default="isvs_requirements.json")
    args = ap.parse_args()

    requirements, provenance, errors = [], [], []
    for name in CHAPTER_FILES:
        try:
            if args.local_dir:
                p = Path(args.local_dir) / name
                data, source = p.read_bytes(), str(p)
            else:
                source = RAW_BASE.format(ref=args.ref, name=name)
                data = fetch(source)
        except Exception as e:  # noqa: BLE001
            errors.append({"file": name, "error": str(e)})
            continue
        text = data.decode("utf-8", errors="replace")
        chapter_reqs = parse_chapter(text, source)
        if not chapter_reqs:
            errors.append({"file": name,
                           "error": "no requirement rows parsed - check format"})
        requirements.extend(chapter_reqs)
        provenance.append({"file": name, "source": source,
                           "sha256": hashlib.sha256(data).hexdigest(),
                           "requirements_found": len(chapter_reqs)})

    requirements.sort(key=lambda r: sort_key(r["id"]))
    ids = [r["id"] for r in requirements]
    dupes = sorted({i for i in ids if ids.count(i) > 1})

    out = {
        "generated_at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "ref": args.ref if not args.local_dir else None,
        "local_dir": args.local_dir,
        "provenance": provenance,
        "errors": errors,
        "duplicate_ids_in_publication": dupes,
        "requirement_count": len(requirements),
        "requirements": requirements,
    }
    Path(args.out).write_text(json.dumps(out, indent=2, ensure_ascii=False))
    print(f"Wrote {len(requirements)} requirements from "
          f"{len(provenance)} chapters -> {args.out}")
    if dupes:
        print(f"WARNING: duplicate IDs in publication: {dupes}")
    if errors:
        print(f"ERRORS: {json.dumps(errors, indent=2)}", file=sys.stderr)
        sys.exit(2)


if __name__ == "__main__":
    main()
