# Private Equity and Labour Adjustment across Pre-Deal Hiring States

Analysis code, aggregate result artifacts, and reproducible exhibits for the manuscript (main paper: 5 tables + 2 figures; online appendix: 28 tables). Everything runs from the aggregate artifacts in `artifacts/` — no licensed microdata is included or required (see `DATA_ACCESS.md`).

## Start here — the notebooks render on GitHub

| Notebook | Contents |
|---|---|
| [`01_paper_exhibits.ipynb`](01_paper_exhibits.ipynb) | Figures 1–2 rebuilt from artifacts; main-text Tables 1–5 displayed and verified cell-by-cell |
| [`02_appendix_exhibits.ipynb`](02_appendix_exhibits.ipynb) | Online-appendix Tables A1–H2 displayed and verified |
| [`03_traceability.ipynb`](03_traceability.ipynb) | Every decimal token in the manuscript (1,196) traced to the artifacts; the 370-row claims ledger resolved with 0 mismatches |

**How the check works.** Each exhibit is shown exactly as printed in the manuscript (`manuscript/`). The verification confirms that every decimal token in every table — estimates, confidence limits, reference moments, empirical probabilities — exists in the generating artifact JSONs at the displayed precision; the notebooks fail loudly otherwise. The two figures are regenerated from `I70.json` (which stores the 286 event-level pairs and the actual 2,000 pseudo-sample gradients) and `I68.json`.

## Layout

```
manuscript/   the current manuscript (Markdown)
artifacts/    70 aggregate result files + CLAIMS_LEDGER.csv (one row per headline claim → artifact path)
figures/      figure1_state_gradient, figure2_quarterly (png + pdf)
code/         exhibits_lib.py (parse + verify) · build_figure1/2.py · make_notebooks.py
pipeline/     the full analysis pipeline (i01…i74 + shared loaders); requires licensed inputs — see DATA_ACCESS.md
```

## Rebuilding

```bash
python3 code/build_figure1.py && python3 code/build_figure2.py   # figures from artifacts
python3 code/make_notebooks.py                                    # re-execute and store notebook outputs
```
Python 3.11+, numpy, matplotlib.

## Inference conventions used throughout

Estimates and intervals are reported to four decimals. Empirical two-sided probabilities are centred finite-simulation tail shares, $(1+\#\{b:|g_b-\bar g|\ge|g^{obs}-\bar g|\})/(B+1)$ with $B=2{,}000$ draws. Each specification is compared with its own untreated reference distribution.

## Licence
MIT. Citation details to be added on publication.
