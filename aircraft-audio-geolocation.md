# Inferring a recording location from aircraft sound

A passing aircraft leaves a changing harmonic pattern in a recording. This project measures that pattern, predicts how sound arrives from flight trajectories, and tests the listener geometry.

## Findings

The initial global blind search abstained. Recording-time information and the flight identity were later supplied by the participant. A controlled comparison tested 42 time-overlapping aircraft without a callsign-prefix filter; 39 had valid fits. The supplied aircraft ranked first under one bounded source-pitch-drift curve-error model, but not across spectrogram objectives and clock assumptions. The observer estimates remain conditional and were not independently validated.

This project **did not uniquely identify the aircraft or verify an exact recording location from audio alone**.

## Analytical work

- Preserve two clips of one flyover on their elapsed-time axis, including the unrecorded 15.16-second interval.
- Extract and review harmonic-spacing measurements.
- Model three-dimensional range, retarded sound-emission time, source pitch, terrain and a modeled atmosphere.
- Compare traced-frequency error with direct spectrogram contrast.
- Audit assumptions, candidate coverage and sensitivity rather than treating numerical rank as identification confidence.

## Read and reproduce

- [Research manuscript (PDF)](projects/aircraft-doppler-geolocation/Audio_Location_Public.pdf)
- [Sanitized project archive (ZIP)](projects/aircraft-doppler-geolocation/Aircraft_Audio_Public_Project.zip)
- [Interactive portfolio](https://james-jean-data-science.s3r3bii.chatgpt.site)

The archive contains the LaTeX manuscript and figures, actual anonymized curve measurements, 42-candidate score table, reusable propagation code and executable physics checks. It does not contain the private recordings or the full private trajectory/environmental reconstruction. The retained tables and figures support review of the reported results; the generic physics tests are not independent validation of a real-world location.

## Privacy and scope

The public materials omit recordings, exact recording date/time, aircraft identifiers and geographic hypotheses. This is a single-event retrospective research case study, not a validated forensic identification service. Public source datasets retain their original terms.

[Back to the project gallery](README.md)
