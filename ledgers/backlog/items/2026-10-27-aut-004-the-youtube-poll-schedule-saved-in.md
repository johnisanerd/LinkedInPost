---
id: 2026-10-27-aut-004-the-youtube-poll-schedule-saved-in
title: The YouTube poll schedule saved in the UI is never used; the workflow has no schedule and does not read it
created: '2026-10-27'
updated: '2026-10-27'
journeys: []
related: []
docs:
- worker/src/automations/routes.ts
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: defect
severity: P2
area: automations
raw_id: AUT-004
source_file: docs/launch-readiness/findings/AUTOMATIONS.md
---

## Problem

The YouTube poll schedule saved in the UI is never used; the workflow has no schedule and does not read it.

## Evidence and reproduction

- **Journeys:** none
- **Confidence:** confirmed-by-reading
- **Evidence:** The Automations page shows a cron field (frontend/src/features/automations/YouTubeScheduler.tsx:50, saved by PUT /automations/youtube/schedule in worker/src/automations/routes.ts:142-149 into KV) and the text "YouTube uses scheduled polling — no webhook registration needed." (frontend/src/features/automations, rendered for the youtube tab). .github/workflows/youtube-comment-poll.yml:9-11 has `# schedule:` and the cron commented out, "Disabled by default"; the only trigger is manual `workflow_dispatch` with a required channel_id. The workflow also reads the worker URL from `secrets.VITE_WORKER_URL` (line 29), a frontend variable name that setup does not document for this job, and the script's WORKER_SCHEDULER_SECRET is described as optional by main() (line 169 does not require it) although the worker rejects an empty one.
- **Repro:** Save a YouTube comment rule and a cron such as `0 */6 * * *` in /automations, wait: no replies are ever posted unless someone triggers the workflow by hand; with the secret unset the script prints "no active comment rule" (a 401 from the worker, swallowed at lines 55-57).
- **Fix hint:** Either have the workflow (or a worker cron) read the saved cron, or change the UI text to say the cron must be set in the workflow file; require WORKER_SCHEDULER_SECRET in main(), and print the HTTP status when the rule lookup fails.

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

Either have the workflow (or a worker cron) read the saved cron, or change the UI text to say the cron must be set in the workflow file; require WORKER_SCHEDULER_SECRET in main(), and print the HTTP status when the rule lookup fails.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/AUTOMATIONS.md (AUT-004). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: read automations/youtube_poller.py, .github/workflows/youtube-comment-poll.yml, worker/src/automations/routes.ts, worker/src/index.ts verifySchedulerSecret.
