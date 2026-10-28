# Broadband planning under map-version changes

**State: protocol only. No result or novelty claim yet.**

## Decision

Which apparent service improvements are revisions to the availability map rather than new coverage?

## Target data

- [FCC broadband data downloads](https://broadbandmap.fcc.gov/data-download) — targeted; exact export and rights must be verified.
- [US Census data APIs](https://www.census.gov/data/developers/data-sets.html) — targeted; exact export and rights must be verified.

## Study design

Versioned spatial joins and change attribution.

Location-ID lineage; comparable map releases; availability versus adoption separation.

## Contribution to test

Audit the data product before treating mapped coverage changes as investment impact. This is a proposed contribution, not a verified gap in the literature. Prior work must be reviewed before any novelty claim.

## Evidence to retain

- Exact source snapshot, request, retrieval time, observation window, definitions, units and redistribution terms.
- Prespecified splits, baseline, search space, tuning budget, seed and decision metric.
- All candidate results, including failures; final holdout used only after model selection.
- Independent headline recomputation, leakage checks and reviewed figures with units and uncertainty.
- Reproduction command and environment; private LaTeX manuscript written from measured results.

## Skills

geospatial SQL, data lineage, public policy analytics. The repository must demonstrate these through executed work before they become portfolio claims.
