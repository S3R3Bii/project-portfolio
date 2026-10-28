# Storm damage ranking under incomplete reporting

**State: protocol only. No result or novelty claim yet.**

## Decision

Which regional risk rankings survive plausible underreporting and heavy-tailed loss assumptions?

## Target data

- [NOAA storm events](https://www.ncei.noaa.gov/access/storm-events-database/) — targeted; exact export and rights must be verified.

## Study design

Robust ranking and tail-sensitive aggregation.

Era-consistent event coverage; damage-unit audit; bootstrap by event; missing-versus-zero sensitivity.

## Contribution to test

Produce a ranking stability envelope, not a falsely precise map of expected insured loss. This is a proposed contribution, not a verified gap in the literature. Prior work must be reviewed before any novelty claim.

## Evidence to retain

- Exact source snapshot, request, retrieval time, observation window, definitions, units and redistribution terms.
- Prespecified splits, baseline, search space, tuning budget, seed and decision metric.
- All candidate results, including failures; final holdout used only after model selection.
- Independent headline recomputation, leakage checks and reviewed figures with units and uncertainty.
- Reproduction command and environment; private LaTeX manuscript written from measured results.

## Skills

robust statistics, uncertainty, geospatial analysis. The repository must demonstrate these through executed work before they become portfolio claims.
