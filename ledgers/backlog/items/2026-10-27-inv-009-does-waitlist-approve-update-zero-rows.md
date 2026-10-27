---
id: 2026-10-27-inv-009-does-waitlist-approve-update-zero-rows
title: Does waitlist approve update zero rows because it passes the email as the user id? (FEB-017)
created: '2026-10-27'
updated: '2026-10-27'
journeys: []
related:
- 2026-10-27-lr-101-waitlist-approve-passes-the-email-as
docs:
- worker/src/db/users.ts
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: investigation
severity: P2
area: frontend/saas-admin
raw_id: INV-009
source_file: docs/launch-readiness/findings/INVESTIGATE.md
---

## Problem

Does waitlist approve update zero rows because it passes the email as the user id? (FEB-017). Approving someone who never signed in would silently do nothing and the person stays blocked.

## Evidence and reproduction

- **Question:** The admin panel calls approve with r.email, and the worker does setUserStatus(db, userId, 'active') with that value. Is users.id an email or a Google sub?
- **Why it matters:** Approving someone who never signed in would silently do nothing and the person stays blocked.
- **How to settle it:** Read worker/src/db/users.ts (id column and setUserStatus) and the access_requests table. To settle: add a pending request for a test email, approve it from /admin, then check the users and access_requests rows.
- **Related items:** LR-101
- **Owner:**

## Acceptance criteria

- The question in the title is answered in Attempts with file:line evidence and a clear yes/no.

## Plan

Decide the fix first; record the decision in Attempts.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/INVESTIGATE.md (INV-009). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: code: worker/src/modes/saas/admin.ts:27-34 approve takes the path segment as userId and calls setUserStatus and resolveAccessRequest with it. What users.id holds was not checked. Covered by LR-101..
