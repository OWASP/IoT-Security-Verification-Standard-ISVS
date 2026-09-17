#!/usr/bin/env python3
"""Build a product-context-specific ISVS mapping from Appendix B.

Deterministic, stdlib-only. Filters the generalized Appendix B Table 1 by
product context without inventing new framework equivalence.

Usage:
  python3 build_custom_mapping.py --local-dir ../../../en --context context.json \
      --out-json custom_mapping.json --out-md custom_mapping.md
  python3 build_custom_mapping.py --local-dir ../../../en --context context.json \
      --out-json custom_mapping.json --out-md custom_mapping.md --isvs-ref master

Inputs:
  --local-dir   directory containing V*-*.md chapters and Appendix_B-Compliance_Mapping.md
  --context     product context JSON (see references/context_profiles.md)
  --isvs-ref    optional version label recorded in output (default: local-dir)
  --appendix-ref optional base-mapping label (default: local Appendix_B file)

Outputs:
  tailored JSON + markdown per references/output_format.md
"""
import argparse
import datetime
import hashlib
import json
import re
from pathlib import Path

REQ_RE = re.compile(r"\|\s*\*\*(\d+\.\d+\.\d+)\*\*\s*\|\s*(.*?)\s*\|\s*(.*?)\s*\|\s*(.*?)\s*\|\s*(.*?)\s*\|")
TABLE1_START = "## Table 1"

FRAMEWORK_VERSIONS = (
    "CRA (EU) 2024/2847; RED (EU) 2022/30 (EN 18031-1/-2/-3); "
    "NIST SP 800-213A; ETSI EN 303 645 v2.1.1"
)
FRAMEWORK_SOURCES = {
    "cra": "https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=OJ:L_202402847",
    "red": "https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32022R0030",
    "nist": "https://doi.org/10.6028/NIST.SP.800-213A",
    "etsi": "https://www.etsi.org/deliver/etsi_en/303600_303699/303645/02.01.01_60/en_303645v020101p.pdf",
    "isvs_repo": "https://github.com/OWASP/IoT-Security-Verification-Standard-ISVS",
}

REQUIRED_CONTEXT_KEYS = [
    "product_name", "device_type", "connectivity", "handles_personal_data",
    "payment_capable", "target_markets", "safety_critical", "update_mechanism",
]


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def parse_requirements(local_dir: Path):
    reqs = {}
    chapter_hashes = {}
    for chapter in sorted(local_dir.glob("V*.md")):
        chapter_hashes[chapter.name] = sha256_file(chapter)
        text = chapter.read_text(encoding="utf-8")
        for match in REQ_RE.finditer(text):
            rid, desc = match.group(1), match.group(2).strip()
            # skip appendix-style rows accidentally matched (chapters only have req tables)
            if rid not in reqs:
                reqs[rid] = {"id": rid, "text": re.sub(r"\s+", " ", desc).strip(),
                             "chapter": chapter.name}
    return reqs, chapter_hashes


def parse_table1(appendix_path: Path):
    text = appendix_path.read_text(encoding="utf-8")
    start = text.find(TABLE1_START)
    if start == -1:
        raise SystemExit("Table 1 section not found in appendix")
    table_text = text[start:]
    table2_pos = table_text.find("## Table 2")
    segment = table_text[:table2_pos] if table2_pos != -1 else table_text
    rows = {}
    for line in segment.splitlines():
        line = line.strip()
        if not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) < 8:
            continue
        # First cell holds ID plus summary, e.g. "**1.1.1** Verify ...".
        first_nostar = re.sub(r"\*", "", cells[0]).strip()
        m = re.match(r"(\d+\.\d+\.\d+)\b", first_nostar)
        if not m:
            continue
        rid = m.group(1)
        rows[rid] = {
            "cra1": cells[1], "cra2": cells[2], "redd": cells[3],
            "rede": cells[4], "redf": cells[5], "nist": cells[6], "etsi": cells[7],
        }
    return rows


