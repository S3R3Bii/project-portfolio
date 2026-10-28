# Local hiring signals without misleading denominators

**State: protocol only. No result or novelty claim yet.**

## Decision

Which industries show sustained labor pressure after separating employment growth from establishment turnover?

## Target data

- [BLS public time series](https://www.bls.gov/data/) — targeted; exact export and rights must be verified.
- [US Census data APIs](https://www.census.gov/data/developers/data-sets.html) — targeted; exact export and rights must be verified.

## Study design

Hierarchical growth estimates and change-point detection.

Vintage and industry-code audits; future-quarter evaluation; small-cell sensitivity.

## Contribution to test

Distinguish hiring demand from changes in the reporting population. This is a proposed contribution, not a verified gap in the literature. Prior work must be reviewed before any novelty claim.

## Evidence to retain

- Exact source snapshot, request, retrieval time, observation window, definitions, units and redistribution terms.
- Prespecified splits, baseline, search space, tuning budget, seed and decision metric.
- All candidate results, including failures; final holdout used only after model selection.
- Independent headline recomputation, leakage checks and reviewed figures with units and uncertainty.
- Reproduction command and environment; private LaTeX manuscript written from measured results.

## Skills

R, SQL, hierarchical modeling, business analysis. The repository must demonstrate these through executed work before they become portfolio claims.
