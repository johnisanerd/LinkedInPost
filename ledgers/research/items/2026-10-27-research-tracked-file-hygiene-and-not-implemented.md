---
id: 2026-10-27-research-tracked-file-hygiene-and-not-implemented
title: Tracked-file hygiene and not-implemented journeys
created: '2026-10-27'
updated: '2026-10-27'
journeys: []
related: []
docs:
- docs/launch-readiness/findings/HYGIENE.md
status: complete
source_revision: a65b712
---

## Question

Which tracked files should not be in git, and which journey features are absent?

## Sources and method

git ls-files and grep checks at the review revision. docs/launch-readiness/findings/HYGIENE.md.

## Findings

10 tracked .DS_Store files, tracked agent run state under state/, a tracked frontend/.env.development with a bypass key, YouTube publish rejected, YouTube poll schedule commented out, no test script.

## Limits

Read-only static reading at the stated revision; nothing was executed. Items filed from this record are unverified until a check is run and recorded.

## Recommendations and follow-up

See HYG and NI items.
