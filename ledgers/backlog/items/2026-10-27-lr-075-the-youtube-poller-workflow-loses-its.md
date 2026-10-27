---
id: 2026-10-27-lr-075-the-youtube-poller-workflow-loses-its
title: The YouTube poller workflow loses its already-replied state on every run, causing duplicate replies, and its schedule block is commented out.
created: '2026-10-27'
updated: '2026-10-27'
journeys:
- 2026-10-27-j118-youtube-comment-polling-schedule
related: []
docs:
- automations/youtube_poller.py
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: defect
severity: P2
area: automations
raw_id: LR-075
source_file: docs/launch-readiness/findings/REVIEW-ITEMS.md
---

## Problem

The YouTube poller workflow loses its already-replied state on every run, causing duplicate replies, and its schedule block is commented out.

## Evidence and reproduction

- **Confidence:** confirmed-by-reading
- **Journeys:** J-118
- **Aliases:** SET-032
- **Evidence:** .github/workflows/youtube-comment-poll.yml:13-31; automations/youtube_poller.py:19,140-159
- **Repro:** static; dispatch twice with the same channel.
- **Fix hint:** Persist replied ids in the worker (KV/D1) or restore and save the file via actions/cache.

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

Persist replied ids in the worker (KV/D1) or restore and save the file via actions/cache.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/REVIEW-ITEMS.md (LR-075). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: static reading of .github/workflows/youtube-comment-poll.yml:13-31.
