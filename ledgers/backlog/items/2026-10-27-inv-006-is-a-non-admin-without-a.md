---
id: 2026-10-27-inv-006-is-a-non-admin-without-a
title: Is a non-admin without a connected sheet locked out of everything? (J-031 vs FEB-003)
created: '2026-10-27'
updated: '2026-10-27'
journeys: []
related:
- 2026-10-27-lr-072-tenants-without-a-sheet-work-in
docs: []
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: investigation
severity: P0
area: frontend/tenancy
raw_id: INV-006
source_file: docs/launch-readiness/findings/INVESTIGATE.md
---

## Problem

Is a non-admin without a connected sheet locked out of everything? (J-031 vs FEB-003). If true, a new SaaS user who skipped the sheet step cannot reach Connections to fix it and the copy blames an admin who has nothing to do.

## Evidence and reproduction

- **Question:** J-031 is P0 (CORE); FEB-003 is a P1 hypothesis. Does the 'Workspace setup pending' wall block every route, including /connections, for a non-admin with no spreadsheetId?
- **Why it matters:** If true, a new SaaS user who skipped the sheet step cannot reach Connections to fix it and the copy blames an admin who has nothing to do.
- **How to settle it:** In frontend/src/components/dashboard/index.tsx read where the early return (line 581) sits relative to <Routes> and whether /connections is rendered by this component or by App.tsx (App.tsx:449-465). To settle: sign in as a fresh non-admin test user with no sheet and visit /connections directly.
- **Related items:** LR-072, J-031, FEB-003
- **Owner:**

## Acceptance criteria

- The question in the title is answered in Attempts with file:line evidence and a clear yes/no.

## Plan

Decide the fix first; record the decision in Attempts.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/INVESTIGATE.md (INV-006). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: code shows the pending wall at frontend/src/components/dashboard/index.tsx:581-595 for `!session.config.spreadsheetId && !session.isAdmin`. Whether it also covers /connections was not traced. Ledger follows FEB-003 severity (LR-072, P1)..
