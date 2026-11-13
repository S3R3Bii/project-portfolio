# Banking Intent Atlas: protocol frozen before evaluation

Prepared November 13, 2026. Independent portfolio engineering study by James N. Jean IV with substantial ChatGPT Codex assistance. This is an offline benchmark, not deployed banking infrastructure or a new NLP method.

## Decision

Compare a lexical classifier and a pretrained sentence-encoder classifier for routing English banking queries to 77 intent labels. Evaluate whether a confidence-based referral policy reduces errors among accepted predictions, and quantify the review workload it leaves. No account action, financial decision, identity check or consumer eligibility decision is automated.

## Source and boundary

Use the official PolyAI BANKING77 train/test files at commit `57ec275d8078af65b7731c2a98be812d844a6d6b`, licensed CC BY 4.0. There are 10,003 declared training rows and 3,080 declared test rows. Read actual counts rather than trusting those declarations. These are benchmark queries; no time stamps, user identities, deployment outcomes or operational prevalence are provided. Do not claim prospective, customer-group-disjoint or production validation.

Use the author's Apache-2.0 `sentence-transformers/all-MiniLM-L6-v2` ONNX model at commit `1110a243fdf4706b3f48f1d95db1a4f5529b4d41`. Pool token outputs with attention-mask mean pooling and L2 normalization, following the model card; limit to its documented 256 wordpieces. The encoder is frozen, not fine-tuned here. Undocumented benchmark contamination in pretraining cannot be excluded.

Candidate rationale: a banking classifier complements the lending capstone, supports analyst/AI roles and has a stable, licensed source. CFPB complaint triage was considered, but September 2026 API notes report narrative removal; this study uses BANKING77 rather than claiming a current complaint feed. A generic sentiment demo was less useful for the intended fine-grained routing decision.

## Split and leakage controls

1. Fingerprint text using Unicode NFKC normalization, case-folding, and retaining only letters/digits. This is an exact-normalized-match guard, not semantic deduplication.
2. Remove all training rows whose fingerprints occur in the official test text. Drop training fingerprint groups carrying conflicting labels; retain the first row of other duplicate training groups. Preserve every official test row for the primary evaluation and separately report within-test duplicate/conflict counts.
3. Split the remaining training rows, stratified by intent, into 70% fitting, 15% probability calibration and 15% policy selection with seed 1729. No exact-normalized fingerprint may cross partitions.
4. Fit vocabulary, IDF and classifier coefficients only on the fitting split. Fit a single temperature per model only on calibration labels. Choose referral thresholds and the recommended pipeline only on policy-selection labels. Record a policy lock before reading test outcomes for scoring. Test texts may be encoded by the frozen pretrained encoder and compared for duplicate auditing before scoring; their outcomes cannot guide these decisions.

## Fixed models

- Reference: training-majority class.
- Lexical: word unigram/bigram TF-IDF, sublinear term frequency, min_df=2, max_features=30,000, L2 normalization; multinomial L2 logistic regression, C=4, lbfgs, max_iter=1,000.
- Semantic: frozen 384-dimensional MiniLM embeddings; the same logistic-regression settings.
- Settings are fixed engineering choices, not a hyperparameter search or a claim of optimality. The common C makes the implementation comparable but does not equalize effective regularization across feature spaces.
- Temperature: minimize calibration negative log likelihood over log(T) in [-3, 3]. Preserve both raw and calibrated reliability diagnostics.

## Referral policy

On the policy split, consider thresholds 0.00, 0.01, ..., 0.99. Accept a prediction when its maximum calibrated probability is at least the threshold. Require at least 200 accepted cases and a two-sided 95% Wilson upper bound on the accepted error proportion of at most 5%. Choose the eligible threshold with greatest coverage, breaking ties toward the higher threshold. If none qualifies, accept none. The 5% target is an illustrative design criterion, not a bank-approved risk tolerance or a deployment guarantee.

Recommend the model with greater eligible policy coverage; break ties using policy macro-F1. Freeze this choice before final test scoring. Report test coverage, accepted errors, accuracy and Wilson bounds without retuning a failed policy. The policy-split bound is a selection heuristic, not a post-selection statistical guarantee; the test bound describes a fixed chosen policy on this benchmark only.

## Outcomes and uncertainty

Primary full-test metrics: top-1 accuracy, macro-F1, top-3 recall and negative log likelihood. Calibration diagnostic: 10 equal-width maximum-confidence bins, with weighted absolute confidence/accuracy difference (ECE); no claim of perfect calibration. Report exact numerators/denominators. Paired bootstrap accuracy difference uses 2,000 resamples of the same test rows, seed 1730; this is conditional on the fixed trained pipelines and benchmark, not training-seed or population uncertainty.

Evaluate a small, predeclared set of 12 synthetic non-banking queries as a separate failure probe. Their acceptance rate is not a population OOD metric. Do not tune on them. A confidence threshold alone is not an out-of-domain detector. The website explores retained test decisions; it does not run fresh inference or secretly send visitor text to an API. A local CLI supports new-text inference with the same scope warnings.

## Acceptance and review

Required: original-source hashes/license; actual data audit; partition disjointness; executed fitting/calibration/policy/test stages; saved per-row predictions; independent SQLite/standard-library recomputation of headline counts and referral behavior; no test-driven policy revision; clear paper with actual rendered-page review; truthful public project card; reproducible code and pinned environment. Keep failed checks. At most three substantive review rounds, 45 active review minutes and 60 review calls. Execution/training time is recorded separately; it is not quota or billing consumption.

Release only observed results. Retain explicit limits if results are weaker than expected. No claim of novelty, causal savings, employment experience, live users, autonomous banking capability or comprehensive OOD safety.
