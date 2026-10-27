---
id: 2026-10-27-idea-011-bin-journey-health-did-not-complete
title: bin/journey-health did not complete and is not portable
created: '2026-10-27'
updated: '2026-10-27'
journeys: []
related:
- 2026-10-27-gap-001-no-executor-pass-nothing-was-run
docs: []
status: captured
promoted_to: []
raw_id: IDEA-011
source_file: docs/launch-readiness/findings/LEGACY-TRACKERS.md
---

## Idea

bin/journey-health did not complete and is not portable. Captured from the legacy tracker; not a commitment. - **Source:** docs/launch-readiness/legacy/MCP-TEST-IDEAS.md (bin/journey-health runs bounced: J1 ran 5/6 before timeout; kill-test not done)
- **Detail:** The script hard-codes LP_ROOT=/home/openclaw/workspaces/linkedin-post and checks ports through /proc/net/tcp, so it is Linux-only and cannot run on a Mac checkout as written. Neither the healthy-stack run nor the dead-stack run finished.
- **Action:** Make LP_ROOT relative to the script and use a portable port check; then use it as part of GAP-001's executor pass.

## Open questions

What would justify promoting this: a real user need, an owner decision, or a failing journey. read-only: bin/journey-health read (lines 9, 28): hard-coded path and /proc/net/tcp check.

## Promotion

No promotion yet. If promoted, link the new backlog item here and set promoted_to.
