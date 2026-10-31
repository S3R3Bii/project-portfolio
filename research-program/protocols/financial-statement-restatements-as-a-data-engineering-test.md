# Financial-statement restatements as a data engineering test

## Execution update — 30 October 2026

A scoped study is executed and released at https://github.com/S3R3Bii/financial-fact-contexts. A company/tag/end-date key collapses 247 source facts into 27 groups; a one-row join would discard 220 distinct contexts. Adding duration still leaves 210 extra contexts in 37 groups; segment/coregistrant identity separates all observed facts. An authored winner differs numerically from 215 facts, reflecting different quantities as well as values; this is not a verified restatement or historical-leakage count. Read its fixed executable protocol, complete exclusions and validation. The broader proposal below is retained as historical design context; it is not the release specification. Independent program manuscripts are public after checks; separate formal-publication projects remain private.

**Historical proposal, superseded by the scoped release above.**

## Decision

How often does a naive latest-value join rewrite the historical features used in a model?

## Target data

- [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces) — targeted; exact export and rights must be verified.

## Study design

Point-in-time XBRL panel construction and revision audit.

Accession-date joins; unit and taxonomy checks; duplicate-fact tests; manual filing reconciliation.

## Contribution to test

Quantify leakage introduced by revision handling before fitting any financial model. This is a proposed contribution, not a verified gap in the literature. Prior work must be reviewed before any novelty claim.

## Evidence to retain

- Exact source snapshot, request, retrieval time, observation window, definitions, units and redistribution terms.
- Prespecified splits, baseline, search space, tuning budget, seed and decision metric.
- All candidate results, including failures; final holdout used only after model selection.
- Independent headline recomputation, leakage checks and reviewed figures with units and uncertainty.
- Reproduction command and environment; private LaTeX manuscript written from measured results.

## Skills

SQL, data engineering, data lineage, testing. The repository must demonstrate these through executed work before they become portfolio claims.
