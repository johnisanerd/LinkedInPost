---
id: 2026-10-27-b-h-1-prune-large-reference-clones-after-extraction-video-pipeline-ref
title: B-H-1 Prune large reference clones after extraction (`video-pipeline/reference/hyperframes` measured 1.4 GB in the local checkout on 2026-10-21; it is a nested Git checkout and appears untracked in the parent repo). Reproduce with `du -sh video-pipeline/reference/hyperframes` and `git status --short -- video-pipeline/reference/hyperframes`
created: '2026-10-27'
updated: '2026-10-27'
journeys: []
related: []
docs:
- docs/plans/video-pipeline/BACKLOG.md
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: improvement
area: video-pipeline/Housekeeping
raw_id: B-H-1
value: H
effort: S
---

## Problem

Prune large reference clones after extraction (`video-pipeline/reference/hyperframes` measured 1.4 GB in the local checkout on 2026-10-21; it is a nested Git checkout and appears untracked in the parent repo). Reproduce with `du -sh video-pipeline/reference/hyperframes` and `git status --short -- video-pipeline/reference/hyperframes`. Section: Housekeeping. Value H, effort S.

## Evidence and reproduction

- Source: docs/plans/video-pipeline/BACKLOG.md (B-H-1).
- Not a defect report; an improvement the owner already listed.

## Acceptance criteria

- The change named in the title is built, and its effect is measured against the trigger (if any).

## Plan

Decide scope when the trigger fires; record the decision in Attempts.

## Attempts

- 2026-10-27 — Imported from docs/plans/video-pipeline/BACKLOG.md into the ledger. No work started.

## Verification

Pending. Filed from the video-pipeline backlog as an improvement; nothing was built or checked here.
