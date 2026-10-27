---
id: 2026-10-27-lr-057-quick-change-and-preview-endpoints-accept
title: Quick change and preview endpoints accept truncated or off-schema model output, or echo the original text, as the replacement.
created: '2026-10-27'
updated: '2026-10-27'
journeys:
- 2026-10-27-j065-quick-change-via-sse
- 2026-10-27-j066-variants-preview-for-a-selection
related: []
docs:
- worker/src/generation/normalize.ts
- generation-worker/src/preview.ts
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: defect
severity: P1
area: worker/generation
raw_id: LR-057
source_file: docs/launch-readiness/findings/REVIEW-ITEMS.md
---

## Problem

Quick change and preview endpoints accept truncated or off-schema model output, or echo the original text, as the replacement.

## Evidence and reproduction

- **Confidence:** confirmed-by-reading
- **Journeys:** J-065, J-066
- **Aliases:** WKB-023, GWP-020
- **Evidence:** worker/src/generation/normalize.ts:19-76; generation-worker/src/preview.ts:54-71,110-116
- **Repro:** static; executor: set maxOutputTokens tiny or mock a refusal.
- **Fix hint:** Ask for {text} consistently and read result.text, throw when empty instead of echoing the input, fail when parsing fails or finishReason is not STOP.

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

Ask for {text} consistently and read result.text, throw when empty instead of echoing the input, fail when parsing fails or finishReason is not STOP.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/REVIEW-ITEMS.md (LR-057). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: static reading of worker/src/generation/normalize.ts:19-76.
