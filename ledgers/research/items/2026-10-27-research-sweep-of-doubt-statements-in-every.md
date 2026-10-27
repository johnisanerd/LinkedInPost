---
id: 2026-10-27-research-sweep-of-doubt-statements-in-every
title: Sweep of doubt statements in every raw review
created: '2026-10-27'
updated: '2026-10-27'
journeys: []
related: []
docs:
- docs/launch-readiness/findings/SWEEP.md
status: complete
source_revision: a65b712
---

## Question

Is every hypothesis, unverified, or TODO-style line in the raw reviews tracked?

## Sources and method

grep of doubt markers across raw reviews and findings; each hit judged tracked, new, or rejected. docs/launch-readiness/findings/SWEEP.md has the coverage table.

## Findings

The sweep reports 100 marker hit lines: 69 already tracked, 27 rejected as ordinary wording or definitions, and 4 hit lines produced 6 new items (SWP-001, SWP-002, INV-021..024). The sweep reports 4 further non-marker doubts, all already tracked. The sweep table itself is the authority for the counts.

## Limits

Read-only static reading at the stated revision; nothing was executed. Items filed from this record are unverified until a check is run and recorded.

## Recommendations and follow-up

Re-run the sweep after each review pass.
