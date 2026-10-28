# Commercial building energy residuals

**State: protocol only. No result or novelty claim yet.**

## Decision

Can peer-adjusted energy-use residuals identify buildings worth an engineering review without ranking them on size alone?

## Target data

- [NYC energy and water benchmarking](https://www.nyc.gov/site/buildings/codes/benchmarking.page) — targeted; exact export and rights must be verified.
- [NOAA integrated surface observations](https://www.ncei.noaa.gov/products/land-based-station/integrated-surface-database) — targeted; exact export and rights must be verified.

## Study design

Robust GAM and gradient-boosted residual benchmarks.

Building-held-out and future-year test; weather normalization; floor-area quality checks.

## Contribution to test

Use calibrated review bands and abstention for implausible records. This is a proposed contribution, not a verified gap in the literature. Prior work must be reviewed before any novelty claim.

## Evidence to retain

- Exact source snapshot, request, retrieval time, observation window, definitions, units and redistribution terms.
- Prespecified splits, baseline, search space, tuning budget, seed and decision metric.
- All candidate results, including failures; final holdout used only after model selection.
- Independent headline recomputation, leakage checks and reviewed figures with units and uncertainty.
- Reproduction command and environment; private LaTeX manuscript written from measured results.

## Skills

R, ML, regression diagnostics, business communication. The repository must demonstrate these through executed work before they become portfolio claims.
