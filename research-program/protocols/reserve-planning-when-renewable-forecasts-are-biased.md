# Reserve planning when renewable forecasts are biased

## Execution update — 30 October 2026

A scoped study is executed and released at https://github.com/S3R3Bii/wind-shortfall-buffer. On 26,260 held hours per region, selected Q75 lowers primary hypothetical proxy cost from 117.120 to 87.820 in Flanders and 103.987 to 75.474 in Wallonia. Coverage is 79.954% and 75.091%. Q80 is slightly cheaper in Wallonia; at penalty ratio two, zero beats the selected buffer in both regions. Mean bias correction worsens held point MAE in both. No actual reliability or financial benefit is measured. Read its fixed executable protocol, complete exclusions and validation. The broader proposal below is retained as historical design context; it is not the release specification. Independent program manuscripts are public after checks; separate formal-publication projects remain private.

**Historical proposal, superseded by the scoped release above.**

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
