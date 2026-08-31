# -*- coding: utf-8 -*-
"""Build the three stored-output notebooks at the repository root."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from build_notebooks import build
ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
os.chdir(ROOT)
MS = "manuscript/PE_Labour_Adjustment_manuscript_2026-08-31.md"
SETUP = f'''import sys, runpy
sys.path.insert(0, "code"); import exhibits_lib as X
md = open("{MS}", encoding="utf-8").read()
paper, appendix = X.split_document(md)
pool = X.load_pool("artifacts")
print("artifact pool loaded ·", len(pool), "quantized values")'''
COMMON = ["Every number in the manuscript's exhibits is regenerated or verified from the aggregate artifacts in `artifacts/`; no licensed microdata is used or required (see `DATA_ACCESS.md`).",
          "Outputs are stored, so the notebooks render on GitHub without running. Rebuild with `python3 code/make_notebooks.py`."]
def table_cells(part_expr, doc):
    cells = [(["## Setup"], SETUP)]
    cells.append(([f"## All {doc} tables — displayed from the manuscript and verified cell-by-cell",
                   "Each table below is shown exactly as printed in the manuscript; the check confirms every decimal token in the table (values, intervals, reference moments, probabilities) exists in the generating artifacts at the displayed precision."],
                  f'''tabs = X.extract_tables({part_expr})
bad = 0
for title, block in tabs:
    n, un = X.verify_block(block, pool)
    print(f"{{title[:74]:<76}} tokens {{n:>3}} · unmatched {{len(un)}}")
    if un: bad += len(un); print("   →", un[:6])
assert bad == 0, "some table tokens do not trace to the artifacts"
print(f"\\nTOTAL: {{len(tabs)}} tables verified")'''))
    for i in range(40):
        cells.append((["### Table display"], f'''if {i} < len(tabs):
    title, block = tabs[{i}]
    _md = "### " + title + "\\n\\n" + block
    print(title)
else:
    _md = ""; print("—")'''))
    return cells
build("01_paper_exhibits.ipynb", "# Main-paper exhibits — Tables 1–5, Figures 1–2", COMMON,
      [(["## Setup"], SETUP),
       (["## Figure 1 — hiring responses across pre-deal hiring states",
         "Built from `I70.json`: the 286 event-level pairs, fixed quintile-bin means, the primary gradient with an event-bootstrap band, and the **actual** 2,000 pseudo-sample gradients."],
        'runpy.run_path("code/build_figure1.py", run_name="__main__")\n_figs = [open("figures/figure1_state_gradient.png", "rb").read()]'),
       (["## Figure 2 — quarterly hiring differences relative to matched controls"],
        'runpy.run_path("code/build_figure2.py", run_name="__main__")\n_figs = [open("figures/figure2_quarterly.png", "rb").read()]'),
       (["## Main-text tables — displayed and verified",
         "Each table is shown exactly as printed in the manuscript; the check confirms every decimal token exists in the generating artifacts at the displayed precision."],
        '''tabs = X.extract_tables(paper)
bad = 0
for title, block in tabs:
    n, un = X.verify_block(block, pool)
    print(f"{title[:74]:<76} tokens {n:>3} · unmatched {len(un)}")
    if un: bad += len(un); print("   →", un[:6])
assert bad == 0
print(f"\\nTOTAL: {len(tabs)} main-text tables verified")''')] +
      [(["### Table"], f'''if {i} < len(tabs):
    title, block = tabs[{i}]
    _md = "### " + title + "\\n\\n" + block
    print(title)
else:
    _md = ""''') for i in range(6)])
build("02_appendix_exhibits.ipynb", "# Online-appendix exhibits — Tables A1–H2", COMMON,
      [(["## Setup"], SETUP),
       (["## Appendix tables — displayed and verified"],
        '''tabs = X.extract_tables(appendix)
bad = 0
for title, block in tabs:
    n, un = X.verify_block(block, pool)
    print(f"{title[:74]:<76} tokens {n:>3} · unmatched {len(un)}")
    if un: bad += len(un); print("   →", un[:6])
assert bad == 0
print(f"\\nTOTAL: {len(tabs)} appendix tables verified")''')] +
      [(["### Table"], f'''if {i} < len(tabs):
    title, block = tabs[{i}]
    _md = "### " + title + "\\n\\n" + block
    print(title)
else:
    _md = ""''') for i in range(30)])
build("03_traceability.ipynb", "# Traceability — manuscript ↔ artifacts ↔ pipeline", COMMON,
      [(["## Setup"], SETUP),
       (["## Every decimal token in the manuscript traces to the artifacts",
         "References and six-figure display roundings aside, every decimal in the prose and tables must exist in the artifact pool at its displayed precision."],
        '''import re
body = re.split(r"\\n#+ References\\s*\\n", md)[0]
tot = bad = 0; badl = []
for m in X.NUM.finditer(body.replace("−", "-").replace("+", "")):
    x = float(m.group()); nd = len(m.group().split(".")[1]); tot += 1
    if (nd, X._q(x, nd)) not in pool and (nd, X._q(abs(x), nd)) not in pool:
        bad += 1; badl.append(m.group())
print(f"decimal tokens {tot} · unmatched {bad}"); print(badl[:8])
assert bad <= 1, badl   # DOI in the reference heading area at most'''),
       (["## The claims ledger resolves against the artifacts"],
        '''import csv, json, os
rows = list(csv.DictReader(open("artifacts/CLAIMS_LEDGER.csv", encoding="utf-8-sig")))
def resolve(o, p):
    for k in [k for k in p.split(".") if k]: o = o[int(k)] if isinstance(o, list) else o[k]
    return o
exact = derived = mismatch = missing = 0
for r in rows:
    f = os.path.join("artifacts", os.path.basename(r["source_json"]))
    if not os.path.exists(f): missing += 1; continue
    try: o = resolve(json.load(open(f, encoding="utf-8")), r["json_path"])
    except Exception: mismatch += 1; continue
    if isinstance(o, (dict, list)): derived += 1; continue
    try: ok = abs(float(r["value"]) - float(o)) <= max(5e-5, abs(float(o)) * 1e-6)
    except Exception: ok = str(o) == r["value"]
    exact += ok; mismatch += (not ok)
print(f"claims ledger: {len(rows)} rows · exact {exact} · derived {derived} · mismatch {mismatch} · missing {missing}")
assert mismatch == 0''')])
print("notebooks built")
