---
id: 2026-10-27-lr-141-all-connection-disconnect-and-settings-writes
title: All connection, disconnect and settings writes are whole-object read-modify-write on one KV key with no versioning, losing concurrent updates.
created: '2026-10-27'
updated: '2026-10-27'
journeys:
- 2026-10-27-j094-connect-linkedin-popup-oauth
- 2026-10-27-j096-connect-gmail
- 2026-10-27-j102-disconnect-a-channel-three-different-disconnect
- 2026-10-27-j105-stored-token-can-no-longer-be
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
severity: P2
area: worker/config
raw_id: LR-141
source_file: docs/launch-readiness/findings/REVIEW-ITEMS.md
---

## Problem

All connection, disconnect and settings writes are whole-object read-modify-write on one KV key with no versioning, losing concurrent updates.

## Evidence and reproduction

- **Confidence:** confirmed-by-reading
- **Journeys:** J-094, J-096, J-102, J-105
- **Aliases:** WKA-017
- **Evidence:** worker/src/index.ts:4221,4286,4745,5003,5127
- **Repro:** static; low-probability race.
- **Fix hint:** Split per-feature records into separate keys or D1 rows and write only the changed key.

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

Split per-feature records into separate keys or D1 rows and write only the changed key.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/REVIEW-ITEMS.md (LR-141). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: static reading of worker/src/index.ts:4221,4286,4745,5003,5127.
