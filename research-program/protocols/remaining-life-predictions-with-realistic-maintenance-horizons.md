# Remaining-life predictions with realistic maintenance horizons

**State: protocol only. No result or novelty claim yet.**

## Decision

Which model gives useful warnings early enough to schedule maintenance under a fixed inspection budget?

## Target data

- [NASA prognostics data repository](https://www.nasa.gov/intelligent-systems-division/discovery-and-systems-health/pcoe/pcoe-data-set-repository/) — targeted; exact export and rights must be verified.

## Study design

Survival or sequence models versus simple degradation baselines.

Engine-unit holdout; operating-regime holdout; lead-time-specific calibration.

## Contribution to test

Score maintenance decisions and warning timeliness instead of random-window RMSE. This is a proposed contribution, not a verified gap in the literature. Prior work must be reviewed before any novelty claim.

## Evidence to retain

- Exact source snapshot, request, retrieval time, observation window, definitions, units and redistribution terms.
- Prespecified splits, baseline, search space, tuning budget, seed and decision metric.
- All candidate results, including failures; final holdout used only after model selection.
- Independent headline recomputation, leakage checks and reviewed figures with units and uncertainty.
- Reproduction command and environment; private LaTeX manuscript written from measured results.

## Skills

predictive maintenance, ML tuning, survival analysis. The repository must demonstrate these through executed work before they become portfolio claims.
