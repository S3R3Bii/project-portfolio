# Vehicle recall remedy delays

**State: protocol only. No result or novelty claim yet.**

## Decision

Which recall characteristics predict a long period before remedy availability, using only initial notice information?

## Target data

- [NHTSA recall APIs](https://www.nhtsa.gov/nhtsa-datasets-and-apis) — targeted; exact export and rights must be verified.

## Study design

Time-to-event modeling and censored evaluation.

Manufacturer-held-out and chronological tests; initial-versus-amended field audit.

## Contribution to test

Model service planning lead time rather than classifying vehicle safety for individuals. This is a proposed contribution, not a verified gap in the literature. Prior work must be reviewed before any novelty claim.

## Evidence to retain

- Exact source snapshot, request, retrieval time, observation window, definitions, units and redistribution terms.
- Prespecified splits, baseline, search space, tuning budget, seed and decision metric.
- All candidate results, including failures; final holdout used only after model selection.
- Independent headline recomputation, leakage checks and reviewed figures with units and uncertainty.
- Reproduction command and environment; private LaTeX manuscript written from measured results.

## Skills

survival analysis, feature provenance, model validation. The repository must demonstrate these through executed work before they become portfolio claims.
