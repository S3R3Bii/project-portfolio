# Electricity forecasts that respect release time

## Execution update — 30 October 2026

A scoped study is executed and released at https://github.com/S3R3Bii/load-forecast-deadline-audit. Across 120 system hours, prior-day noon MAE is 857.6 MW versus 619.3 MW at same-day noon and 338.0 MW using end-of-day files. Both same-day selectors miss the prior-day deadline for all 120 hours; end-of-day files were published after 115 intervals ended. The smaller retrospective error does not establish a better scheduling policy. Same-day noon worsens MAE on 25 October:668.6 versus 591.3 MW. Read its fixed executable protocol, complete exclusions and validation. The broader proposal below is retained as historical design context; it is not the release specification. Independent program manuscripts are public after checks; separate formal-publication projects remain private.

**Historical proposal, superseded by the scoped release above.**

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
