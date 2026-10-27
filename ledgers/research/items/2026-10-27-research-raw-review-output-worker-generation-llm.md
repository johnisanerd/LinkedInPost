---
id: 2026-10-27-research-raw-review-output-worker-generation-llm
title: 'Raw review output: Worker generation, LLM, integrations, newsletter, publish adapters.'
created: '2026-10-27'
updated: '2026-10-27'
journeys: []
related: []
docs:
- docs/launch-readiness/findings/raw/worker-b.md
status: complete
source_revision: a65b712
---

## Question

What does the code in this area get wrong, and what must be verified?

## Sources and method

Read-only review by one reviewer agent at revision a65b712. Scope: Worker generation, LLM, integrations, newsletter, publish adapters. Raw file: docs/launch-readiness/findings/raw/worker-b.md.

## Findings

46 raw items in the file. Items filed as backlog records (by ledger record, where the raw ID was merged or kept): 2026-10-27-lr-010-newsletter-by-id-actions-approve-send, 2026-10-27-lr-011-the-email-newsletter-send-is-a, 2026-10-27-lr-012-channel-credentials-are-one-shared-config, 2026-10-27-lr-013-the-scheduled-publish-durable-object-drops, 2026-10-27-lr-015-completeonboarding-accepts-any-spreadsheet-id-without, 2026-10-27-lr-016-the-generate-stream-endpoint-lets-the, 2026-10-27-lr-056-send-to-generation-navigates-away-without, 2026-10-27-lr-057-quick-change-and-preview-endpoints-accept, 2026-10-27-lr-058-fetchwithretry-retries-non-idempotent-posts-posts, 2026-10-27-lr-059-gmail-to-cc-bcc-and-subject, 2026-10-27-lr-060-many-llm-and-paid-api-paths, 2026-10-27-lr-061-gemini-token-usage-is-read-from, 2026-10-27-lr-062-normalizedeliveryimageurl-rewrites-any-url-with-an, 2026-10-27-lr-063-newsletter-send-has-no-claim-or, 2026-10-27-lr-064-newsletter-bodies-are-generated-in-gemini, 2026-10-27-lr-065-fetched-article-and-llm-text-is, 2026-10-27-lr-066-newsletter-preview-and-approval-messages-can, 2026-10-27-lr-068-per-user-oauth-tokens-expire-with, 2026-10-27-lr-069-articles-without-a-parseable-date-are, 2026-10-27-lr-070-publish-has-no-server-side-idempotency, 2026-10-27-lr-071-durable-object-names-have-no-user, 2026-10-27-lr-117-rss-parsing-does-not-decode-entities, 2026-10-27-lr-136-automation-rules-and-youtube-schedules-expire, 2026-10-27-lr-137-gmail-auto-reply-needs-a-kv, 2026-10-27-lr-138-instagram-comment-automation-can-reply-to, 2026-10-27-lr-142-content-review-is-advisory-only-publish, 2026-10-27-lr-143-content-review-usage-is-logged-against, 2026-10-27-lr-144-monthly-token-usage-misses-the-first, 2026-10-27-lr-148-fetched-article-text-client-sent-research, 2026-10-27-lr-149-the-dall-e-provider-defaults-to, 2026-10-27-lr-152-linkedin-commentary-is-sent-raw-to, 2026-10-27-lr-153-multi-part-sends-leave-partial-deliveries, 2026-10-27-lr-154-no-llm-provider-call-has-a, 2026-10-27-lr-155-provider-and-model-are-silently-substituted, 2026-10-27-lr-157-image-fetch-and-upload-helpers-follow, 2026-10-27-lr-158-newsletter-schedule-logic-uses-utc-ignores, 2026-10-27-lr-159-there-is-no-per-channel-length, 2026-10-27-lr-160-the-public-waitlist-endpoint-is-unthrottled, 2026-10-27-lr-161-internal-scheduler-routes-load-the-global, 2026-10-27-lr-190-the-workflow-engine-is-not-run, 2026-10-27-lr-192-image-generation-cost-keys-do-not, 2026-10-27-lr-193-the-static-gemini-model-list-and. Raw IDs: WKB-001, WKB-002, WKB-003, WKB-004, WKB-005, WKB-006, WKB-007, WKB-008, WKB-009, WKB-010, WKB-011, WKB-012, WKB-013, WKB-014, WKB-015, WKB-016, WKB-017, WKB-018, WKB-019, WKB-020, WKB-021, WKB-022, WKB-023, WKB-024, WKB-025, WKB-026, WKB-027, WKB-028, WKB-029, WKB-030, WKB-031, WKB-032, WKB-033, WKB-034, WKB-035, WKB-036, WKB-037, WKB-038, WKB-039, WKB-040, WKB-041, WKB-042, WKB-043, WKB-044, WKB-045, WKB-046.

## Limits

Read-only static reading at the stated revision; nothing was executed. Items filed from this record are unverified until a check is run and recorded.

## Recommendations and follow-up

Work each filed backlog item; add evidence in its Attempts.
