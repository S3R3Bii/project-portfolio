# Flight forecast transfer across aviation systems

## Source-readiness update — 29 October 2026

Unreleased: the published US and European threshold indicators are not the same event, and matched reporting populations/vintages remain unverified. Read the [bounded common-unit hold](../source-holds/study09-flight-common-units.md). No transfer model, calibration score or completed-study claim.

**State: protocol only. No result or novelty claim yet.**

## Decision

Does a delay model tuned on US airports retain useful calibration on European operational aggregates?

## Target data

- [Bureau of Transportation Statistics aviation data](https://www.transtats.bts.gov/) — targeted; exact export and rights must be verified.
- [EUROCONTROL aviation intelligence](https://ansperformance.eu/data/) — targeted; exact export and rights must be verified.

## Study design

Domain shift and aggregate forecast calibration.

Common-unit reconciliation; region holdout; matched seasonal windows.

## Contribution to test

Test when cross-region transfer should be rejected instead of advertising one universal model. This is a proposed contribution, not a verified gap in the literature. Prior work must be reviewed before any novelty claim.

## Evidence to retain

- Exact source snapshot, request, retrieval time, observation window, definitions, units and redistribution terms.
- Prespecified splits, baseline, search space, tuning budget, seed and decision metric.
- All candidate results, including failures; final holdout used only after model selection.
- Independent headline recomputation, leakage checks and reviewed figures with units and uncertainty.
- Reproduction command and environment; private LaTeX manuscript written from measured results.

## Skills

transfer learning, calibration, measurement validity. The repository must demonstrate these through executed work before they become portfolio claims.
