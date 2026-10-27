---
id: 2026-10-27-lr-010-newsletter-by-id-actions-approve-send
title: Newsletter by-id actions (approve, send, update, delete, regenerate, issue.update) have no tenant or ownership check
created: '2026-10-27'
updated: '2026-10-27'
journeys:
- 2026-10-27-j109-create-a-newsletter-and-preview-it
- 2026-10-27-j110-draft-approve-and-send-a-newsletter
- 2026-10-27-j112-newsletter-actions-are-not-tenant-scoped
- 2026-10-27-j140-tenant-a-cannot-read-or-modify
related: []
docs:
- worker/src/newsletter/handlers.ts
- worker/src/newsletter/persistence.ts
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: defect
severity: P0
area: worker/newsletter
raw_id: LR-010
source_file: docs/launch-readiness/findings/REVIEW-ITEMS.md
---

## Problem

Newsletter by-id actions (approve, send, update, delete, regenerate, issue.update) have no tenant or ownership check.

## Evidence and reproduction

- **Confidence:** confirmed-by-reading
- **Journeys:** J-109, J-110, J-112, J-140
- **Aliases:** WKA-004, WKB-006
- **Evidence:** worker/src/newsletter/handlers.ts:69,83,136,189; worker/src/newsletter/persistence.ts:150,165-196
- **Repro:** static. Executor: tenant A creates a newsletter; tenant B calls `newsletter.delete` with A's id.
- **Fix hint:** Load the row and compare spreadsheet_id (or add user_id) with the caller in one shared helper used by all by-id handlers; assert changes > 0.

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

Load the row and compare spreadsheet_id (or add user_id) with the caller in one shared helper used by all by-id handlers; assert changes > 0.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/REVIEW-ITEMS.md (LR-010). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: static reading of worker/src/newsletter/handlers.ts:69,83,136,189.
