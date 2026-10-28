# Electricity forecasts that respect release time

**State: protocol only. No result or novelty claim yet.**

## Decision

When does correcting the balancing authority demand forecast improve the next-day reserve estimate?

## Target data

- [EIA balancing authority operations](https://www.eia.gov/electricity/930-content/about.html) — targeted; exact export and rights must be verified.
- [NOAA integrated surface observations](https://www.ncei.noaa.gov/products/land-based-station/integrated-surface-database) — targeted; exact export and rights must be verified.

## Study design

Residual models and calibrated prediction intervals.

Strict forecast-vintage alignment; held-out seasons and authorities; coverage by load regime.

## Contribution to test

Separate weather hindsight from information actually available when reserves are scheduled. This is a proposed contribution, not a verified gap in the literature. Prior work must be reviewed before any novelty claim.

## Evidence to retain

- Exact source snapshot, request, retrieval time, observation window, definitions, units and redistribution terms.
- Prespecified splits, baseline, search space, tuning budget, seed and decision metric.
- All candidate results, including failures; final holdout used only after model selection.
- Independent headline recomputation, leakage checks and reviewed figures with units and uncertainty.
- Reproduction command and environment; private LaTeX manuscript written from measured results.

## Skills

time series, feature engineering, calibration, data engineering. The repository must demonstrate these through executed work before they become portfolio claims.
