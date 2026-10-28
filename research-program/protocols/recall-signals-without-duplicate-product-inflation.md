# Recall signals without duplicate product inflation

**State: protocol only. No result or novelty claim yet.**

## Decision

How much do duplicate and amended enforcement notices distort a product-category alert stream?

## Target data

- [openFDA APIs](https://open.fda.gov/apis/) — targeted; exact export and rights must be verified.

## Study design

Event entity resolution and sequential anomaly detection.

Human-audited public-label sample; amendment lineage; future-time alert evaluation.

## Contribution to test

Separate notification churn from distinct recall events before detecting anomalies. This is a proposed contribution, not a verified gap in the literature. Prior work must be reviewed before any novelty claim.

## Evidence to retain

- Exact source snapshot, request, retrieval time, observation window, definitions, units and redistribution terms.
- Prespecified splits, baseline, search space, tuning budget, seed and decision metric.
- All candidate results, including failures; final holdout used only after model selection.
- Independent headline recomputation, leakage checks and reviewed figures with units and uncertainty.
- Reproduction command and environment; private LaTeX manuscript written from measured results.

## Skills

NLP, SQL, record linkage, monitoring. The repository must demonstrate these through executed work before they become portfolio claims.
