---
id: 2026-10-27-lr-019-committed-owner-resource-ids-d1-kv
title: Committed owner resource ids (D1, KV, emails, client id, URL) make setup skip creation and fail migrations on any other Cloudflare account.
created: '2026-10-27'
updated: '2026-10-27'
journeys:
- 2026-10-27-j001-web-setup-wizard-end-to-end
- 2026-10-27-j002-headless-full-bootstrap-with-python-setup
- 2026-10-27-j003-fresh-cloudflare-account-against-the-committed
related:
- 2026-10-27-lr-134-default-admin-email-is-hard-coded
docs:
- setup/cloudflare.py
- setup.py
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: defect
severity: P1
area: deploy/config
raw_id: LR-019
source_file: docs/launch-readiness/findings/REVIEW-ITEMS.md
---

## Problem

Committed owner resource ids (D1, KV, emails, client id, URL) make setup skip creation and fail migrations on any other Cloudflare account.

## Evidence and reproduction

- **Confidence:** confirmed-by-reading
- **Journeys:** J-001..J-003
- **Aliases:** SET-011, ARCH-012 (owner data)
- **Evidence:** worker/wrangler.jsonc:10-20,52-65; setup/cloudflare.py:315-323
- **Repro:** static. Fresh Cloudflare account, `python setup.py --cloudflare`.
- **Fix hint:** Commit a template with placeholders and generate wrangler.jsonc, or verify ids via wrangler d1 info before trusting them.

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

Commit a template with placeholders and generate wrangler.jsonc, or verify ids via wrangler d1 info before trusting them.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/REVIEW-ITEMS.md (LR-019). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: static reading of worker/wrangler.jsonc:10-20,52-65.
