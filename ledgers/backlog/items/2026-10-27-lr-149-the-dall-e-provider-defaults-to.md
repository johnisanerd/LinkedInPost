---
id: 2026-10-27-lr-149-the-dall-e-provider-defaults-to
title: The dall-e provider defaults to gpt-image-1 but reads url instead of b64_json and uses DALL-E 3 sizes, and the Stability 4:3 ratio is invalid.
created: '2026-10-27'
updated: '2026-10-27'
journeys:
- 2026-10-27-j068-ai-image-generation-text-and-reference
related: []
docs:
- worker/src/image-gen/providers/dall-e.ts
- worker/src/image-gen/providers/stability.ts
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: investigation
severity: P2
area: worker/image-gen
raw_id: LR-149
source_file: docs/launch-readiness/findings/REVIEW-ITEMS.md
---

## Problem

The dall-e provider defaults to gpt-image-1 but reads url instead of b64_json and uses DALL-E 3 sizes, and the Stability 4:3 ratio is invalid. Suspected, not confirmed (see Confidence in the evidence).

## Evidence and reproduction

- **Confidence:** hypothesis
- **Journeys:** J-068
- **Aliases:** WKB-027
- **Evidence:** worker/src/image-gen/providers/dall-e.ts:4-15; worker/src/image-gen/providers/stability.ts:4-12
- **Repro:** static; executor: configure provider `dall-e`, no model, call `generateImageFromText`.
- **Fix hint:** Handle b64_json, set sizes per model, map unsupported aspect ratios; confirm with a live call.

## Acceptance criteria

- The question in the title is answered in Attempts with file:line evidence and a clear yes/no.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

Handle b64_json, set sizes per model, map unsupported aspect ratios; confirm with a live call.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/REVIEW-ITEMS.md (LR-149). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: hypothesis from static reading of worker/src/image-gen/providers/dall-e.ts:4-15; confirm by running the Repro and observing the described behaviour.
