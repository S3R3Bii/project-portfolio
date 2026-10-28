# SOFR publication-day anomaly triage

**State: protocol only. No result or novelty claim yet.**

## Decision

Can an alert distinguish a large but routine calendar effect from a persistent change in funding conditions?

## Target data

- [New York Fed markets data](https://www.newyorkfed.org/markets/reference-rates/sofr) — targeted; exact export and rights must be verified.

## Study design

Robust seasonal decomposition and change detection.

Forward-only thresholds; calendar ablations; fixed false-alert budget.

## Contribution to test

Evaluate alert burden and delay, not hindsight labels of financial crises. This is a proposed contribution, not a verified gap in the literature. Prior work must be reviewed before any novelty claim.

## Evidence to retain

- Exact source snapshot, request, retrieval time, observation window, definitions, units and redistribution terms.
- Prespecified splits, baseline, search space, tuning budget, seed and decision metric.
- All candidate results, including failures; final holdout used only after model selection.
- Independent headline recomputation, leakage checks and reviewed figures with units and uncertainty.
- Reproduction command and environment; private LaTeX manuscript written from measured results.

## Skills

time series, anomaly detection, model monitoring. The repository must demonstrate these through executed work before they become portfolio claims.
