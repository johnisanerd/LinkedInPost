---
id: 2026-10-27-inv-011-do-the-dall-e-and-stability
title: Do the dall-e and Stability providers return usable images with default settings? (WKB-027)
created: '2026-10-27'
updated: '2026-10-27'
journeys: []
related:
- 2026-10-27-lr-149-the-dall-e-provider-defaults-to
docs:
- worker/src/image-gen/providers/dall-e.ts
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: investigation
severity: P2
area: worker/image-gen
raw_id: INV-011
source_file: docs/launch-readiness/findings/INVESTIGATE.md
---

## Problem

Do the dall-e and Stability providers return usable images with default settings? (WKB-027). Image generation would throw after billing for users with default settings.

## Evidence and reproduction

- **Question:** Default model is gpt-image-1, which returns b64_json not url; sizes are DALL-E 3 sizes; Stability 4:3 is claimed invalid.
- **Why it matters:** Image generation would throw after billing for users with default settings.
- **How to settle it:** Read worker/src/image-gen/providers/dall-e.ts:4-15 and stability.ts:4-12, check current provider API docs, then call generateImageFromText once per provider with a test key.
- **Related items:** LR-149
- **Owner:**

## Acceptance criteria

- The question in the title is answered in Attempts with file:line evidence and a clear yes/no.

## Plan

Decide the fix first; record the decision in Attempts.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/INVESTIGATE.md (INV-011). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: API facts come from the raw review and were not checked here. Covered by LR-149..
