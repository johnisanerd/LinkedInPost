---
id: 2026-10-27-aut-005-poller-spends-youtube-quota-on-every
title: Poller spends YouTube quota on every run (search.list per page plus a comment fetch per video)
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
type: investigation
severity: P3
area: automations
raw_id: AUT-005
source_file: docs/launch-readiness/findings/AUTOMATIONS.md
---

## Problem

Poller spends YouTube quota on every run (search.list per page plus a comment fetch per video). Suspected, not confirmed (see Confidence in the evidence).

## Evidence and reproduction

- **Journeys:** none
- **Confidence:** hypothesis
- **Evidence:** youtube_poller.py:183-211 pages search.list (100 quota units per call) over all videos and lines 217-252 call commentThreads for every video on every run, plus comments.insert (about 50 units) per reply. With the default 10,000 units per day, a six-hourly schedule on a large channel can exhaust quota, after which 403 responses are retried forever (lines 101-108).
- **Repro:** Static check only: count the calls per run for a channel with more than 100 videos; not run against the YouTube API.
- **Fix hint:** Use the channel's uploads playlist (playlistItems.list, 1 unit) and stop paging once videos older than the last poll are reached.

## Acceptance criteria

- The question in the title is answered in Attempts with file:line evidence and a clear yes/no.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

Use the channel's uploads playlist (playlistItems.list, 1 unit) and stop paging once videos older than the last poll are reached.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/AUTOMATIONS.md (AUT-005). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: read automations/youtube_poller.py, .github/workflows/youtube-comment-poll.yml, worker/src/automations/routes.ts, worker/src/index.ts verifySchedulerSecret.
