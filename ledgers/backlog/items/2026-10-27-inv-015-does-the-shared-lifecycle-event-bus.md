---
id: 2026-10-27-inv-015-does-the-shared-lifecycle-event-bus
title: Does the shared lifecycle event bus leak node metadata between users? (WKA-037)
created: '2026-10-27'
updated: '2026-10-27'
journeys: []
related:
- 2026-10-27-lr-191-the-process-wide-lifecycle-event-bus
docs:
- worker/src/index.ts
- worker/src/engine/events/LifecycleEventBus.ts
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: investigation
severity: P3
area: worker/generation
raw_id: INV-015
source_file: docs/launch-readiness/findings/INVESTIGATE.md
---

## Problem

Does the shared lifecycle event bus leak node metadata between users? (WKA-037). Another user's node ids and durations could appear in a stream; handlers may leak on early return.

## Evidence and reproduction

- **Question:** lifecycleEventBus is a module singleton and each /api/generate/stream request subscribes with no run or user filter. Is it also contradicted by WKB-044 (engine never run)?
- **Why it matters:** Another user's node ids and durations could appear in a stream; handlers may leak on early return.
- **How to settle it:** Read worker/src/index.ts:859-890 and worker/src/engine/events/LifecycleEventBus.ts:51; check whether the engine runs in production (WKB-044). To settle: run two concurrent generations on a local worker and compare the streamed events.
- **Related items:** LR-191
- **Owner:**

## Acceptance criteria

- The question in the title is answered in Attempts with file:line evidence and a clear yes/no.

## Plan

Decide the fix first; record the decision in Attempts.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/INVESTIGATE.md (INV-015). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: not re-read in this pass; the raw review and WKB-044 disagree on whether the engine runs. Covered by LR-191..
