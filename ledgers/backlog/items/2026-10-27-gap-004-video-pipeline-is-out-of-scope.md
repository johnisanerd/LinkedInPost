---
id: 2026-10-27-gap-004-video-pipeline-is-out-of-scope
title: video-pipeline/ is out of scope
created: '2026-10-27'
updated: '2026-10-27'
journeys: []
related: []
docs:
- video-pipeline/direction/skills/LEDGER.yaml
- docs/plans/video-pipeline/BACKLOG.md
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: process
severity: P3
area: process/review
raw_id: GAP-004
source_file: docs/launch-readiness/findings/GAPS.md
---

## Problem

video-pipeline/ is out of scope.

## Evidence and reproduction

- **Gap:** video-pipeline/ is a separate product with vendored submodules (.gitmodules lists ViMax, MoneyPrinterTurbo, youtube-automation-agent, remotion) and its own ledger (video-pipeline/direction/skills/LEDGER.yaml) and backlog (docs/plans/video-pipeline/BACKLOG.md). It was not reviewed.
- **Action:** The owner decides whether it gets its own launch-release.
- **Owner:**

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.

## Plan

Decide the fix first; record the decision in Attempts.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/GAPS.md (GAP-004). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: checked that .gitmodules, video-pipeline/direction/skills/LEDGER.yaml and docs/plans/video-pipeline/BACKLOG.md exist..
