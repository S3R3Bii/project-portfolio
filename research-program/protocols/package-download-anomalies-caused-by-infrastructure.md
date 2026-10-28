# Package download anomalies caused by infrastructure

**State: protocol only. No result or novelty claim yet.**

## Decision

Which package-demand spikes vanish after removing known automation and mirror effects?

## Target data

- [PyPI BigQuery download statistics](https://docs.pypi.org/api/bigquery/) — targeted; exact export and rights must be verified.

## Study design

Robust aggregation and anomaly triage.

Document bot-filter limits; version-level and time holdouts; free-query cost guard.

## Contribution to test

Measure data-pipeline artifacts before inferring user adoption. This is a proposed contribution, not a verified gap in the literature. Prior work must be reviewed before any novelty claim.

## Evidence to retain

- Exact source snapshot, request, retrieval time, observation window, definitions, units and redistribution terms.
- Prespecified splits, baseline, search space, tuning budget, seed and decision metric.
- All candidate results, including failures; final holdout used only after model selection.
- Independent headline recomputation, leakage checks and reviewed figures with units and uncertainty.
- Reproduction command and environment; private LaTeX manuscript written from measured results.

## Skills

SQL, data quality, anomaly detection. The repository must demonstrate these through executed work before they become portfolio claims.
