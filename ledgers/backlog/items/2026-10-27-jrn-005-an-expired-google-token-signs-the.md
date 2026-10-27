---
id: 2026-10-27-jrn-005-an-expired-google-token-signs-the
title: An expired Google token signs the user out and unmounts the dashboard, so unsaved editor text can be lost
created: '2026-10-27'
updated: '2026-10-27'
journeys:
- 2026-10-27-j021-google-id-token-expires-mid-session
related:
- 2026-10-27-inv-004-is-an-empty-admin-emails-an
- 2026-10-27-inv-005-is-an-unset-worker-shared-secret
- 2026-10-27-inv-006-is-a-non-admin-without-a
- 2026-10-27-inv-007-is-the-gmail-push-webhook-unauthenticated
- 2026-10-27-inv-014-does-getnodecatalog-return-an-empty-node
- 2026-10-27-inv-018-does-the-wizard-s-deployment-mode
- 2026-10-27-inv-020-can-a-rethrown-alarm-error-replay
- 2026-10-27-jrn-001-send-to-generation-updates-a-table
- 2026-10-27-jrn-002-the-scheduled-publish-alarm-never-checks
- 2026-10-27-jrn-003-deleting-a-topic-removes-images-and
- 2026-10-27-jrn-004-when-the-sheets-merge-fails-the
- 2026-10-27-lr-001-the-e2e-dev-auth-bypass-secret
- 2026-10-27-lr-002-rescheduling-an-already-queued-post-from
- 2026-10-27-lr-009-allowed-emails-is-never-read-by
- 2026-10-27-lr-010-newsletter-by-id-actions-approve-send
- 2026-10-27-lr-012-channel-credentials-are-one-shared-config
- 2026-10-27-lr-013-the-scheduled-publish-durable-object-drops
- 2026-10-27-lr-014-every-early-exit-in-executescheduledpublish-counts
- 2026-10-27-lr-016-the-generate-stream-endpoint-lets-the
- 2026-10-27-lr-017-the-frontend-dev-port-5175-is
- 2026-10-27-lr-019-committed-owner-resource-ids-d1-kv
- 2026-10-27-lr-020-generation-worker-kv-namespaces-are-never
- 2026-10-27-lr-023-topicgenerationrules-is-used-for-both-add
- 2026-10-27-lr-024-auto-saved-editor-drafts-are-never
- 2026-10-27-lr-030-onboarding-marks-itself-complete-even-when
- 2026-10-27-lr-031-the-editor-stores-post-time-as
- 2026-10-27-lr-034-oauth-connect-hangs-forever-when-the
- 2026-10-27-lr-050-the-generation-worker-accepts-requests-when
- 2026-10-27-lr-051-deployment-mode-never-reaches-the-worker
- 2026-10-27-lr-053-the-only-cron-runs-daily-at
- 2026-10-27-lr-056-send-to-generation-navigates-away-without
- 2026-10-27-lr-060-many-llm-and-paid-api-paths
- 2026-10-27-lr-070-publish-has-no-server-side-idempotency
- 2026-10-27-lr-071-durable-object-names-have-no-user
- 2026-10-27-lr-072-tenants-without-a-sheet-work-in
- 2026-10-27-lr-074-template-assignments-news-snapshots-and-llm
- 2026-10-27-lr-089-the-editor-has-no-beforeunload-guard
- 2026-10-27-lr-105-auth-errors-are-detected-by-regex
- 2026-10-27-lr-106-the-google-id-token-is-kept
- 2026-10-27-lr-108-whatsapp-connect-silently-picks-the-first
- 2026-10-27-lr-129-the-wizard-deploy-step-timeout-cannot
- 2026-10-27-lr-133-the-google-audience-check-runs-only
- 2026-10-27-lr-134-default-admin-email-is-hard-coded
- 2026-10-27-lr-137-gmail-auto-reply-needs-a-kv
- 2026-10-27-lr-141-all-connection-disconnect-and-settings-writes
- 2026-10-27-lr-151-oauth-callbacks-report-success-after-a
- 2026-10-27-lr-157-image-fetch-and-upload-helpers-follow
- 2026-10-27-lr-160-the-public-waitlist-endpoint-is-unthrottled
- 2026-10-27-lr-161-internal-scheduler-routes-load-the-global
- 2026-10-27-lr-180-the-embedded-setup-wizard-hard-codes
- 2026-10-27-lr-187-getnodecatalog-returns-a-response-object-inside
docs:
- worker/src/db/clips.ts
- worker/src/index.ts
- worker/src/modes/saas/waitlist.ts
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: investigation
severity: P2
area: frontend/shell
raw_id: JRN-005
source_file: docs/launch-readiness/findings/JOURNEY-DELTA.md
---

## Problem

An expired Google token signs the user out and unmounts the dashboard, so unsaved editor text can be lost. Suspected, not confirmed (see Confidence in the evidence).

## Evidence and reproduction

- **Journeys:** J-021
- **Covers:** LR-024, LR-106, LR-089 (closest; none says auth expiry drops the editor state)
- **Confidence:** hypothesis
- **Evidence:** frontend/src/App.tsx:374-380 (handleAuthExpired clears the token and sets session to null)
- **Repro:** Type in the editor without saving, expire the token (edit the stored id token), click Save. Pass: the text is still there after sign-in, or the user is warned before sign-out.
- **Fix hint:** Persist editor text to localStorage on change (LR-024 recovery path) and restore it after re-sign-in; or refresh the token instead of signing out.

## Acceptance criteria

- The question in the title is answered in Attempts with file:line evidence and a clear yes/no.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

Persist editor text to localStorage on change (LR-024 recovery path) and restore it after re-sign-in; or refresh the token instead of signing out.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/JOURNEY-DELTA.md (JRN-005). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: frontend/src/App.tsx:374-380.
