---
id: 2026-10-27-lr-001-the-e2e-dev-auth-bypass-secret
title: The E2E/dev auth-bypass secret ships in the public Pages bundle and is pushed to the production worker, so anyone can forge a login.
created: '2026-10-27'
updated: '2026-10-27'
journeys:
- 2026-10-27-j012-dev-auth-bypass-for-local-work
- 2026-10-27-j015-approved-user-signs-in-self-hosted
- 2026-10-27-j027-admin-only-screens-and-actions-are
- 2026-10-27-j136-dev-auth-bypass-secret-present-in
related: []
docs:
- worker/src/plugins/dev-google-auth-bypass/resolve-session.ts
- setup/worker_config.py
- setup/cloudflare.py
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: defect
severity: P0
area: deploy/auth
raw_id: LR-001
source_file: docs/launch-readiness/findings/REVIEW-ITEMS.md
---

## Problem

The E2E/dev auth-bypass secret ships in the public Pages bundle and is pushed to the production worker, so anyone can forge a login.

## Evidence and reproduction

- **Confidence:** confirmed-by-reading
- **Journeys:** J-012, J-015, J-027, J-136
- **Aliases:** ARCH-001, FEB-001, SET-006, FEB-026
- **Evidence:** .github/workflows/deploy-pages.yml:51-52; worker/src/plugins/dev-google-auth-bypass/resolve-session.ts:20-36
- **Repro:** static reasoning. Build with the secret set, grep `frontend/dist/assets/*.js` for the value, POST `{action:"bootstrap",idToken:"<value>"}` to the worker.
- **Fix hint:** Remove VITE_E2E_BYPASS_SECRET from deploy-pages.yml, stop pushing DEV_GOOGLE_AUTH_BYPASS_SECRET as a prod worker secret (setup/worker_config.py:270-283, setup/cloudflare.py:156-175), gate the bypass on import.meta.env.DEV; use a separate staging worker for cloud E2E.

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

Remove VITE_E2E_BYPASS_SECRET from deploy-pages.yml, stop pushing DEV_GOOGLE_AUTH_BYPASS_SECRET as a prod worker secret (setup/worker_config.py:270-283, setup/cloudflare.py:156-175), gate the bypass on import.meta.env.DEV; use a separate staging worker for cloud E2E.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/REVIEW-ITEMS.md (LR-001). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: static reading of .github/workflows/deploy-pages.yml:51-52.
