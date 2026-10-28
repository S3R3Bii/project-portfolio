# Brake-event detection that transfers across roads

## Execution update — 28 October 2026

A narrower study was executed under a fixed repository protocol: past-only acceleration-reference reconstruction and frame-alert transfer across three roads. It does not establish independent brake-event detection or latency. All 18 candidates, source data and held-out results are at https://github.com/S3R3Bii/brake-signal-transfer. The broader proposal below remains history and a source of future experiments.

**State: protocol only. No result or novelty claim yet.**

## Decision

Can a detector identify abrupt deceleration with a fixed false-alert budget on unseen traffic settings?

## Target data

- [California PATH vehicle trajectories](https://highways.dot.gov/research/research-data-resources/next-generation-simulation-ngsim) — targeted; exact export and rights must be verified.

## Study design

Trajectory smoothing and event detection.

Vehicle-group and site holdouts; derivative-noise sensitivity; independently checked kinematics.

## Contribution to test

Quantify the tradeoff between smoothing latency and missed events. This is a proposed contribution, not a verified gap in the literature. Prior work must be reviewed before any novelty claim.

## Evidence to retain

- Exact source snapshot, request, retrieval time, observation window, definitions, units and redistribution terms.
- Prespecified splits, baseline, search space, tuning budget, seed and decision metric.
- All candidate results, including failures; final holdout used only after model selection.
- Independent headline recomputation, leakage checks and reviewed figures with units and uncertainty.
- Reproduction command and environment; private LaTeX manuscript written from measured results.

## Skills

kinematics, signal processing, time series, ML evaluation. The repository must demonstrate these through executed work before they become portfolio claims.
