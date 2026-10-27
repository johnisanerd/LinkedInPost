---
id: 2026-10-27-hyg-003-a-tracked-dev-env-file-holds
title: A tracked dev env file holds an auth-bypass secret key
created: '2026-10-27'
updated: '2026-10-27'
journeys:
- 2026-10-27-j136-dev-auth-bypass-secret-present-in
related:
- 2026-10-27-lr-001-the-e2e-dev-auth-bypass-secret
docs:
- frontend/.env.development
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: hygiene
severity: P1
area: frontend/.env.development
raw_id: HYG-003
source_file: docs/launch-readiness/findings/HYGIENE.md
---

## Problem

A tracked dev env file holds an auth-bypass secret key.

## Evidence and reproduction

- **Journeys:** J-136
- **Confidence:** confirmed-by-reading
- **Evidence:** frontend/.env.development is tracked (`git ls-files | grep env.development` lists it). Its keys include VITE_DEV_GOOGLE_AUTH_BYPASS_SECRET and VITE_DEV_GOOGLE_AUTH_BYPASS. The value is not recorded in this file. ARCH-AUDIT.md said .gitignore covers .env; it does not cover .env.development, so this file was missed.
- **Repro:** `git ls-files frontend/.env.development` shows the file; `sed 's/=.*/=<redacted>/' frontend/.env.development` shows the keys.
- **Fix hint:** untrack the file (`git rm --cached`) and ignore `.env.*` except `.env.example`. Check whether the committed value equals any production worker secret; if it does, rotate both. Also see LR-001, which covers the production bypass secret.

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

untrack the file (`git rm --cached`) and ignore `.env.*` except `.env.example`. Check whether the committed value equals any production worker secret; if it does, rotate both. Also see LR-001, which covers the production bypass secret.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/HYGIENE.md (HYG-003). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: checked by reading the cited file and git ls-files.
