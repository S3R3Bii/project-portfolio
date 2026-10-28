# Model selection under a fixed compute budget

**State: protocol only. No result or novelty claim yet.**

## Decision

Which tuning strategy yields the most reliable improvement per unit of compute across heterogeneous tabular tasks?

## Target data

- [OpenML benchmark data and tasks](https://www.openml.org/) — targeted; exact export and rights must be verified.

## Study design

Nested benchmark of random search and successive halving.

Dataset-level holdout; fixed budgets and seeds; tuning-time accounting; test set isolation.

## Contribution to test

Report unsuccessful searches and variability, not just the winning run. This is a proposed contribution, not a verified gap in the literature. Prior work must be reviewed before any novelty claim.

## Evidence to retain

- Exact source snapshot, request, retrieval time, observation window, definitions, units and redistribution terms.
- Prespecified splits, baseline, search space, tuning budget, seed and decision metric.
- All candidate results, including failures; final holdout used only after model selection.
- Independent headline recomputation, leakage checks and reviewed figures with units and uncertainty.
- Reproduction command and environment; private LaTeX manuscript written from measured results.

## Skills

ML tuning, experimental design, benchmarking, reproducibility. The repository must demonstrate these through executed work before they become portfolio claims.
