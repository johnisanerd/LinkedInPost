---
id: 2026-10-27-j016-saas-landing-page-and-redirect-for
title: J-016 SaaS landing page and redirect for signed-in users
status: planned
created: '2026-10-27'
updated: '2026-10-27'
journey_type: user
scope_type: section
scope: frontend
actor: New signed-in user
trigger: '`deploymentMode: saas` build.'
verification_owner: unassigned (owner to set)
source_revision: null
checked_at: null
modules: &id001 []
code_paths: *id001
related: []
docs:
- docs/launch-readiness/journeys/JOURNEYS.md
priority: P2
core: 'yes'
external_service: Google OAuth
legacy_id: J-016
---

## Purpose and scope

SaaS landing page and redirect for signed-in users. Priority P2, CORE yes. Imported from journey J-016 in docs/launch-readiness/journeys/JOURNEYS.md.

## Actor, trigger and prerequisites

Persona: New signed-in user. Preconditions: `deploymentMode: saas` build.

## Steps and information flow

1. Signed out: open `/` (renders `Landing`); `/landing` redirects to `/`.
2. Sign in; `/` now redirects to `/topics`.
3. Open `/pricing`, `/about`, `/terms`, `/privacy-policy` signed out.

## Modules and code map

frontend/src/App.tsx, frontend/src/features/saas/Landing.tsx, frontend/src/pages/PricingPage.tsx, frontend/src/pages/AboutPage.tsx, frontend/src/pages/TermsOfServicePage.tsx

## Success and acceptance

Landing renders with sign-in; after login `window.location.pathname === "/topics"`; the four public pages render without a token. (Landing text "Join 2,400+ content creators" is a hard-coded claim; confirm it is true or remove before launch: frontend/src/features/saas/Landing.tsx.)

## Failure, edge cases and recovery

Failure behaviour is described in the steps and pass check above. Defects found on this journey are linked from their backlog records (their journeys field names this record).

## Verification evidence

Not verified. Nothing was executed; the journey was derived from reading the code. Status stays planned until the steps are run at a named revision.

## Gaps and linked work

Linked work is derived from the backlog records whose journeys field names this record.

## Next actions

Run the steps on a fresh clone and the pass check; record the outcome in Verification evidence; resolve every linked backlog item before marking verified.
