# Physiological signal quality before prediction

**State: protocol only. No result or novelty claim yet.**

## Decision

Can simple signal-quality checks prevent confident errors when recording conditions change?

## Target data

- [PhysioNet research data](https://physionet.org/) — targeted; exact export and rights must be verified.

## Study design

Signal quality features and out-of-distribution detection.

Only openly licensed noncredentialed recordings; subject-held-out validation; recording-device sensitivity.

## Contribution to test

Evaluate the quality gate separately from any downstream clinical inference. This is a proposed contribution, not a verified gap in the literature. Prior work must be reviewed before any novelty claim.

## Evidence to retain

- Exact source snapshot, request, retrieval time, observation window, definitions, units and redistribution terms.
- Prespecified splits, baseline, search space, tuning budget, seed and decision metric.
- All candidate results, including failures; final holdout used only after model selection.
- Independent headline recomputation, leakage checks and reviewed figures with units and uncertainty.
- Reproduction command and environment; private LaTeX manuscript written from measured results.

## Skills

signal processing, uncertainty, data quality. The repository must demonstrate these through executed work before they become portfolio claims.
