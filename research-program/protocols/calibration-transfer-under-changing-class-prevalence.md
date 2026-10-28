# Calibration transfer under changing class prevalence

**State: protocol only. No result or novelty claim yet.**

## Decision

When can a cheap recalibration step replace full retraining after the target rate changes?

## Target data

- [OpenML benchmark data and tasks](https://www.openml.org/) — targeted; exact export and rights must be verified.

## Study design

Planned prevalence-shift experiments and recalibration.

Untouched datasets; controlled shift clearly labelled experimental; proper scoring rules.

## Contribution to test

Separate a controlled stress experiment from evidence of real production drift. This is a proposed contribution, not a verified gap in the literature. Prior work must be reviewed before any novelty claim.

## Evidence to retain

- Exact source snapshot, request, retrieval time, observation window, definitions, units and redistribution terms.
- Prespecified splits, baseline, search space, tuning budget, seed and decision metric.
- All candidate results, including failures; final holdout used only after model selection.
- Independent headline recomputation, leakage checks and reviewed figures with units and uncertainty.
- Reproduction command and environment; private LaTeX manuscript written from measured results.

## Skills

calibration, classification, ML monitoring. The repository must demonstrate these through executed work before they become portfolio claims.
