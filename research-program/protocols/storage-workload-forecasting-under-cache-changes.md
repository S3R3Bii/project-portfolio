# Storage workload forecasting under cache changes

## Execution update — 30 October 2026

A scoped study is executed and released at https://github.com/S3R3Bii/cache-change-forecast-audit. The previous-block baseline has lower MAE in all nine final volume/scenario groups, including unchanged controls. Across changed groups, macro MAE is 0.054979 versus 0.070884 for the frozen linear model; development also favors the baseline. Combined changed MSE instead favors the linear model, 0.011782 versus 0.012023. The recommendation is specific to the predeclared MAE objective; cache changes alone do not explain the linear model weakness. Read its fixed executable protocol, complete exclusions and validation. The broader proposal below is retained as historical design context; it is not the release specification. Independent program manuscripts are public after checks; separate formal-publication projects remain private.

**Historical proposal, superseded by the scoped release above.**

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
