# Build the research in public, one verifiable change at a time

GitHub is the working record for this program. Each completed study should show how the question, data, analysis and conclusions developed, with useful commits throughout the work.

## Commit milestones

Use a focused commit when a coherent change is ready to inspect:

1. Define the decision, research question and evaluation protocol.
2. Verify the source, rights, schema and retrieval method.
3. Implement ingestion and source reconciliation.
4. Add SQL transformations and lineage checks.
5. Establish simple baselines and the evaluation split.
6. Add a justified model or tuning comparison with retained results.
7. Investigate robustness, calibration and failure cases.
8. Add independent checks and automated verification.
9. Produce the figures and decision summary.
10. Package a reproducible release with its limitations and next experiment.

These are meaningful work units, not a commit quota. Combine inseparable changes and commit smaller changes when each has a clear purpose. Preserve normal timestamps and accurate authorship. Do not rewrite older projects to imply work happened at another time.

## Issues, branches and pull requests

- Open an issue for a concrete research question, defect or deliverable. State the acceptance criteria and link the relevant data or method.
- Use a short descriptive branch for a substantive change. Link its pull request to the issue and explain the resulting behavior and validation.
- Review the diff, numerical checks and rendered figures before merging. Keep meaningful commits visible when merging; do not squash solely to hide the research process.
- Record negative findings, corrected defects and failed approaches when they inform the result. A short evidence note is more useful than a long generic progress log.
- Use releases for reproducible study milestones: exact source snapshot, code revision, environment, results and limitations. A release is not a journal publication.

## Public/private boundary

Public commits contain only reviewed code, eligible data, derived results and visuals. Manuscript drafts stay in a separate private location outside public repository history. Business-sensitive projects such as PikiVu use approved visual case studies rather than source publication. Do not commit keys, personal records, local machine paths, environment files or proprietary datasets.

Use the account's verified GitHub noreply identity for commits. Run a focused privacy check on the staged diff before pushing. Check GitHub's actual state before claiming a push, check, pull request or release succeeded.

## Evidence of progress

For each study, retain its issue, commit and pull-request links, successful checks, release revision and current status. Report actual activity and completed work; leave proposed studies labeled as proposed. The portfolio should let a hiring team inspect both scientific judgment and practical engineering habits.

GitHub's [profile-contribution documentation](https://docs.github.com/en/account-and-profile/concepts/contributions-on-your-profile) explains the public activity graph and the timeline of commits, issues and pull requests. Display timing and eligibility are controlled by GitHub.
