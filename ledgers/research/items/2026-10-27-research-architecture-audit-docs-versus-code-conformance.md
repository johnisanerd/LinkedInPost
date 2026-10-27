---
id: 2026-10-27-research-architecture-audit-docs-versus-code-conformance
title: 'Architecture audit: docs versus code conformance'
created: '2026-10-27'
updated: '2026-10-27'
journeys: []
related: []
docs:
- docs/launch-readiness/findings/ARCH-AUDIT.md
status: complete
source_revision: a65b712
---

## Question

Do the documented architecture, config, and deployment claims match the code?

## Sources and method

Static reading of docs and config at a65b712. docs/launch-readiness/findings/ARCH-AUDIT.md.

## Findings

20 architecture findings (ARCH-001..020), each tracked as a duplicate of a merged review item or kept as its own record. The conformance table lists each doc claim with its verdict.

## Limits

Read-only static reading at the stated revision; nothing was executed. Items filed from this record are unverified until a check is run and recorded. The architecture audit missed a tracked env file (HYG-003), so it is not a complete secret scan.

## Recommendations and follow-up

Keep ARCH rows as duplicates of their review items; fix the review item, not the audit.
