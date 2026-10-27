---
id: 2026-10-27-aut-002-first-run-auto-replies-to-every
title: First run auto-replies to every historic comment on every video, with no recency limit or dry run
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
severity: P1
area: automations
raw_id: AUT-002
source_file: docs/launch-readiness/findings/AUTOMATIONS.md
---

## Problem

First run auto-replies to every historic comment on every video, with no recency limit or dry run.

## Evidence and reproduction

- **Journeys:** none
- **Confidence:** confirmed-by-reading
- **Evidence:** The docstring says "recent comments" (youtube_poller.py:3), but main() pages `search` over all channel videos (lines 183-211) and `commentThreads` over all pages of each video (lines 225-252) and calls post_reply for each thread not in the replied set (lines 237-244). There is no date cutoff, no per-run cap, no skip for the owner's own comments, and no confirm or dry-run switch.
- **Repro:** Enable a comment rule with a template, run the workflow on a channel with a few hundred old comments: every one gets the template reply in one run.
- **Fix hint:** Add a publishedAfter cutoff (for example the last recorded poll time), a per-run reply cap, skip comments authored by the channel itself, and a `DRY_RUN=1` mode that only prints what it would send.

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

Add a publishedAfter cutoff (for example the last recorded poll time), a per-run reply cap, skip comments authored by the channel itself, and a `DRY_RUN=1` mode that only prints what it would send.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/AUTOMATIONS.md (AUT-002). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: read automations/youtube_poller.py, .github/workflows/youtube-comment-poll.yml, worker/src/automations/routes.ts, worker/src/index.ts verifySchedulerSecret.
