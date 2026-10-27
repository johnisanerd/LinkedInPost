---
id: 2026-10-27-research-journey-designer-output-146-journeys
title: Journey designer output (146 journeys)
created: '2026-10-27'
updated: '2026-10-27'
journeys: []
related: []
docs:
- docs/launch-readiness/journeys/JOURNEYS.md
- docs/launch-readiness/journeys/COVERAGE.md
status: complete
source_revision: a65b712
---

## Question

What are the user and operator journeys the code actually supports?

## Sources and method

Journeys written from USE-CASES.md, the README, routes, dispatcher actions and wizard steps; each route checked with grep. docs/launch-readiness/journeys/JOURNEYS.md.

## Findings

146 journeys, each imported as a planned journey record. 47 carry code-reading findings; 3 are NOT IMPLEMENTED (J-013, J-081, J-118).

## Limits

Read-only static reading at the stated revision; nothing was executed. Items filed from this record are unverified until a check is run and recorded. Pass checks are not executed.

## Recommendations and follow-up

Run each journey and set its status.
