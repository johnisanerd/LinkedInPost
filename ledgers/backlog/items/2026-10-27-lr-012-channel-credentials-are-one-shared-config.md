---
id: 2026-10-27-lr-012-channel-credentials-are-one-shared-config
title: 'Channel credentials are one shared config: publish falls back to the owner token for users without one, and any user connecting overwrites it.'
created: '2026-10-27'
updated: '2026-10-27'
journeys:
- 2026-10-27-j076-publish-now-to-linkedin
- 2026-10-27-j077-publish-to-instagram-image-required
- 2026-10-27-j078-send-via-gmail
- 2026-10-27-j079-send-via-whatsapp
- 2026-10-27-j080-send-via-telegram
- 2026-10-27-j090-publish-fails-because-the-channel-token
- 2026-10-27-j094-connect-linkedin-popup-oauth
- 2026-10-27-j095-connect-instagram
- 2026-10-27-j096-connect-gmail
- 2026-10-27-j103-a-user-with-no-linkedin-connection
- 2026-10-27-j140-tenant-a-cannot-read-or-modify
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
severity: P0
area: worker/publish
raw_id: LR-012
source_file: docs/launch-readiness/findings/REVIEW-ITEMS.md
---

## Problem

Channel credentials are one shared config: publish falls back to the owner token for users without one, and any user connecting overwrites it.

## Evidence and reproduction

- **Confidence:** confirmed-by-reading
- **Journeys:** J-076..J-080, J-090, J-094..J-096, J-103, J-140
- **Aliases:** WKA-001, WKB-002
- **Evidence:** worker/src/index.ts:4986-5011 (LinkedIn shared-token fallback); worker/src/index.ts:3092,3148-3170 (single shared-config key)
- **Repro:** static reasoning. Executor: admin connects LinkedIn; user B (no connection) calls `publishContent` channel `linkedin`; observe the post on the admin's profile. Then user B connects; user C without a connection now posts as B.
- **Fix hint:** Publish only with the caller social_integrations row and throw connect-your-account when absent or undecryptable; stop calling persist*Connection from user OAuth callbacks; keep shared channels admin-only.

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

Publish only with the caller social_integrations row and throw connect-your-account when absent or undecryptable; stop calling persist*Connection from user OAuth callbacks; keep shared channels admin-only.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/REVIEW-ITEMS.md (LR-012). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: static reading of worker/src/index.ts:4986-5011 (LinkedIn shared-token fallback).
