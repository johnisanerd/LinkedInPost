---
id: 2026-10-27-inv-004-is-an-empty-admin-emails-an
title: Is an empty ADMIN_EMAILS an owner-admin P0 or a P2? (J-127 vs ARCH-012)
created: '2026-10-27'
updated: '2026-10-27'
journeys: []
related:
- 2026-10-27-lr-134-default-admin-email-is-hard-coded
docs:
- worker/src/index.ts
- setup/worker_config.py
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: investigation
severity: P0
area: worker/auth
raw_id: INV-004
source_file: docs/launch-readiness/findings/INVESTIGATE.md
---

## Problem

Is an empty ADMIN_EMAILS an owner-admin P0 or a P2? (J-127 vs ARCH-012). On a customer or fork deployment missing the variable, the project author gets admin over that tenant. Severity decides whether it blocks launch.

## Evidence and reproduction

- **Question:** The journey designer rates J-127 P0 (CORE) because an empty ADMIN_EMAILS makes 99pratyush@gmail.com admin on any deployment. ARCH-012 and LR-134 rate it P2. Which severity is right?
- **Why it matters:** On a customer or fork deployment missing the variable, the project author gets admin over that tenant. Severity decides whether it blocks launch.
- **How to settle it:** Read worker/src/index.ts:3020-3027 (resolveAdminEmailAllowlist). Decide whether launch is single-owner (then P2) or hands the repo to customers (then P0). To settle: deploy to a fresh test Worker with ADMIN_EMAILS unset and sign in as the default address; also check setup/worker_config.py always writes ADMIN_EMAILS.
- **Related items:** LR-134, J-127, ARCH-012
- **Owner:**

## Acceptance criteria

- The question in the title is answered in Attempts with file:line evidence and a clear yes/no.

## Plan

Decide the fix first; record the decision in Attempts.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/INVESTIGATE.md (INV-004). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: code confirms the fallback: resolveAdminEmailAllowlist returns [DEFAULT_ADMIN_EMAIL = '99pratyush@gmail.com'] when ADMIN_EMAILS is empty (worker/src/index.ts:3020-3027). The code comment calls it intentional ('never treat every user as admin'). Ledger follows the finding severity (LR-134, P2); the owner decides the severity..
