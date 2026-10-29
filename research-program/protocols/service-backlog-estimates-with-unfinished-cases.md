# Service backlog estimates with unfinished cases

## Execution update — 29 October 2026

A scoped study is executed and released at https://github.com/S3R3Bii/closure-time-censoring. Across eight primary held NYC311 panels, censoring-aware 28-day restricted means have equal-panel MAE 0.033 calendar days versus 1.689 for capped completed-case summaries against the later captured-record benchmark. Every one of 96 held sensitivities favors the restricted mean; synthetic cutoffs and unverified censoring assumptions limit interpretation. Read its fixed executable protocol, complete exclusions and validation. The broader proposal below is retained as historical design context; it is not the release specification. Independent program manuscripts are public after checks; separate formal-publication projects remain private.

**Historical proposal, superseded by the scoped release above.**

## Decision

How misleading is the average closure time when many service requests remain open?

## Target data

- [NYC 311 service requests](https://data.cityofnewyork.us/resource/erm2-nwe9) — targeted; exact export and rights must be verified.

## Study design

Survival estimates and restricted mean closure time.

Censoring audit; agency and future-cohort holdouts; sensitivity to status recoding.

## Contribution to test

Compare what a live manager could know with a completed-cases-only retrospective dashboard. This is a proposed contribution, not a verified gap in the literature. Prior work must be reviewed before any novelty claim.

## Evidence to retain

- Exact source snapshot, request, retrieval time, observation window, definitions, units and redistribution terms.
- Prespecified splits, baseline, search space, tuning budget, seed and decision metric.
- All candidate results, including failures; final holdout used only after model selection.
- Independent headline recomputation, leakage checks and reviewed figures with units and uncertainty.
- Reproduction command and environment; private LaTeX manuscript written from measured results.

## Skills

survival analysis, SQL, operational metrics, R. The repository must demonstrate these through executed work before they become portfolio claims.