def decide_applicability(rid, desc, ctx):
    text = desc.lower()
    reasons = []
    notes = []
    prompts = []
    verdict = "in_scope"
    confidence = "High"

    personal_keys = ["personal data", "pii", "privacy", "erasure", "deletion"]
    payment_keys = ["payment", "fraud", "monetary"]
    update_keys = ["update", "patch", "sbom", "upgrade"]
    log_keys = ["log", "monitor", "audit", "telemetry"]
    radio_keys = ["bluetooth", "wi-fi", "wifi", "zigbee", "lorawan", "cellular", "radio", "nfc"]

    def is_unknown(v):
        return v is None

    # personal data
    if any(k in text for k in personal_keys):
        if ctx.get("handles_personal_data") is False:
            return "out_of_scope", "no personal data in context", "", "High", []
        if is_unknown(ctx.get("handles_personal_data")):
            verdict, confidence = "review", "Low"
            reasons.append("handles_personal_data unknown")
            prompts.append("confirm whether the product processes personal data")

    # payment
    if any(k in text for k in payment_keys):
        if ctx.get("payment_capable") is False:
            return "out_of_scope", "payment_capable is false in context", "", "High", []
        if is_unknown(ctx.get("payment_capable")):
            verdict, confidence = "review", "Low"
            reasons.append("payment_capable unknown")
            prompts.append("confirm whether the product can initiate monetary transfer")

    # update mechanism
    if any(k in text for k in update_keys):
        um = ctx.get("update_mechanism")
        if um == "none":
            verdict, confidence = "review", "Medium"
            reasons.append("update_mechanism is none; confirm manual or managed update path")
            prompts.append("confirm how security updates reach the device")
        elif is_unknown(um):
            verdict, confidence = "review", "Low"
            reasons.append("update_mechanism unknown")
            prompts.append("confirm the update path before scoping")

    # connectivity: radio-specific requirements with no radio
    conn = ctx.get("connectivity") or []
    if isinstance(conn, list) and len(conn) == 0 and any(k in text for k in radio_keys):
        verdict, confidence = "review", "Medium"
        reasons.append("no connectivity declared; confirm bearers")
        prompts.append("confirm radio bearers in use")

    # safety critical raises logging/update reviews to in_scope
    if ctx.get("safety_critical") is True and verdict == "review":
        if any(k in text for k in log_keys + update_keys):
            verdict, confidence = "in_scope", "Medium"
            reasons.append("safety_critical true keeps logging/update in scope")
            prompts = []

    # RED-f context note (never changes the preserved cell)
    redf_note = ""
    if ctx.get("payment_capable") is False:
        redf_note = "RED 3.3(f) preserved from Appendix B; not applicable by context"
    elif is_unknown(ctx.get("payment_capable")):
        redf_note = "RED 3.3(f) preserved from Appendix B; payment capability unconfirmed"

    if verdict == "in_scope" and not reasons:
        reasons.append("exercised by declared context")
    reason = "; ".join(reasons) if reasons else "exercised by declared context"
    return verdict, reason, redf_note, confidence, prompts


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--local-dir", required=True)
    ap.add_argument("--context", required=True)
    ap.add_argument("--out-json", required=True)
    ap.add_argument("--out-md", required=True)
    ap.add_argument("--isvs-ref", default=None)
    ap.add_argument("--appendix-ref", default=None)
    args = ap.parse_args()

    local_dir = Path(args.local_dir)
    ctx = json.loads(Path(args.context).read_text(encoding="utf-8"))
    for key in REQUIRED_CONTEXT_KEYS:
        if key not in ctx:
            raise SystemExit(f"context missing required key: {key}")

    reqs, chapter_hashes = parse_requirements(local_dir)
    appendix_path = local_dir / "Appendix_B-Compliance_Mapping.md"
    if not appendix_path.exists():
        raise SystemExit(f"appendix not found: {appendix_path}")
    table1 = parse_table1(appendix_path)
    appendix_hash = sha256_file(appendix_path)

    isvs_ref = args.isvs_ref or f"local-dir:{local_dir.resolve().name}"
    appendix_ref = args.appendix_ref or f"local:{appendix_path.name} sha256:{appendix_hash[:12]}"
    now = datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds")

    mappings = []
    for rid in sorted(reqs, key=lambda r: tuple(int(p) for p in r.split("."))):
        desc = reqs[rid]["text"]
        verdict, reason, redf_note, conf, prompts = decide_applicability(rid, desc, ctx)
        fw = table1.get(rid, {"cra1": "TBD", "cra2": "TBD", "redd": "TBD",
                              "rede": "TBD", "redf": "TBD", "nist": "TBD", "etsi": "TBD"})
        base_missing = rid not in table1
        context_note = redf_note
        if base_missing:
            context_note = ((context_note + "; ") if context_note else "") + \
                "no base alignment in Appendix B scope; TBD pending base update"
            if verdict == "in_scope":
                verdict, conf = "review", "Low"
                prompts = prompts + ["base mapping has no row for this requirement; confirm against Appendix B scope note"]
        mappings.append({
            "id": rid,
            "description": desc,
            "chapter": reqs[rid]["chapter"],
            "applicability": verdict,
            "reason": reason,
            "confidence": conf,
            "frameworks": fw,
            "context_note": context_note,
            "reviewer_prompt": "; ".join(prompts),
            "base_missing": base_missing,
        })

    counts = {
        "total": len(mappings),
        "in_scope": sum(1 for m in mappings if m["applicability"] == "in_scope"),
        "out_of_scope": sum(1 for m in mappings if m["applicability"] == "out_of_scope"),
        "review": sum(1 for m in mappings if m["applicability"] == "review"),
    }

    output = {
        "generated": now,
        "isvs_ref": isvs_ref,
        "base_mapping": appendix_ref,
        "framework_versions": FRAMEWORK_VERSIONS,
        "sources": FRAMEWORK_SOURCES,
        "context": ctx,
        "chapter_hashes": chapter_hashes,
        "appendix_sha256": appendix_hash,
        "counts": counts,
        "mappings": mappings,
    }
    Path(args.out_json).write_text(json.dumps(output, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    # markdown
    lines = []
    lines.append(f"# Custom ISVS Mapping — {ctx.get('product_name')}")
    lines.append("")
    lines.append("> **Informative only.** This tailored mapping is a scoping aid. It does not")
    lines.append("> constitute legal or conformity advice. Satisfying ISVS requirements does")
    lines.append("> not constitute compliance with any listed regulation, and compliance with a")
    lines.append("> framework cannot be claimed solely based on this mapping.")
    lines.append("")
    lines.append(f"- Generated: {now}")
    lines.append(f"- ISVS reference: {isvs_ref}")
    lines.append(f"- Base mapping: {appendix_ref}")
    lines.append(f"- Framework versions: {FRAMEWORK_VERSIONS}")
    lines.append(f"- Context: device_type={ctx.get('device_type')}, connectivity={ctx.get('connectivity')}, "
                 f"handles_personal_data={ctx.get('handles_personal_data')}, "
                 f"payment_capable={ctx.get('payment_capable')}, target_markets={ctx.get('target_markets')}, "
                 f"safety_critical={ctx.get('safety_critical')}, update_mechanism={ctx.get('update_mechanism')}")
    lines.append(f"- Method: isvs-custom-mapping-builder skill")
    lines.append("")
    lines.append("| ISVS Req | Applicability | Reason | CRA-I | CRA-II | RED-d | RED-e | RED-f | NIST 800-213A | ETSI 303 645 | Context note | Confidence |")
    lines.append("|----------|---------------|--------|-------|--------|-------|-------|-------|---------------|--------------|--------------|------------|")
    for m in mappings:
        fw = m["frameworks"]
        lines.append(f"| **{m['id']}** | {m['applicability']} | {m['reason']} | {fw['cra1']} | {fw['cra2']} | "
                     f"{fw['redd']} | {fw['rede']} | {fw['redf']} | {fw['nist']} | {fw['etsi']} | "
                     f"{m['context_note']} | {m['confidence']} |")
    lines.append("")
    lines.append("## Decision Log")
    lines.append("")
    lines.append(f"Rule-based scoping over {counts['total']} requirements: "
                 f"{counts['in_scope']} in_scope, {counts['out_of_scope']} out_of_scope, "
                 f"{counts['review']} review. Framework cells preserved verbatim from Appendix B Table 1. "
                 f"Sources: ISVS chapters {isvs_ref}; base {appendix_ref}; framework URLs in JSON sources.")
    lines.append("")
    lines.append("## Items Requiring Human Decision")
    lines.append("")
    needs = [m for m in mappings if m["applicability"] == "review" or m["base_missing"]]
    if not needs:
        lines.append("None. All requirements scoped with High or Medium confidence.")
    else:
        for m in needs[:50]:
            q = m["reviewer_prompt"] or "confirm product behavior against canonical requirement text"
            lines.append(f"1. **{m['id']}** — {q} (confidence {m['confidence']}).")
        if len(needs) > 50:
            lines.append(f"Plus {len(needs) - 50} further review items; see JSON for the full list.")
    lines.append("")
    lines.append("## Verification Runs")
    lines.append("")
    lines.append("| Step | Command | Result |")
    lines.append("|------|---------|--------|")
    lines.append(f"| Build | build_custom_mapping.py --local-dir ... | {counts['total']} requirements, "
                 f"{counts['in_scope']} in_scope, {counts['out_of_scope']} out_of_scope, {counts['review']} review |")
    lines.append("| Validate | validate_custom_mapping.py ... | run validator before submitting |")
    lines.append("")
    Path(args.out_md).write_text("\n".join(lines), encoding="utf-8")
    print(f"wrote {args.out_json} and {args.out_md}: {counts}")


if __name__ == "__main__":
    main()
