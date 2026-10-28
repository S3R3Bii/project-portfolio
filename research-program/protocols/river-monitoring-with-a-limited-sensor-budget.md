# River monitoring with a limited sensor budget

**State: protocol only. No result or novelty claim yet.**

## Decision

Which gauges add the most independent warning information for downstream water-level changes?

## Target data

- [USGS water data APIs](https://api.waterdata.usgs.gov/) — targeted; exact export and rights must be verified.

## Study design

Lagged conditional dependence and sensor subset selection.

Basin-held-out and chronological testing; missing telemetry stress; lead-time audit.

## Contribution to test

Optimize informational redundancy while distinguishing predictive association from hydrologic causality. This is a proposed contribution, not a verified gap in the literature. Prior work must be reviewed before any novelty claim.

## Evidence to retain

- Exact source snapshot, request, retrieval time, observation window, definitions, units and redistribution terms.
- Prespecified splits, baseline, search space, tuning budget, seed and decision metric.
- All candidate results, including failures; final holdout used only after model selection.
- Independent headline recomputation, leakage checks and reviewed figures with units and uncertainty.
- Reproduction command and environment; private LaTeX manuscript written from measured results.

## Skills

sensor analytics, feature selection, time series. The repository must demonstrate these through executed work before they become portfolio claims.
