# Flight trajectory compression for operational analytics

## Execution update — 30 October 2026

A scoped study is executed and released at https://github.com/S3R3Bii/flight-compression-query-audit. Every point-reducing setting fails at least one fixed budget on a development run, so the selector retains the original points. On 65 final runs from 17 different aircraft, geometric 25 m retains 8.1% of point-record bytes but fails a budget on every run. Time-aware 10 m retains 33.0% and fails only the route-length budget on 12 runs. No final-set reselection occurs. Read its fixed executable protocol, complete exclusions and validation. The broader proposal below is retained as historical design context; it is not the release specification. Independent program manuscripts are public after checks; separate formal-publication projects remain private.

**Historical proposal, superseded by the scoped release above.**

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
