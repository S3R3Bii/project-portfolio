# Cancellation-aware airport service reliability

**State: protocol only. No result or novelty claim yet.**

## Decision

Which arrival-risk metric remains useful when airlines cancel their most disrupted flights?

## Target data

- [Bureau of Transportation Statistics aviation data](https://www.transtats.bts.gov/) — targeted; exact export and rights must be verified.
- [NOAA integrated surface observations](https://www.ncei.noaa.gov/products/land-based-station/integrated-surface-database) — targeted; exact export and rights must be verified.

## Study design

Competing outcomes and route-standardized reliability decomposition.

Airline and future-year holdouts; cancellation denominator audit; matched-route sensitivity.

## Contribution to test

Treat cancellation as an outcome rather than silently removing it from delay evaluation. This is a proposed contribution, not a verified gap in the literature. Prior work must be reviewed before any novelty claim.

## Evidence to retain

- Exact source snapshot, request, retrieval time, observation window, definitions, units and redistribution terms.
- Prespecified splits, baseline, search space, tuning budget, seed and decision metric.
- All candidate results, including failures; final holdout used only after model selection.
- Independent headline recomputation, leakage checks and reviewed figures with units and uncertainty.
- Reproduction command and environment; private LaTeX manuscript written from measured results.

## Skills

SQL, statistical inference, survival analysis, communication. The repository must demonstrate these through executed work before they become portfolio claims.
