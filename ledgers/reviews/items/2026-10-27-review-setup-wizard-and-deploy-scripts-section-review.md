---
id: 2026-10-27-review-setup-wizard-and-deploy-scripts-section-review
title: Setup wizard and deploy scripts section review (read-only)
status: complete
created: '2026-10-27'
updated: '2026-10-27'
scope_type: section
scope: setup
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

Scope: section / setup. Source revision a65b712 (main before this review). Read-only; nothing executed.

## Executive summary

The Node and Python wizards, deploy scripts and workflows were read by one reviewer (SET items), plus the setup and ARCH checks.

## Current state and capabilities

The Node wizard is unauthenticated and binds all interfaces; setup prints and rotates secrets; several committed owner IDs break setup for others.

## Changes since previous review

First review of this scope. There is no previous review.

## Conflicts and architectural issues

Priority: the wizard exposure and secret handling first (P0), then the non-owner setup path.

## Direction and priorities

Setup was not run; every SET item needs an executor check on a clean machine.

## Follow-up work

Every item is a linked backlog record (see the backlog index). Priorities follow the severities in the records.

## Evidence and limitations

Static reading only. Nothing executed. Journeys and findings are unverified until an executor runs them at a named revision.
