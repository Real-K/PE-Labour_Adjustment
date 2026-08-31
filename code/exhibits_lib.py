# -*- coding: utf-8 -*-
"""Helpers: parse the manuscript's exhibits and verify every numeric token against the artifacts."""
import json, os, re, math, csv
from decimal import Decimal, ROUND_HALF_UP

def _q(x, nd): return Decimal(repr(x)).quantize(Decimal(1).scaleb(-nd), ROUND_HALF_UP)

def load_pool(art_dir):
    vals = []
    def walk(o):
        if isinstance(o, dict): [walk(v) for v in o.values()]
        elif isinstance(o, list): [walk(v) for v in o]
        elif isinstance(o, (int, float)) and not isinstance(o, bool) and math.isfinite(float(o)): vals.append(float(o))
    for f in os.listdir(art_dir):
        if f.endswith(".json"): walk(json.load(open(os.path.join(art_dir, f), encoding="utf-8")))
    for r in csv.DictReader(open(os.path.join(art_dir, "CLAIMS_LEDGER.csv"), encoding="utf-8-sig")):
        for v in [r["value"], r["n"]] + re.findall(r"-?\d+\.?\d*", r["ci95"] or ""):
            try: vals.append(float(v))
            except ValueError: pass
    pool = set()
    for x in vals:
        for nd in range(1, 7):
            for v in (x, abs(x), x * 100, abs(x) * 100): pool.add((nd, _q(v, nd)))
    return pool

def split_document(md):
    i = md.find("# Online Appendix")
    return md[:i], md[i:]

def extract_tables(md):
    out, cur, buf = [], None, []
    for ln in md.split("\n"):
        if ln.startswith("### Table"):
            if cur: out.append((cur, "\n".join(buf).strip()))
            cur, buf = ln.replace("### ", ""), []
        elif ln.startswith(("### ", "## ", "# ")) and cur:
            out.append((cur, "\n".join(buf).strip())); cur, buf = None, []
        elif cur is not None:
            buf.append(ln)
    if cur: out.append((cur, "\n".join(buf).strip()))
    return out

NUM = re.compile(r"[-−+]?\d+\.\d+")

def verify_block(block, pool):
    unmatched, tot = [], 0
    for m in NUM.finditer(block.replace("−", "-").replace("+", "")):
        x = float(m.group()); nd = len(m.group().split(".")[1]); tot += 1
        if (nd, _q(x, nd)) not in pool and (nd, _q(abs(x), nd)) not in pool:
            unmatched.append(m.group())
    return tot, unmatched
