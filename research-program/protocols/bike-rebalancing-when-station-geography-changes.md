# Bike rebalancing when station geography changes

## Execution update — 29 October 2026

A scoped study is executed and released at https://github.com/S3R3Bii/station-geography-transfer. Across 12 held coordinate groups and 2,208 station-days, selected-model MAE is 11.621 departures/day versus 21.047 for the pooled baseline, a 44.8% reduction. Two groups have higher error. Temporal settings also differ, so this model-bundle comparison does not isolate geography. All 16 fixed coordinate-displacement cases and all group failures are retained. Read its fixed executable protocol, complete exclusions and validation. The broader proposal below is retained as historical design context; it is not the release specification. Independent program manuscripts are public after checks; separate formal-publication projects remain private.

**Historical proposal, superseded by the scoped release above.**

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
