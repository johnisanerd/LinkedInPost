---
id: 2026-10-27-lr-066-newsletter-preview-and-approval-messages-can
title: 'Newsletter preview and approval messages can never be delivered: a client id is used as a Gmail token and an email as a Telegram chat id.'
created: '2026-10-27'
updated: '2026-10-27'
journeys:
- 2026-10-27-j110-draft-approve-and-send-a-newsletter
- 2026-10-27-j111-scheduled-newsletter-send-vs-a-once
related: []
docs:
- worker/src/newsletter/draftCreator.ts
- worker/src/newsletter/persistence.ts
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: defect
severity: P1
area: worker/newsletter
raw_id: LR-066
source_file: docs/launch-readiness/findings/REVIEW-ITEMS.md
---

## Problem

Newsletter preview and approval messages can never be delivered: a client id is used as a Gmail token and an email as a Telegram chat id.

## Evidence and reproduction

- **Confidence:** confirmed-by-reading
- **Journeys:** J-110, J-111
- **Aliases:** WKB-019, WKB-035
- **Evidence:** worker/src/newsletter/draftCreator.ts:242-291; worker/src/newsletter/persistence.ts:224-250
- **Repro:** static. Executor: create a newsletter with adminEmail set, trigger a draft, check the worker logs.
- **Fix hint:** Send previews with the admin stored integration token or a real chat id, or remove the preview promise and the auto-approve toggle.

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

Send previews with the admin stored integration token or a real chat id, or remove the preview promise and the auto-approve toggle.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/REVIEW-ITEMS.md (LR-066). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: static reading of worker/src/newsletter/draftCreator.ts:242-291.
