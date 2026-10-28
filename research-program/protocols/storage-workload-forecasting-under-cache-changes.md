# Storage workload forecasting under cache changes

**State: protocol only. No result or novelty claim yet.**

## Decision

When does a predictor trained on one cache regime fail after an operational configuration change?

## Target data

- [USENIX FAST storage traces](https://www.usenix.org/conference/fast) — targeted; exact export and rights must be verified.

## Study design

Sequence forecasts and workload change detection.

Dataset and redistribution permission gate; chronological replay; regime-held-out evaluation.

## Contribution to test

Treat deployment shift as the experiment rather than fitting another generic trace predictor. This is a proposed contribution, not a verified gap in the literature. Prior work must be reviewed before any novelty claim.

## Evidence to retain

- Exact source snapshot, request, retrieval time, observation window, definitions, units and redistribution terms.
- Prespecified splits, baseline, search space, tuning budget, seed and decision metric.
- All candidate results, including failures; final holdout used only after model selection.
- Independent headline recomputation, leakage checks and reviewed figures with units and uncertainty.
- Reproduction command and environment; private LaTeX manuscript written from measured results.

## Skills

systems ML, performance analysis, time series. The repository must demonstrate these through executed work before they become portfolio claims.
