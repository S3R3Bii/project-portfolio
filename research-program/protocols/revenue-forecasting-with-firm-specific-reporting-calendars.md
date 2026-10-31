# Revenue forecasting with firm-specific reporting calendars

## Execution update — 31 October 2026 UTC

A scoped study is executed and released at https://github.com/S3R3Bii/revenue-reporting-calendars. On 13 protected pairs, calendar pooling has 4.758807% equal-company macro MAPE and fiscal pooling 4.776929%; the small ordering changes across company/year accounts. Zero-growth same-quarter revenue wins validation at 6.789346% but has 10.048371% test MAPE; test results do not replace the committed selection. Walmart zero growth beats all growth-pooling candidates on its four targets. Read its fixed executable protocol, complete exclusions and validation. The broader proposal below is retained as historical design context; it is not the release specification. Independent program manuscripts are public after checks; separate formal-publication projects remain private.

**Historical proposal, superseded by the scoped release above.**

## Decision

Does fiscal-quarter alignment outperform calendar-quarter pooling when forecasting reported revenue?

## Target data

- [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces) — targeted; exact export and rights must be verified.

## Study design

Panel forecasting with filing-time covariates.

Company and future-filing holdouts; amendment embargo; scale-normalized losses.

## Contribution to test

Treat reporting-calendar design as an empirical modeling choice. This is a proposed contribution, not a verified gap in the literature. Prior work must be reviewed before any novelty claim.

## Evidence to retain

- Exact source snapshot, request, retrieval time, observation window, definitions, units and redistribution terms.
- Prespecified splits, baseline, search space, tuning budget, seed and decision metric.
- All candidate results, including failures; final holdout used only after model selection.
- Independent headline recomputation, leakage checks and reviewed figures with units and uncertainty.
- Reproduction command and environment; private LaTeX manuscript written from measured results.

## Skills

forecasting, feature engineering, panel data. The repository must demonstrate these through executed work before they become portfolio claims.
