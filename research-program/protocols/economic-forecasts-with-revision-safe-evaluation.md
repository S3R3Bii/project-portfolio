# Economic forecasts with revision-safe evaluation

**State: protocol only. No result or novelty claim yet.**

## Decision

Which model wins change when first-release economic data replace the latest revised series?

## Target data

- [Federal Reserve economic data](https://fred.stlouisfed.org/) — targeted; exact export and rights must be verified.

## Study design

Vintage-aware forecasting and ranking comparison.

ALFRED vintage availability gate; identical information sets; rolling origins.

## Contribution to test

Measure the price of hindsight explicitly instead of publishing one backtest score. This is a proposed contribution, not a verified gap in the literature. Prior work must be reviewed before any novelty claim.

## Evidence to retain

- Exact source snapshot, request, retrieval time, observation window, definitions, units and redistribution terms.
- Prespecified splits, baseline, search space, tuning budget, seed and decision metric.
- All candidate results, including failures; final holdout used only after model selection.
- Independent headline recomputation, leakage checks and reviewed figures with units and uncertainty.
- Reproduction command and environment; private LaTeX manuscript written from measured results.

## Skills

quant research, time series, data provenance. The repository must demonstrate these through executed work before they become portfolio claims.
