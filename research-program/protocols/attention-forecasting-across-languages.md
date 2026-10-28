# Attention forecasting across languages

**State: protocol only. No result or novelty claim yet.**

## Decision

Can English-language attention improve forecasts for related Spanish and Japanese pages without leaking future popularity?

## Target data

- [Wikimedia pageview APIs](https://doc.wikimedia.org/generated-data-platform/aqs/analytics-api/) — targeted; exact export and rights must be verified.

## Study design

Cross-series lag models and change detection.

Language and topic holdouts; page-renaming lineage; no inferred speaker fluency.

## Contribution to test

Measure cross-language transfer and asymmetric lag structure. This is a proposed contribution, not a verified gap in the literature. Prior work must be reviewed before any novelty claim.

## Evidence to retain

- Exact source snapshot, request, retrieval time, observation window, definitions, units and redistribution terms.
- Prespecified splits, baseline, search space, tuning budget, seed and decision metric.
- All candidate results, including failures; final holdout used only after model selection.
- Independent headline recomputation, leakage checks and reviewed figures with units and uncertainty.
- Reproduction command and environment; private LaTeX manuscript written from measured results.

## Skills

NLP, forecasting, international data. The repository must demonstrate these through executed work before they become portfolio claims.
