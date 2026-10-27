---
id: 2026-10-27-lr-191-the-process-wide-lifecycle-event-bus
title: The process-wide lifecycle event bus can leak node metadata between SSE streams, and handlers are not unsubscribed on early return.
created: '2026-10-27'
updated: '2026-10-27'
journeys:
- 2026-10-27-j053-generate-a-draft-from-the-queue
- 2026-10-27-j113-enrichment-page-and-node-catalog-admin
related: []
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
raw_id: LR-191
source_file: docs/launch-readiness/findings/REVIEW-ITEMS.md
---

## Problem

The process-wide lifecycle event bus can leak node metadata between SSE streams, and handlers are not unsubscribed on early return. Suspected, not confirmed (see Confidence in the evidence).

## Evidence and reproduction

- **Confidence:** hypothesis
- **Journeys:** J-053, J-113
- **Aliases:** WKA-037
- **Evidence:** worker/src/index.ts:859-873; worker/src/engine/events/LifecycleEventBus.ts:51
- **Repro:** static.
- **Fix hint:** Filter by a per-request run id and unsubscribe on every return.

## Acceptance criteria

- The question in the title is answered in Attempts with file:line evidence and a clear yes/no.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

Filter by a per-request run id and unsubscribe on every return.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/REVIEW-ITEMS.md (LR-191). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: hypothesis from static reading of worker/src/index.ts:859-873; confirm by running the Repro and observing the described behaviour.
