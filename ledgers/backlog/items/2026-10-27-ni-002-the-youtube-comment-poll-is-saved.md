---
id: 2026-10-27-ni-002-the-youtube-comment-poll-is-saved
title: The YouTube comment poll is saved in the UI but its schedule is commented out in the workflow
created: '2026-10-27'
updated: '2026-10-27'
journeys:
- 2026-10-27-j118-youtube-comment-polling-schedule
related: []
docs: []
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: hygiene
severity: P2
area: ci/youtube
raw_id: NI-002
source_file: docs/launch-readiness/findings/HYGIENE.md
---

## Problem

The YouTube comment poll is saved in the UI but its schedule is commented out in the workflow.

## Evidence and reproduction

- **Journeys:** J-118
- **Confidence:** confirmed-by-reading
- **Evidence:** .github/workflows/youtube-comment-poll.yml:9-11 (the schedule block, including the cron line, is commented out with "Disabled by default").
- **Repro:** save a YouTube poll cron in the UI, then check the Actions tab: no scheduled run appears.
- **Fix hint:** either enable the schedule in the workflow when the UI saves a cron, or show the user that polling is manual-only. Decide which; do not hide the setting.

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

either enable the schedule in the workflow when the UI saves a cron, or show the user that polling is manual-only. Decide which; do not hide the setting.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/HYGIENE.md (NI-002). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: checked by reading the cited file and git ls-files.
