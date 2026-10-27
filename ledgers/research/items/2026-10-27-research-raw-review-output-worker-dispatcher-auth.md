---
id: 2026-10-27-research-raw-review-output-worker-dispatcher-auth
title: 'Raw review output: Worker dispatcher, auth, persistence, scheduled publish, tenancy.'
created: '2026-10-27'
updated: '2026-10-27'
journeys: []
related: []
docs:
- docs/launch-readiness/findings/raw/worker-a.md
status: complete
source_revision: a65b712
---

## Question

What does the code in this area get wrong, and what must be verified?

## Sources and method

Read-only review by one reviewer agent at revision a65b712. Scope: Worker dispatcher, auth, persistence, scheduled publish, tenancy. Raw file: docs/launch-readiness/findings/raw/worker-a.md.

## Findings

38 raw items in the file. Items filed as backlog records (by ledger record, where the raw ID was merged or kept): 2026-10-27-lr-010-newsletter-by-id-actions-approve-send, 2026-10-27-lr-012-channel-credentials-are-one-shared-config, 2026-10-27-lr-013-the-scheduled-publish-durable-object-drops, 2026-10-27-lr-014-every-early-exit-in-executescheduledpublish-counts, 2026-10-27-lr-015-completeonboarding-accepts-any-spreadsheet-id-without, 2026-10-27-lr-049-cors-allows-only-get-post-and, 2026-10-27-lr-052-loadstoredconfig-omits-imagegen-enrichmentskills-and-youtube, 2026-10-27-lr-054-every-row-mutation-upserts-the-full, 2026-10-27-lr-055-addtopic-swallows-a-sheets-failure-so, 2026-10-27-lr-056-send-to-generation-navigates-away-without, 2026-10-27-lr-060-many-llm-and-paid-api-paths, 2026-10-27-lr-063-newsletter-send-has-no-claim-or, 2026-10-27-lr-067-gmail-telegram-and-whatsapp-recipients-come, 2026-10-27-lr-068-per-user-oauth-tokens-expire-with, 2026-10-27-lr-070-publish-has-no-server-side-idempotency, 2026-10-27-lr-071-durable-object-names-have-no-user, 2026-10-27-lr-072-tenants-without-a-sheet-work-in, 2026-10-27-lr-073-deleterow-trusts-the-client-row-index, 2026-10-27-lr-074-template-assignments-news-snapshots-and-llm, 2026-10-27-lr-090-feed-refresh-replaces-a-multi-topic, 2026-10-27-lr-105-auth-errors-are-detected-by-regex, 2026-10-27-lr-131-streaming-and-rest-routes-parse-bodies, 2026-10-27-lr-132-the-api-feed-limit-is-unvalidated, 2026-10-27-lr-135-every-request-re-verifies-the-google, 2026-10-27-lr-140-env-secrets-and-legacy-plaintext-tokens, 2026-10-27-lr-141-all-connection-disconnect-and-settings-writes, 2026-10-27-lr-144-monthly-token-usage-misses-the-first, 2026-10-27-lr-145-list-queries-clips-feedback-rows-users, 2026-10-27-lr-146-one-topics-row-without-an-id, 2026-10-27-lr-147-migration-0010-may-orphan-legacy-rows, 2026-10-27-lr-150-trending-panels-use-deployment-wide-env, 2026-10-27-lr-151-oauth-callbacks-report-success-after-a, 2026-10-27-lr-157-image-fetch-and-upload-helpers-follow, 2026-10-27-lr-160-the-public-waitlist-endpoint-is-unthrottled, 2026-10-27-lr-161-internal-scheduler-routes-load-the-global, 2026-10-27-lr-187-getnodecatalog-returns-a-response-object-inside, 2026-10-27-lr-188-small-access-admin-defects-sql-text, 2026-10-27-lr-191-the-process-wide-lifecycle-event-bus. Raw IDs: WKA-001, WKA-002, WKA-003, WKA-004, WKA-005, WKA-006, WKA-007, WKA-008, WKA-009, WKA-010, WKA-011, WKA-012, WKA-013, WKA-014, WKA-015, WKA-016, WKA-017, WKA-018, WKA-019, WKA-020, WKA-021, WKA-022, WKA-023, WKA-024, WKA-025, WKA-026, WKA-027, WKA-028, WKA-029, WKA-030, WKA-031, WKA-032, WKA-033, WKA-034, WKA-035, WKA-036, WKA-037, WKA-038.

## Limits

Read-only static reading at the stated revision; nothing was executed. Items filed from this record are unverified until a check is run and recorded.

## Recommendations and follow-up

Work each filed backlog item; add evidence in its Attempts.
