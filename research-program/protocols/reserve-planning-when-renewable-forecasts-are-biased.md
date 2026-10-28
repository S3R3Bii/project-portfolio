# Reserve planning when renewable forecasts are biased

**State: protocol only. No result or novelty claim yet.**

## Decision

When does correcting persistent regional forecast bias reduce reserve shortfalls more than optimizing average error?

## Target data

- [EIA balancing authority operations](https://www.eia.gov/electricity/930-content/about.html) — targeted; exact export and rights must be verified.

## Study design

Quantile correction and asymmetric reserve policies.

Season-blocked folds; authority holdout; capacity-ratio sensitivity.

## Contribution to test

Evaluate the decision loss associated with forecast bias rather than reporting RMSE alone. This is a proposed contribution, not a verified gap in the literature. Prior work must be reviewed before any novelty claim.

## Evidence to retain

- Exact source snapshot, request, retrieval time, observation window, definitions, units and redistribution terms.
- Prespecified splits, baseline, search space, tuning budget, seed and decision metric.
- All candidate results, including failures; final holdout used only after model selection.
- Independent headline recomputation, leakage checks and reviewed figures with units and uncertainty.
- Reproduction command and environment; private LaTeX manuscript written from measured results.

## Skills

forecasting, optimization, uncertainty. The repository must demonstrate these through executed work before they become portfolio claims.
