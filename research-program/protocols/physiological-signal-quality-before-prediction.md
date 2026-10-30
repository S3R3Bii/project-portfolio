# Physiological signal quality before prediction

## Execution update — 30 October 2026

A scoped study is executed and released at https://github.com/S3R3Bii/ecg-quality-gate-transfer. All three candidate gates violate the authored 5% source-clean false-rejection constraint. The least aggressive flags 58 of 150 later source-clean development windows (38.666666667%); the full range is 38.666666667-52%. The fixed selection keeps accept-all, providing no noise-detection improvement. A secondary separate-recording audit of the same rejected thresholds flags 14-22% of source-clean controls, without recalibration or reselection. This is a negative finding about these two features and the declared calibration/search, without clinical acceptability or safety claims. Read its fixed executable protocol, complete exclusions and validation. The broader proposal below is retained as historical design context; it is not the release specification. Independent program manuscripts are public after checks; separate formal-publication projects remain private.

**Historical proposal, superseded by the scoped release above.**

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
