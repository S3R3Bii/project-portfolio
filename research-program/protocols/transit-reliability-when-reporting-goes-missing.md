# Transit reliability when reporting goes missing

**State: protocol only. No result or novelty claim yet.**

## Decision

Which apparent service recoveries disappear once missing operator-months are treated as missing rather than zero?

## Target data

- [Federal Transit Administration National Transit Database](https://www.transit.dot.gov/ntd/ntd-data) — targeted; exact export and rights must be verified.

## Study design

Panel reconciliation and bounded missingness sensitivity.

Published agency-total reconciliation; reporting-break checks; withheld-month recovery experiment.

## Contribution to test

Make dashboard reliability the primary outcome rather than ranking operators on incomplete totals. This is a proposed contribution, not a verified gap in the literature. Prior work must be reviewed before any novelty claim.

## Evidence to retain

- Exact source snapshot, request, retrieval time, observation window, definitions, units and redistribution terms.
- Prespecified splits, baseline, search space, tuning budget, seed and decision metric.
- All candidate results, including failures; final holdout used only after model selection.
- Independent headline recomputation, leakage checks and reviewed figures with units and uncertainty.
- Reproduction command and environment; private LaTeX manuscript written from measured results.

## Skills

SQL, data engineering, missing data, visualization. The repository must demonstrate these through executed work before they become portfolio claims.
