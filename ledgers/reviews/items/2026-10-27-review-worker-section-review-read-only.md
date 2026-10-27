---
id: 2026-10-27-review-worker-section-review-read-only
title: Worker section review (read-only)
status: complete
created: '2026-10-27'
updated: '2026-10-27'
scope_type: section
scope: worker
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

Scope: section / worker. Source revision a65b712 (main before this review). Read-only; nothing executed.

## Executive summary

The main worker dispatcher, auth, publish, scheduled publish, newsletter and generation proxy were read by two reviewers.

## Current state and capabilities

The dispatcher accepts client-controlled tenant fields in places, and credentials are shared across users (WKA/WKB items).

## Changes since previous review

First review of this scope. There is no previous review.

## Conflicts and architectural issues

The allowlist is not enforced and the scheduled-publish path drops the user identity.

## Direction and priorities

Priority: tenancy and credential isolation, then schedule correctness, then tests.

## Follow-up work

Every item is a linked backlog record (see the backlog index). Priorities follow the severities in the records.

## Evidence and limitations

Static reading only. Nothing executed. Journeys and findings are unverified until an executor runs them at a named revision.
