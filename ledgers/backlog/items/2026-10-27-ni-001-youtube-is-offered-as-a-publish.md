---
id: 2026-10-27-ni-001-youtube-is-offered-as-a-publish
title: YouTube is offered as a publish channel, but publishing rejects it with "Unsupported delivery channel"
created: '2026-10-27'
updated: '2026-10-27'
journeys:
- 2026-10-27-j081-youtube-as-a-publish-target
related: []
docs:
- worker/src/index.ts
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: hygiene
severity: P2
area: worker/youtube
raw_id: NI-001
source_file: docs/launch-readiness/findings/HYGIENE.md
---

## Problem

YouTube is offered as a publish channel, but publishing rejects it with "Unsupported delivery channel".

## Evidence and reproduction

- **Journeys:** J-081
- **Confidence:** confirmed-by-reading
- **Evidence:** worker/src/index.ts:129 (ChannelId includes youtube); worker/src/index.ts:5365-5375 (coerceChannelId accepts only instagram, linkedin, telegram, whatsapp, gmail and throws otherwise); worker/src/index.ts:4841 (publish calls coerceChannelId).
- **Repro:** POST /action with channel "youtube" to a publish action; expect the error "Unsupported delivery channel."
- **Fix hint:** decide: either implement YouTube publish or remove YouTube from the publish channel choices in the UI. The choice is a product decision, so it is an owner question first.

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

decide: either implement YouTube publish or remove YouTube from the publish channel choices in the UI. The choice is a product decision, so it is an owner question first.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/HYGIENE.md (NI-001). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: checked by reading the cited file and git ls-files.
