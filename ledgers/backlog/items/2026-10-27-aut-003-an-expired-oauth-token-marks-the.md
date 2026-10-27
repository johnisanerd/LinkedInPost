---
id: 2026-10-27-aut-003-an-expired-oauth-token-marks-the
title: An expired OAuth token marks the whole backlog as replied, so those comments are never answered
created: '2026-10-27'
updated: '2026-10-27'
journeys: []
related: []
docs: []
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: defect
severity: P2
area: automations
raw_id: AUT-003
source_file: docs/launch-readiness/findings/AUTOMATIONS.md
---

## Problem

An expired OAuth token marks the whole backlog as replied, so those comments are never answered.

## Evidence and reproduction

- **Journeys:** none
- **Confidence:** confirmed-by-reading
- **Evidence:** youtube_poller.py:110-112 returns True for HTTP 401 ("treat as permanent"). main() then adds the thread to `new_replied` (lines 245-248), saves the list (line 254) and records a successful poll (line 256). YOUTUBE_OAUTH_TOKEN is a single access token in a GitHub secret (workflow line 28), and Google access tokens last about an hour, so a stale token is the normal case.
- **Repro:** Run with an expired YOUTUBE_OAUTH_TOKEN: the log shows "reply auth failed (401)" for each comment, the run reports "done — replied to N comments", and after refreshing the token a rerun skips all of them.
- **Fix hint:** Return False (not replied) on 401 and abort the run on the first 401; document or implement token refresh from a refresh token.

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

Return False (not replied) on 401 and abort the run on the first 401; document or implement token refresh from a refresh token.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/AUTOMATIONS.md (AUT-003). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: read automations/youtube_poller.py, .github/workflows/youtube-comment-poll.yml, worker/src/automations/routes.ts, worker/src/index.ts verifySchedulerSecret.
