# Complaint capacity under delayed information

**State: protocol only. No result or novelty claim yet.**

## Decision

How much monthly review capacity should a product team reserve when a missed surge is more costly than unused capacity?

## Target data

- [Consumer Financial Protection Bureau](https://www.consumerfinance.gov/data-research/consumer-complaints/) — targeted; exact export and rights must be verified.

## Study design

Lag-aware pooled forecasting and quantile capacity policies.

Rolling temporal folds; untouched 24-month test; product and lag sensitivity; loss-ratio sweep.

## Contribution to test

Evaluate capacity regret under reporting delay instead of another complaint sentiment classifier. This is a proposed contribution, not a verified gap in the literature. Prior work must be reviewed before any novelty claim.

## Evidence to retain

- Exact source snapshot, request, retrieval time, observation window, definitions, units and redistribution terms.
- Prespecified splits, baseline, search space, tuning budget, seed and decision metric.
- All candidate results, including failures; final holdout used only after model selection.
- Independent headline recomputation, leakage checks and reviewed figures with units and uncertainty.
- Reproduction command and environment; private LaTeX manuscript written from measured results.

## Skills

SQL, Python, forecasting, decision analysis, data quality. The repository must demonstrate these through executed work before they become portfolio claims.
