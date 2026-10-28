# Operational metrics that survive data pipeline changes

**State: protocol only. No result or novelty claim yet.**

## Decision

Which integrity checks catch a broken reporting feed before it changes a business decision?

## Target data

- [Consumer Financial Protection Bureau](https://www.consumerfinance.gov/data-research/consumer-complaints/) — targeted; exact export and rights must be verified.
- [NYC Taxi and Limousine Commission trip records](https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page) — targeted; exact export and rights must be verified.
- [EIA balancing authority operations](https://www.eia.gov/electricity/930-content/about.html) — targeted; exact export and rights must be verified.

## Study design

Replay of documented schema changes plus explicitly injected faults.

Separate real revisions from synthetic faults; independent expected outputs; latency and false-alert accounting.

## Contribution to test

Benchmark decision-changing failures instead of counting generic null checks. This is a proposed contribution, not a verified gap in the literature. Prior work must be reviewed before any novelty claim.

## Evidence to retain

- Exact source snapshot, request, retrieval time, observation window, definitions, units and redistribution terms.
- Prespecified splits, baseline, search space, tuning budget, seed and decision metric.
- All candidate results, including failures; final holdout used only after model selection.
- Independent headline recomputation, leakage checks and reviewed figures with units and uncertainty.
- Reproduction command and environment; private LaTeX manuscript written from measured results.

## Skills

SQL, data engineering, testing, observability. The repository must demonstrate these through executed work before they become portfolio claims.
