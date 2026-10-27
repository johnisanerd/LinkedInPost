---
id: 2026-10-27-lr-011-the-email-newsletter-send-is-a
title: The email newsletter send is a stub that logs a TODO and marks the issue sent, so nothing is delivered while the user is told it shipped.
created: '2026-10-27'
updated: '2026-10-27'
journeys:
- 2026-10-27-j110-draft-approve-and-send-a-newsletter
- 2026-10-27-j111-scheduled-newsletter-send-vs-a-once
related: []
docs:
- worker/src/newsletter/scheduler.ts
- worker/src/newsletter/handlers.ts
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: defect
severity: P0
area: worker/newsletter
raw_id: LR-011
source_file: docs/launch-readiness/findings/REVIEW-ITEMS.md
---

## Problem

The email newsletter send is a stub that logs a TODO and marks the issue sent, so nothing is delivered while the user is told it shipped.

## Evidence and reproduction

- **Confidence:** confirmed-by-reading
- **Journeys:** J-110, J-111
- **Aliases:** WKB-005, WKA-024 (email branch)
- **Evidence:** worker/src/newsletter/scheduler.ts:91-101; worker/src/newsletter/handlers.ts:63-90
- **Repro:** static. Executor: create a newsletter with emailRecipients, approve an issue, call `newsletter.sendApproved`; check status = `sent` and Gmail Sent folder is empty.
- **Fix hint:** Implement the Gmail send with a per-user token, or fail loudly and leave the issue approved (block creating email newsletters).

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

Implement the Gmail send with a per-user token, or fail loudly and leave the issue approved (block creating email newsletters).

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/REVIEW-ITEMS.md (LR-011). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: static reading of worker/src/newsletter/scheduler.ts:91-101.
