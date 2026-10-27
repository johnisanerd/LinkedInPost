---
id: 2026-10-27-lr-134-default-admin-email-is-hard-coded
title: DEFAULT_ADMIN_EMAIL is hard-coded to the owner, so a fork with empty ADMIN_EMAILS makes the original owner admin
created: '2026-10-27'
updated: '2026-10-27'
journeys:
- 2026-10-27-j003-fresh-cloudflare-account-against-the-committed
- 2026-10-27-j127-empty-admin-emails-makes-the-repo
related: []
docs:
- worker/src/index.ts
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: defect
severity: P2
area: worker/auth
raw_id: LR-134
source_file: docs/launch-readiness/findings/REVIEW-ITEMS.md
---

## Problem

DEFAULT_ADMIN_EMAIL is hard-coded to the owner, so a fork with empty ADMIN_EMAILS makes the original owner admin.

## Evidence and reproduction

- **Confidence:** confirmed-by-reading
- **Journeys:** J-003, J-127
- **Aliases:** ARCH-012 (admin fallback)
- **Evidence:** worker/src/index.ts:3020-3027
- **Repro:** (static check) Open worker/src/index.ts:3020-3027 and confirm the behaviour described in the summary; then exercise the matching journey (J-003, J-127) to observe it.
- **Fix hint:** Remove the fallback and fail closed when ADMIN_EMAILS is empty.

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

Remove the fallback and fail closed when ADMIN_EMAILS is empty.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/REVIEW-ITEMS.md (LR-134). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: static reading of worker/src/index.ts:3020-3027.
