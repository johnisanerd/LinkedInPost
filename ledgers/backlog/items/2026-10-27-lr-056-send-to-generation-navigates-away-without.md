---
id: 2026-10-27-lr-056-send-to-generation-navigates-away-without
title: Send to Generation navigates away without consuming the stream, flips status non-atomically, and never saves results or recovers from errors.
created: '2026-10-27'
updated: '2026-10-27'
journeys:
- 2026-10-27-j053-generate-a-draft-from-the-queue
- 2026-10-27-j054-network-drop-in-the-middle-of
- 2026-10-27-j055-generation-worker-down-mis-secreted-or
- 2026-10-27-j056-send-to-generation-button-on-a
related: []
docs:
- worker/src/index.ts
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: defect
severity: P1
area: worker/generation
raw_id: LR-056
source_file: docs/launch-readiness/findings/REVIEW-ITEMS.md
---

## Problem

Send to Generation navigates away without consuming the stream, flips status non-atomically, and never saves results or recovers from errors.

## Evidence and reproduction

- **Confidence:** confirmed-by-reading
- **Journeys:** J-053..J-056
- **Aliases:** FEA-004, WKA-013, WKB-017
- **Evidence:** frontend/src/components/dashboard/components/TopicPostPreviewCard.tsx:62-66; worker/src/index.ts:1165-1268
- **Repro:** Create a Draft topic, click "Send to Generation", then watch the variants page: it stays on the pending view; kill the generation worker beforehand and confirm no error is shown and status stays Pending.
- **Fix hint:** Claim with UPDATE ... WHERE status=Draft, persist the completed result server-side under ctx.waitUntil, emit an error event and revert to Draft on failure, and read the stream or poll on the client.

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

Claim with UPDATE ... WHERE status=Draft, persist the completed result server-side under ctx.waitUntil, emit an error event and revert to Draft on failure, and read the stream or poll on the client.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/REVIEW-ITEMS.md (LR-056). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: static reading of frontend/src/components/dashboard/components/TopicPostPreviewCard.tsx:62-66.
