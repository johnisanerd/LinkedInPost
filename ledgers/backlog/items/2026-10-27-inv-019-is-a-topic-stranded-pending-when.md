---
id: 2026-10-27-inv-019-is-a-topic-stranded-pending-when
title: Is a topic stranded Pending when the user leaves during Send to Generation? (FEA-004)
created: '2026-10-27'
updated: '2026-10-27'
journeys: []
related:
- 2026-10-27-lr-056-send-to-generation-navigates-away-without
docs:
- frontend/src/services/backendApi.ts
- worker/src/index.ts
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: investigation
severity: P1
area: worker/generation
raw_id: INV-019
source_file: docs/launch-readiness/findings/INVESTIGATE.md
---

## Problem

Is a topic stranded Pending when the user leaves during Send to Generation? (FEA-004). A topic could stay Pending forever with no refresh or error.

## Evidence and reproduction

- **Question:** The raw item is P1 with a hypothesis on worker-side cancellation: if the client navigates away, does the worker keep running and save a result?
- **Why it matters:** A topic could stay Pending forever with no refresh or error.
- **How to settle it:** Read frontend/src/services/backendApi.ts (sendTopicToGeneration) and worker/src/index.ts:1165-1270. To settle: click Send to Generation, navigate away at once, and watch the sheet row and the worker log.
- **Related items:** LR-056
- **Owner:**

## Acceptance criteria

- The question in the title is answered in Attempts with file:line evidence and a clear yes/no.

## Plan

Decide the fix first; record the decision in Attempts.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/INVESTIGATE.md (INV-019). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: not run; raw item flags the worker-side behaviour as a hypothesis. Covered by LR-056..
