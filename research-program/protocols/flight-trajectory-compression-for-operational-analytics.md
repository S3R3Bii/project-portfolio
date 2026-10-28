# Flight trajectory compression for operational analytics

**State: protocol only. No result or novelty claim yet.**

## Decision

How much can trajectory storage be reduced before route and delay metrics become misleading?

## Target data

- [OpenSky Network data](https://opensky-network.org/data/) — targeted; exact export and rights must be verified.

## Study design

Error-bounded compression and query benchmarking.

Terms and access gate; flight-held-out test; spatial and timing error budgets.

## Contribution to test

Connect compression tolerance to analytical decision accuracy. This is a proposed contribution, not a verified gap in the literature. Prior work must be reviewed before any novelty claim.

## Evidence to retain

- Exact source snapshot, request, retrieval time, observation window, definitions, units and redistribution terms.
- Prespecified splits, baseline, search space, tuning budget, seed and decision metric.
- All candidate results, including failures; final holdout used only after model selection.
- Independent headline recomputation, leakage checks and reviewed figures with units and uncertainty.
- Reproduction command and environment; private LaTeX manuscript written from measured results.

## Skills

data engineering, algorithms, benchmarking. The repository must demonstrate these through executed work before they become portfolio claims.
