# Human-readable models versus explanation stability

**State: protocol only. No result or novelty claim yet.**

## Decision

Which models retain stable explanations after small, plausible data perturbations?

## Target data

- [OpenML benchmark data and tasks](https://www.openml.org/) — targeted; exact export and rights must be verified.

## Study design

GAM/tree baselines versus boosted models with explanation sensitivity.

Nested tuning; correlated-feature tests; rank stability and predictive loss evaluated together.

## Contribution to test

Make explanation stability a measured tradeoff rather than a decorative SHAP plot. This is a proposed contribution, not a verified gap in the literature. Prior work must be reviewed before any novelty claim.

## Evidence to retain

- Exact source snapshot, request, retrieval time, observation window, definitions, units and redistribution terms.
- Prespecified splits, baseline, search space, tuning budget, seed and decision metric.
- All candidate results, including failures; final holdout used only after model selection.
- Independent headline recomputation, leakage checks and reviewed figures with units and uncertainty.
- Reproduction command and environment; private LaTeX manuscript written from measured results.

## Skills

interpretable ML, robustness, statistical validation. The repository must demonstrate these through executed work before they become portfolio claims.
