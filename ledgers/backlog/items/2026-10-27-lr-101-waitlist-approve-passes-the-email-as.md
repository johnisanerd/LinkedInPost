---
id: 2026-10-27-lr-101-waitlist-approve-passes-the-email-as
title: Waitlist approve passes the email as the user id, so approving a person who never signed in updates zero user rows.
created: '2026-10-27'
updated: '2026-10-27'
journeys:
- 2026-10-27-j017-non-approved-google-account-signs-in
- 2026-10-27-j019-admin-approves-a-waitlist-entry
related: []
docs:
- worker/src/modes/saas/admin.ts
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: investigation
severity: P2
area: frontend/saas-admin
raw_id: LR-101
source_file: docs/launch-readiness/findings/REVIEW-ITEMS.md
---

## Problem

Waitlist approve passes the email as the user id, so approving a person who never signed in updates zero user rows. Suspected, not confirmed (see Confidence in the evidence).

## Evidence and reproduction

- **Confidence:** hypothesis
- **Journeys:** J-017, J-019
- **Aliases:** FEB-017, WKA-030 (approve path)
- **Evidence:** frontend/src/features/saas/AdminPanel.tsx (handleApprove(r.email)); worker/src/modes/saas/admin.ts:27-34
- **Repro:** approve a waitlist entry, then sign in as that person.
- **Fix hint:** Approve by access-request id or email via a route that creates or activates the user row.

## Acceptance criteria

- The question in the title is answered in Attempts with file:line evidence and a clear yes/no.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

Approve by access-request id or email via a route that creates or activates the user row.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/REVIEW-ITEMS.md (LR-101). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: hypothesis from static reading of frontend/src/features/saas/AdminPanel.tsx (handleApprove(r.email)); confirm by running the Repro and observing the described behaviour.
