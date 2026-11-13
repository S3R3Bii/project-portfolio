BANKING INTENT ATLAS

Knowing when an NLP routershould defer

James N. Jean IV | Independent portfolio engineering study | November 13, 2026Substantial ChatGPT Codex assistance; local CPU inference; no paid inference service.

Executive summary. A fixed pretrained sentence encoder improved top-1 banking-intent accuracy from 86.8% to 91.7% on 3,080 official BANKING77 test queries. Both classifiers were trained on the same 6,958-row fitting partition. A separate policy split selected the encoder pipeline before test scoring. [1, 2]

At its frozen 0.66 confidence threshold, the selected pipeline accepted 2,755 queries (89.4%) and referred 325 for human review. It made 96 errors among accepted queries: 3.5%, with a 95% Wilson interval of 2.9%-4.2%. This is offline benchmark evidence, not a deployment guarantee.

Figure 1. Test-set coverage/error curves are descriptive. Filled points are policies frozen on a separate split. The 5% line is an illustrative design target; thresholds were not retuned on this curve.

Recommendation. Use the encoder pipeline as the stronger candidate for a supervised intent-suggestion pilot. Retain human review and a separate domain check: it confidently accepted 2 of 12 synthetic non-banking probes. No banking action should be automated from this study.

1. Keep the evidence streams separate

BANKING77 provides English online-banking queries labeled with 77 intents. Its official training/test split supplies a useful constrained benchmark, but it has no customer identifiers, timestamps or live operational outcomes. This study preserves all official test rows for its primary comparison. [1]

Figure 2. The three lower boxes partition the 9,941 eligible training rows. The official test set is a separate cohort, not the next stage of that training funnel.

The fingerprint uses NFKC normalization, case-folding and alphanumeric characters. It removes exact-normalized overlap, not semantic paraphrases. A post hoc sensitivity check deduplicated test text and removed conflicting-label groups: 3,075 queries remained, with 91.74% encoder accuracy versus the primary 91.72%. This diagnostic did not change the model or policy.

2. Compare two complete, fixed pipelines

Figure 3. Full-test top-1 accuracy; error bars are 95% Wilson intervals over query rows. The majority-class reference is selected from the fitting split.

The encoder advantage was 4.97 percentage points; a paired 2,000-resample query bootstrap gave a 95% interval of 3.86-6.07 points. The interval conditions on these two trained pipelines and the fixed test set; it does not include training-seed variation or future customer drift.

Lexical representation. TF-IDF uses word unigrams/bigrams, sublinear term frequency, min_df=2, up to 30,000 features and L2 normalization. The vocabulary and IDF are learned only from the fitting split. Negation and other stopwords are retained.

Semantic representation. The author-published all-MiniLM-L6-v2 ONNX model maps each query to a 384-dimensional vector. Attention-mask mean pooling and L2 normalization follow the model card. No query reached the 256-wordpiece limit. The encoder is frozen; only the downstream classifier is trained. [2]

Both classifiers use L2 logistic regression with C=4, lbfgs and a 1,000-iteration cap; both converged before the cap. These are fixed engineering settings, not tuned optima. Equal C does not imply equal effective regularization across feature spaces.

3. Turn confidence into a review policy

A single temperature per model minimizes negative log likelihood on the 1,491-row calibration split. The separate 1,492-row policy split considers confidence cutoffs from 0.00 to 0.99. An eligible cutoff must accept at least 200 queries and have a two-sided 95% Wilson upper error bound at or below 5%. Among eligible cutoffs, choose greatest coverage. [3]

Figure 4. Final-test reliability after temperature calibration. Ten equal-width bins; sparse low-confidence bins can fluctuate. ECE is 0.0143 for TF-IDF and 0.0129 for MiniLM, not a universal confidence guarantee.

The encoder offers more coverage at its own qualifying threshold, while the lexical policy has fewer accepted errors. This is a workload/risk tradeoff, not a claim that the encoder dominates every operating point. The policy-split bound is a selection heuristic; the independent test evaluates the frozen choice.

4. Inspect failures, including confident ones

