---
id: 2026-10-27-review-launch-readiness-of-the-whole-application-read
title: Launch readiness of the whole application (read-only)
status: complete
created: '2026-10-27'
updated: '2026-10-27'
scope_type: overall
scope: application
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

Scope: overall / application. Source revision a65b712 (main before this review). Read-only; nothing executed.

## Executive summary

The review found 348 open and 71 investigate items across the application and 95 items the current code already fixes. Nothing is verified by execution. The top risks are data-isolation and auth-gate defects (P0): shared channel credentials, a scheduled-publish user drop, an unenforced allowlist, and a shipped dev bypass secret (LR-001). A tracked dev env file with a bypass key (HYG-003) is P1.

## Current state and capabilities

Implemented and read: frontend features, worker dispatcher and publish, generation worker, setup wizard, workflows. Missing or not implemented: YouTube publish, YouTube poll schedule, a test script, a pipeline_rows table. Test coverage of P0 journeys is weak (TST items).

## Changes since previous review

First review of this scope. There is no previous review.

## Conflicts and architectural issues

Architectural conflicts: per-tenant data and credentials are not isolated in the worker and the generation worker; setup scripts and the Node wizard expose secrets; documented allowlist and bypass behaviour contradict the code (ARCH items, linked as duplicates of review items).

## Direction and priorities

Priority: fix P0 tenancy and secret items first, then add tests for the P0 journeys, then P1. Verify by executing the P0 journeys on a fresh clone before any closure.

## Follow-up work

Every item is a linked backlog record (see the backlog index). Priorities follow the severities in the records.

## Evidence and limitations

Static reading only. Nothing executed. Journeys and findings are unverified until an executor runs them at a named revision.
