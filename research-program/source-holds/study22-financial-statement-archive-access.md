# Study 22: official financial-statement bulk archive access

The SEC [Financial Statement Data Sets](https://www.sec.gov/data-research/sec-markets-data/financial-statement-data-sets) provide an official alternative to the blocked companyfacts API. The accessible documentation describes accession-linked submissions, primary-statement facts and a revised native key including segments. The landing page also describes December 2024 reprocessing; a current historical bundle cannot by itself establish what a bulk-data consumer saw at an earlier date.

On 30 October 2026, ordinary HEAD requests to the page-linked 2025 Q4 and 2026 Q1 ZIPs returned HTTP403. A single ordinary GET check of 2025 Q4, closed before reading financial facts, also returned HTTP403. No financial-fact body was read, cohort established, join tested or model fitted. The API and this alternative bulk route remain access holds. No access control was bypassed and no identity was rotated.

A future authorized source export still needs exact accession/context/unit/taxonomy reconciliation and preserved prior-versus-current report evidence. No financial restatement, leakage rate, investment conclusion or completed-study claim follows from this source check.
