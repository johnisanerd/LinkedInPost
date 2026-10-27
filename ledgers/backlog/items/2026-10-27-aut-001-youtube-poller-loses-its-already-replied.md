---
id: 2026-10-27-aut-001-youtube-poller-loses-its-already-replied
title: YouTube poller loses its "already replied" list on every CI run, so each run re-replies to every comment
created: '2026-10-27'
updated: '2026-10-27'
journeys: []
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
severity: P1
area: automations
raw_id: AUT-001
source_file: docs/launch-readiness/findings/AUTOMATIONS.md
---

## Problem

YouTube poller loses its "already replied" list on every CI run, so each run re-replies to every comment.

## Evidence and reproduction

- **Journeys:** none
- **Confidence:** confirmed-by-reading
- **Evidence:** automations/youtube_poller.py:19 stores replied IDs in `.youtube_replied_ids` in the working directory (load_replied line 140, save_replied line 152). .github/workflows/youtube-comment-poll.yml:17-31 checks out a fresh clone, runs the script, and has no cache or artifact step for that file, so the list is empty at the start of every run. The worker records only a poll timestamp (routes.ts:208), not reply IDs.
- **Repro:** Run the workflow twice against a channel with a comment rule: the second run posts a second reply under every top-level comment the first run answered.
- **Fix hint:** Persist the replied IDs between runs (actions/cache or a KV/D1 record through the worker) and skip any thread that already has a reply from the channel owner.

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

Persist the replied IDs between runs (actions/cache or a KV/D1 record through the worker) and skip any thread that already has a reply from the channel owner.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/AUTOMATIONS.md (AUT-001). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: read automations/youtube_poller.py, .github/workflows/youtube-comment-poll.yml, worker/src/automations/routes.ts, worker/src/index.ts verifySchedulerSecret.
