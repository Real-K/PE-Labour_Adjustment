# -*- coding: utf-8 -*-
"""DID_RESULTS.md — every statistic from I75.json organised as candidate table panels for the PI."""
import json, os
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)
E = json.load(open(os.path.join(ROOT, "artifacts", "I75.json"), encoding="utf-8"))["estimates"]
def r(p): return f"{p['coef']:+.4f} | [{p['ci'][0]:.4f}, {p['ci'][1]:.4f}] | {p['t']:.2f}".replace("-", "−")
L = ["# Stacked matched panel DiD — full statistics menu (I75)", "",
     f"Design: {E['design']['n_events']} state-balanced matched sets stacked into an event×firm panel "
     f"({E['design']['n_units']:,} units, {E['design']['n_rows']:,} firm-months, {E['design']['n_cal_months']} calendar months). "
     "Outcome: monthly worker-entry rate (entries / insured employment), untransformed. Fixed effects: unit and calendar month. "
     f"SEs cluster on events. The state S is the target's continuous pre-deal state assigned to its matched set, centred at the event mean ({E['design']['S_centering']}), "
     "so the Treated×Post coefficient is the effect at the mean state. Controls are never-treated, so the stacked design involves no treated-vs-treated comparisons.", "",
     "## Panel A — headline DiD", "", "| Coefficient | Estimate | 95% CI | t |", "|---|---:|---:|---:|",
     f"| Treated × post (level model) | {r(E['panelA_did']['treat_post'])} |",
     f"| Treated × post (interaction model, at mean S) | {r(E['panelA_did']['treat_post_in_S_model'])} |",
     f"| Treated × post × S | {r(E['panelA_did']['treat_post_S'])} |", "",
     "## Panel B — outcome variants (β1 at mean S / β2)", "",
     "| Outcome | β1 | t | β2 | t | Rows |", "|---|---:|---:|---:|---:|---:|"]
LAB = {"rate": "Monthly hiring rate", "log1p_rate": "log(1 + rate)", "any_entry": "Any-entry indicator",
       "sep_rate": "Separation rate", "churn_rate": "Churn rate"}
for k, lab in LAB.items():
    d = E["panelD_outcomes"][k]
    L.append(f"| {lab} | {d['beta1']['coef']:+.4f} | {d['beta1']['t']:.2f} | {d['beta2']['coef']:+.4f} | {d['beta2']['t']:.2f} | {d['n_rows']:,} |".replace("-", "−"))
pe = E["panelE_state_forms"]
L += ["", "## Panel C — state parametrisations (β2 equivalents)", "",
      "| Form | Estimate | 95% CI | t |", "|---|---:|---:|---:|",
      f"| Continuous S | {r(pe['continuous'])} |",
      f"| Per SD of S ({pe['S_sd']}) | {r(pe['per_sd'])} |",
      f"| Per IQR of S ({pe['S_iqr']}) | {r(pe['per_iqr'])} |",
      f"| Top tercile vs rest | {r(pe['tercile_T3_vs_rest'])} |",
      f"| Median split | {r(pe['median_split'])} |", "",
      "*Discrete splits are imprecise at the monthly scale — one reason the paper's primary design uses the continuous state.*", ""]
pf = E["panelF_design_compare"]
L += ["## Panel D — matching-design comparison", "",
      "| Design | β2 | 95% CI | t | Events |", "|---|---:|---:|---:|---:|",
      f"| State-balanced (primary sets) | {r(pf['balanced_286']['beta2'])} | 286 |",
      f"| Conventional (state not in cell) | {r(pf['conventional_301']['beta2'])} | {pf['conventional_301']['n_events']} |", ""]
pg = E["panelG_variants"]
L += ["## Panel E — specification variants (β2)", "",
      "| Variant | Estimate | 95% CI | t |", "|---|---:|---:|---:|",
      f"| Unit + calendar-month FE (base) | {r(E['panelA_did']['treat_post_S'])} |",
      f"| Unit + event-time FE | {r(pg['fe_unit_eventtime'])} |",
      f"| Cluster on units instead of events | {r(pg['cluster_unit'])} |",
      f"| Event-equal weighting | {r(pg['event_equal_weight'])} |", ""]
ph = E["panelH_magnitudes"]
L += ["## Panel F — magnitudes and joint pre-trend tests", "",
      f"- Pre-period treated mean monthly rate: {ph['pre_mean_treated_rate']}",
      f"- Annualised β1 (12×): {ph['annualised_beta1']} ({ph['beta1_pct_of_pre_mean']}% of the pre-period monthly mean)",
      f"- β2 × IQR, annualised: {ph['beta2_iqr_annualised']} ({ph['beta2_iqr_pct_of_pre_mean']}% per month relative to the pre-mean)",
      f"- Joint pre-quarter Wald (level): χ²(3) = {ph['pretrend_wald_level']['chi2_3']}, p = {ph['pretrend_wald_level']['p']}",
      f"- Joint pre-quarter Wald (state interaction): χ²(3) = {ph['pretrend_wald_state']['chi2_3']}, p = {ph['pretrend_wald_state']['p']}", "",
      "## Panel G — event-study coefficients (reference q−1)", "",
      "| Quarter | Treated×q | t | Treated×q×S | t | T3 group | T1 group |", "|---|---:|---:|---:|---:|---:|---:|"]
for qq in (-4, -3, -2, 1, 2, 3, 4):
    b1 = E["panelB_es_level"][f"q{qq}"]; b2 = E["panelC_es_state"][f"q{qq}"]
    t3 = E["panelI_es_bystate"]["T3_low_hiring"][f"q{qq}"]; t1 = E["panelI_es_bystate"]["T1_high_hiring"][f"q{qq}"]
    L.append(f"| q{qq} | {b1['coef']:+.4f} | {b1['t']:.2f} | {b2['coef']:+.4f} | {b2['t']:.2f} | {t3['coef']:+.4f} | {t1['coef']:+.4f} |".replace("-", "−"))
L += ["", "Figures: `figures/figure_did_eventstudy.png` (level + state interaction), `figures/figure_did_bystate.png` (T3 vs T1 paths).", ""]
open(os.path.join(ROOT, "did", "DID_RESULTS.md"), "w", encoding="utf-8").write("\n".join(L))
print("DID_RESULTS.md written")
