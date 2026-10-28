# Bike rebalancing when station geography changes

**State: protocol only. No result or novelty claim yet.**

## Decision

Can a demand model transfer to new or relocated stations without overstating dock availability?

## Target data

- [Citi Bike system data](https://citibikenyc.com/system-data) — targeted; exact export and rights must be verified.

## Study design

Station embeddings versus spatial and seasonal baselines.

Leave-station-out and future-month splits; station-ID lineage; no trip-to-occupancy inference.

## Contribution to test

Measure cold-start transfer and the value of geographical pooling, not generic trip-count prediction. This is a proposed contribution, not a verified gap in the literature. Prior work must be reviewed before any novelty claim.

## Evidence to retain

- Exact source snapshot, request, retrieval time, observation window, definitions, units and redistribution terms.
- Prespecified splits, baseline, search space, tuning budget, seed and decision metric.
- All candidate results, including failures; final holdout used only after model selection.
- Independent headline recomputation, leakage checks and reviewed figures with units and uncertainty.
- Reproduction command and environment; private LaTeX manuscript written from measured results.

## Skills

geospatial ML, feature engineering, forecasting. The repository must demonstrate these through executed work before they become portfolio claims.
