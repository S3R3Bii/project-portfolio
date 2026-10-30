# Broadband planning under map-version changes

## Execution update — 30 October 2026

A scoped study is executed and released at https://github.com/S3R3Bii/broadband-map-denominators. Among 90 later state-transitions with 100/20 Mbps reported-share gains, 20 have a positive denominator component. Across all 102 later transitions, the equal-geography mean reported-share change is 0.749748902 percentage points, the mean served-quantity component is 1.148377635 points and the mean denominator component is -0.398628733 points. The fixed served-quantity counterfactual is infeasible for one DC transition at each speed. These are exact accounting comparisons using fraction-implied quantities, without construction, adoption or causal attribution. Read its fixed executable protocol, complete exclusions and validation. The broader proposal below is retained as historical design context; it is not the release specification. Independent program manuscripts are public after checks; separate formal-publication projects remain private.

**Historical proposal, superseded by the scoped release above.**

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
