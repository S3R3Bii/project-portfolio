# Airport taxi dispatch with asymmetric waiting costs

## Execution update — 29 October 2026

A scoped study is executed and released at https://github.com/S3R3Bii/airport-pickup-capacity. The frozen 75th-percentile policy has 4.5% lower held modeled cost than the median in the declared 250-services-per-zone-hour, 3:1 cost scenario, despite higher raw count error. On the two fixed holiday dates its cost is 15.1% higher. Both findings are retained; actual dispatch availability, queues and savings are not established. Read its fixed executable protocol, complete exclusions and validation. The broader proposal below is retained as historical design context; it is not the release specification. Independent program manuscripts are public after checks; separate formal-publication projects remain private.

**Historical proposal, superseded by the scoped release above.**

## Decision

Should airport pickup planning use the median or a higher demand quantile by hour?

## Target data

- [NYC Taxi and Limousine Commission trip records](https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page) — targeted; exact export and rights must be verified.

## Study design

Quantile forecasts and bounded dispatch-capacity simulation.

Month-blocked tuning; holiday stress test; missing trip and zone consistency checks.

## Contribution to test

Translate forecast error into excess vehicles versus unmet observed trip demand without claiming rider wait-time ground truth. This is a proposed contribution, not a verified gap in the literature. Prior work must be reviewed before any novelty claim.

## Evidence to retain

- Exact source snapshot, request, retrieval time, observation window, definitions, units and redistribution terms.
- Prespecified splits, baseline, search space, tuning budget, seed and decision metric.
- All candidate results, including failures; final holdout used only after model selection.
- Independent headline recomputation, leakage checks and reviewed figures with units and uncertainty.
- Reproduction command and environment; private LaTeX manuscript written from measured results.

## Skills

SQL, Python, quantile regression, optimization. The repository must demonstrate these through executed work before they become portfolio claims.