Figure 5. Six most frequent wrong-label pairs for the selected encoder over all 3,080 test queries. Similar banking concepts remain separable labels in this benchmark.

Errors such as card arrival versus delivery estimate and declined transfer versus declined card payment show why a useful system should expose alternatives instead of treating the top label as ground truth. The explorer retains top-three alternatives and distinguishes accepted mistakes from referred cases.

All 12 non-banking probes were declared before evaluation. The lexical policy accepted none; the encoder accepted the two above. This tiny authored challenge set is not an estimate of real-world out-of-domain error. It demonstrates a concrete failure of relying on maximum class probability as a domain detector.

Practical implication. A proposed pilot needs an explicit supported-intent/domain gate, a human escalation path and monitoring of novel requests. Building and validating such a gate is a next experiment, not a feature claimed by this release.

5. Engineering that can be inspected

The project runs locally in Python. Pinned public-source URLs and SHA-256 hashes identify the dataset, tokenizer and ONNX weights. The source manifest, split manifest, protocol and policy lock preserve the order of decisions. No external model API receives query text.

A SQLite database contains one query record per retained source row and one prediction per query/model. Unique indexes and explicit joins make the test grain inspectable. Public prediction CSVs contain IDs, labels, probabilities and text fingerprints; the small browser example set is drawn from the licensed benchmark.

The encoder computed 13,021 query vectors in 22.5 seconds in this run, using ONNX Runtime CPU execution with four intra-op threads. This is a single local execution observation, not a controlled speed comparison or service-level guarantee. Package versions are pinned in requirements.txt and recorded in environment.json.

James defined the portfolio objective; ChatGPT Codex substantially assisted protocol design, implementation, execution, verification, writing and presentation. This is new independent portfolio work, not prior professional NLP tenure.

6. Limits and the next defensible experiment

What the evidence establishes. Two executed pipelines, a separately selected referral policy, and independently checked outcomes on a fixed 77-intent English benchmark. The selected encoder is a stronger candidate for a supervised pilot under the stated illustrative error target.

What remains unverified. New customers, different institutions, multilingual messages, evolving intent definitions, adversarial inputs, semantically repeated customers, privacy-sensitive production text and deployment costs. No temporal or customer-group holdout is possible with the provided fields. Exact-normalized deduplication does not remove all paraphrases. The fixed pretrained encoder may have encountered related material during pretraining; this cannot be ruled out from the model card.

Statistical limits. The test contains four repeated normalized-text rows and one conflicting-label group. A deduplicated/unambiguous sensitivity check is reported separately. Row-level intervals condition on the benchmark and may understate uncertainty from latent grouping. The calibration diagnostic and authored OOD probes do not establish universal reliability or safety.

Next experiment. Obtain a permitted, genuinely new institution/time-period sample; define intended intents and unknown categories before annotation; compare the frozen baseline with an explicit domain-rejection model. Measure accepted-intent error, unknown-query rejection and human review time prospectively. Set tolerances with the team that bears the error cost. Do not infer cost savings from benchmark coverage alone.

Sources and reproducibility

[1] Casanueva, I., Temcinas, T., Gerz, D., Henderson, M., and Vulic, I. (2020). Efficient Intent Detection with Dual Sentence Encoders. NLP4ConvAI. BANKING77 dataset, CC BY 4.0.aclanthology.org/2020.nlp4convai-1.5/github.com/PolyAI-LDN/task-specific-datasets

[2] Sentence Transformers. all-MiniLM-L6-v2 model card and ONNX weights, Apache-2.0. Pinned revision and file hashes are retained in source_manifest.json.huggingface.co/sentence-transformers/all-MiniLM-L6-v2

[3] Guo, C., Pleiss, G., Sun, Y., and Weinberger, K. Q. (2017). On Calibration of Modern Neural Networks. ICML. Temperature-scaling motivation; this implementation fits only one scalar per pipeline.proceedings.mlr.press/v70/guo17a.html

Primary project evidence: PROTOCOL.md; source_manifest.json; split_manifest.csv; policy_lock.json; predictions.csv; metrics.json; independent_audit.json; queries.sql. Source code and reproducibility instructions are included in the portfolio repository.