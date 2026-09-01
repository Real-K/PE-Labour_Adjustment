# -*- coding: utf-8 -*-
"""DiD event-study figures from I75.json: (1) level + state-interacted coefficients, (2) by-state-group paths."""
import json, os
import numpy as np
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)
ART = os.environ.get("P014_ARTIFACTS", os.path.join(ROOT, "artifacts"))
FIG = os.environ.get("P014_FIGDIR", os.path.join(ROOT, "figures"))
E = json.load(open(os.path.join(ART, "I75.json"), encoding="utf-8"))["estimates"]
QS = [-4, -3, -2, -1, 1, 2, 3, 4]
def series(P):
    b, lo, hi = [], [], []
    for qq in QS:
        if qq == -1: b.append(0.0); lo.append(0.0); hi.append(0.0)
        else:
            d = P[f"q{qq}"]; b.append(d["coef"]); lo.append(d["ci"][0]); hi.append(d["ci"][1])
    return np.array(b), np.array(lo), np.array(hi)

fig, ax = plt.subplots(1, 2, figsize=(11.2, 4.1))
for a, key, ttl, col in ((ax[0], "panelB_es_level", "(a) Treated × quarter (level)", "#1b4a8a"),
                         (ax[1], "panelC_es_state", "(b) Treated × quarter × state", "#8a1b2e")):
    b, lo, hi = series(E[key])
    a.axhline(0, color="0.45", lw=.8); a.axvline(-0.5, color="0.45", lw=.9, ls=":")
    a.errorbar(QS, b, yerr=[b - lo, hi - b], fmt="o", ms=4.5, lw=1, capsize=2.5, color=col, ecolor="0.6")
    a.set_title(ttl, fontsize=10.5, loc="left"); a.set_xlabel("Quarter relative to deal (reference q−1)")
    a.spines[["top", "right"]].set_visible(False)
ax[0].set_ylabel("Monthly hiring rate, treated − control", fontsize=9)
w1, w2 = E["panelH_magnitudes"]["pretrend_wald_level"], E["panelH_magnitudes"]["pretrend_wald_state"]
fig.suptitle("Stacked matched difference-in-differences: event-study coefficients", fontsize=10.6, y=1.005, x=.008, ha="left")
fig.text(.008, -0.06, f"Notes. Unit (event×firm) and calendar-month fixed effects; 95% intervals cluster on events (n = {E['design']['n_events']}). "
         f"Joint pre-quarter Wald tests: level χ²(3) = {w1['chi2_3']} (p = {w1['p']:.3f}); state χ²(3) = {w2['chi2_3']} (p = {w2['p']:.3f}). "
         "The state variable is the target's continuous pre-deal state, centred at the event mean.", fontsize=7.6, color="0.4", ha="left")
fig.tight_layout()
for e in ("png", "pdf"): fig.savefig(os.path.join(FIG, f"figure_did_eventstudy.{e}"), dpi=200, bbox_inches="tight")
print("saved figure_did_eventstudy")

fig, a = plt.subplots(figsize=(7.6, 4.2))
a.axhline(0, color="0.45", lw=.8); a.axvline(-0.5, color="0.45", lw=.9, ls=":")
for key, lab, col, off in (("T3_low_hiring", "Low pre-deal hiring (top state tercile)", "#8a1b2e", 0.07),
                           ("T1_high_hiring", "High pre-deal hiring (bottom tercile)", "#1b4a8a", -0.07)):
    P = E["panelI_es_bystate"][key]
    b, lo, hi = series(P)
    a.errorbar(np.array(QS) + off, b, yerr=[b - lo, hi - b], fmt="o", ms=4.5, lw=1, capsize=2.5,
               color=col, ecolor="0.65", label=f"{lab} (n = {P['n_events']})")
a.legend(frameon=False, fontsize=8.5, loc="upper left")
a.set_xlabel("Quarter relative to deal (reference q−1)"); a.set_ylabel("Monthly hiring rate, treated − control")
a.spines[["top", "right"]].set_visible(False)
a.set_title("Stacked event-study by pre-deal hiring state group", fontsize=10.6, loc="left")
fig.text(.01, -0.05, "Notes. Separate stacked event-study regressions within state-tercile subsamples; unit and calendar-month fixed effects; event-clustered 95% intervals.",
         fontsize=7.6, color="0.4", ha="left")
fig.tight_layout()
for e in ("png", "pdf"): fig.savefig(os.path.join(FIG, f"figure_did_bystate.{e}"), dpi=200, bbox_inches="tight")
print("saved figure_did_bystate")
