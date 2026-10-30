# Economic forecasts with revision-safe evaluation

## Execution update — 30 October 2026

A scoped study is executed and released at https://github.com/S3R3Bii/gdp-vintage-forecast-audit. On 42 held quarters, the development-selected 50% blend has MAE 3.629 versus 2.987 for the plain 20-quarter mean using origin inputs and early GDP. Later targets change these to 3.641 and 3.012. Mean 20 leads all four regimes; target changes reverse one other pair under hindsight inputs and none under origin inputs. No trading or operational benefit is measured. Read its fixed executable protocol, complete exclusions and validation. The broader proposal below is retained as historical design context; it is not the release specification. Independent program manuscripts are public after checks; separate formal-publication projects remain private.

**Historical proposal, superseded by the scoped release above.**

## Decision

Which model wins change when first-release economic data replace the latest revised series?

## Target data

- [Federal Reserve economic data](https://fred.stlouisfed.org/) — targeted; exact export and rights must be verified.

## Study design

Vintage-aware forecasting and ranking comparison.

ALFRED vintage availability gate; identical information sets; rolling origins.

## Contribution to test

Measure the price of hindsight explicitly instead of publishing one backtest score. This is a proposed contribution, not a verified gap in the literature. Prior work must be reviewed before any novelty claim.

## Evidence to retain

- Exact source snapshot, request, retrieval time, observation window, definitions, units and redistribution terms.
- Prespecified splits, baseline, search space, tuning budget, seed and decision metric.
- All candidate results, including failures; final holdout used only after model selection.
- Independent headline recomputation, leakage checks and reviewed figures with units and uncertainty.
- Reproduction command and environment; private LaTeX manuscript written from measured results.

## Skills

quant research, time series, data provenance. The repository must demonstrate these through executed work before they become portfolio claims.
