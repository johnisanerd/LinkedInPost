---
id: 2026-10-27-review-automations-section-review-read-only
title: Automations section review (read-only)
status: complete
created: '2026-10-27'
updated: '2026-10-27'
scope_type: section
scope: automations
reviewer: Claude Haiku 5.5 (read-only review agents, coordinated by the lead)
reviewed_at: '2026-10-27T15:44:37+01:00'
source_revision: a65b712
previous_review: null
journeys: []
related: []
docs:
- docs/launch-readiness/findings/REVIEW-ITEMS.md
---

## Scope and revision

Scope: section / automations. Source revision a65b712 (main before this review). Read-only; nothing executed.

## Executive summary

automations/ is one YouTube comment poller. The review found state loss and reply-scope defects.

## Current state and capabilities

The poller's replied-IDs file is not persisted between CI runs, and the first run replies to all history.

## Changes since previous review

First review of this scope. There is no previous review.

## Conflicts and architectural issues

Priority: persist state or make the run idempotent; then limit the first run.

## Direction and priorities

Nothing executed; the workflow schedule is disabled, so the poller is manual-only today.

## Follow-up work

Every item is a linked backlog record (see the backlog index). Priorities follow the severities in the records.

## Evidence and limitations

Static reading only. Nothing executed. Journeys and findings are unverified until an executor runs them at a named revision.
