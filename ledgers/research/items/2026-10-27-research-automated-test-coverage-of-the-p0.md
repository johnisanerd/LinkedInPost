---
id: 2026-10-27-research-automated-test-coverage-of-the-p0
title: Automated test coverage of the P0/P1 core journeys
created: '2026-10-27'
updated: '2026-10-27'
journeys: []
related: []
docs:
- docs/launch-readiness/findings/TEST-COVERAGE.md
status: complete
source_revision: a65b712
---

## Question

Which P0/P1 core journeys have an automated test that asserts their pass check?

## Sources and method

find and grep over worker, frontend, tests, tests-e2e, generation-worker and setup test files. docs/launch-readiness/findings/TEST-COVERAGE.md.

## Findings

70 journeys checked: 9 covered, 24 partial, 37 with no test (TST items). 10 of 15 P0 journeys have none. tests-e2e wiring specs assert their own mocks, so they do not count.

## Limits

Read-only static reading at the stated revision; nothing was executed. Items filed from this record are unverified until a check is run and recorded.

## Recommendations and follow-up

Write a test per TST item before its fix.
