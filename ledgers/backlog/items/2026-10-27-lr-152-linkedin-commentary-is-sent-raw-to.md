---
id: 2026-10-27-lr-152-linkedin-commentary-is-sent-raw-to
title: LinkedIn commentary is sent raw to rest/posts, where reserved characters may truncate multi-image posts.
created: '2026-10-27'
updated: '2026-10-27'
journeys:
- 2026-10-27-j067-pick-and-upload-images-for-a
- 2026-10-27-j076-publish-now-to-linkedin
related: []
docs:
- worker/src/integrations/linkedin/index.ts
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: investigation
severity: P2
area: worker/integrations
raw_id: LR-152
source_file: docs/launch-readiness/findings/REVIEW-ITEMS.md
---

## Problem

LinkedIn commentary is sent raw to rest/posts, where reserved characters may truncate multi-image posts. Suspected, not confirmed (see Confidence in the evidence).

## Evidence and reproduction

- **Confidence:** hypothesis
- **Journeys:** J-067, J-076
- **Aliases:** WKB-022
- **Evidence:** worker/src/integrations/linkedin/index.ts:60-63,75
- **Repro:** static; executor: publish a 2-image post with text "Results (up 40%)" and compare with the LinkedIn rendering.
- **Fix hint:** Escape reserved characters for rest/posts or use ugcPosts consistently; add real alt text.

## Acceptance criteria

- The question in the title is answered in Attempts with file:line evidence and a clear yes/no.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

Escape reserved characters for rest/posts or use ugcPosts consistently; add real alt text.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/REVIEW-ITEMS.md (LR-152). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: hypothesis from static reading of worker/src/integrations/linkedin/index.ts:60-63,75; confirm by running the Repro and observing the described behaviour.
