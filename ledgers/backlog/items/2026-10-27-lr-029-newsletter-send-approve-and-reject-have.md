---
id: 2026-10-27-lr-029-newsletter-send-approve-and-reject-have
title: Newsletter Send, Approve and Reject have no confirmation, no per-issue pending state and swallow errors
created: '2026-10-27'
updated: '2026-10-27'
journeys:
- 2026-10-27-j109-create-a-newsletter-and-preview-it
- 2026-10-27-j110-draft-approve-and-send-a-newsletter
related: []
docs: []
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: defect
severity: P1
area: frontend/newsletter
raw_id: LR-029
source_file: docs/launch-readiness/findings/REVIEW-ITEMS.md
---

## Problem

Newsletter Send, Approve and Reject have no confirmation, no per-issue pending state and swallow errors.

## Evidence and reproduction

- **Confidence:** confirmed-by-reading
- **Journeys:** J-109, J-110
- **Aliases:** FEB-008
- **Evidence:** frontend/src/features/campaign/components/newsletter/NewsletterDashboard.tsx:229-260
- **Repro:** click Send on an approved issue with the worker returning an error; no feedback. Static reasoning.
- **Fix hint:** Add a confirm dialog with recipient count, per-issue pending state and show the thrown error.

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

Add a confirm dialog with recipient count, per-issue pending state and show the thrown error.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/REVIEW-ITEMS.md (LR-029). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: static reading of frontend/src/features/campaign/components/newsletter/NewsletterDashboard.tsx:229-260.
