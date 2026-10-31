# Study 09: cross-region arrival-label hold

The proposed flight-model transfer study remains **unreleased**. [BTS defines delayed arrival](https://www.transtats.bts.gov/ot_delay/OT_DelayCause1.asp) at fifteen minutes or more after schedule. [EUROCONTROL Network Manager OTP15](https://ansperformance.eu/definition/punctuality/) permits arrival/departure within 15:59 after schedule. Directly treating these published aggregate indicators as the same event fails the common-unit gate. Counts in the 15:00–15:59 boundary interval are needed to reconcile them.

A logical illustration, not observed data: in 100 flights with 20 BTS-delayed arrivals, all twenty could be sixteen minutes late or all could be fifteen minutes thirty seconds late. Both have the same BTS aggregate; their European-threshold late counts are twenty and zero. The aggregate alone cannot identify the comparable target. [Non-operated schedules](https://ansperformance.eu/definition/opschedules/) also measure schedule/flight-plan matching and are explicitly distinguished from cancellation definitions; matched populations and original input vintages remain unverified.

No bulk outcomes, fitting or transfer/calibration score was produced, and no release was counted. The [source terms](https://ansperformance.eu/about/disclaimer/) permit attributed noncommercial copying while restricting modification; no source values were copied or transformed publicly. Obtain threshold-resolved counts, aligned reporting/operated populations and dated availability, then prospectively specify the comparable target. This bounded check does not establish that no suitable public source exists. Preserve the original proposal and continue other studies.


## Separate recorded-minute protocol and source acquisition — 31 October 2026 UTC

A [separate fixed US label-sensitivity protocol](https://github.com/S3R3Bii/arrival-label-boundaries) selects January 2024 reporting-carrier arrivals to ORD and ATL, with 14/15/16 recorded-minute probes and complete exclusion accounting. It does not convert US recorded minutes into European physical-second labels. The protocol was committed before any flight-record request.

Official BTS table/download metadata returned 200, but the selected full-archive form returned “(loadMyTable) Cannot display data.” One instrumented retry with identical dataset/year/month choices returned the same error. No archive path or flight-row values were obtained. [Source-access evidence](https://github.com/S3R3Bii/arrival-label-boundaries/blob/61c3a92036e5db1fed4723ee836298ed064cac57/data/source_access.json) and [draft PR](https://github.com/S3R3Bii/arrival-label-boundaries/pull/2) retain the failure and unexecuted gates. This repository is protocol only and is not counted among the 45 released studies.

Stop unchanged source retries. A new attempt needs changed availability of the exact fixed archive or a verified request defect. The original cross-region common-event, population, rights and historical-availability gates remain unresolved. No transfer model, threshold result, calibration, figure, manuscript or release was produced.
