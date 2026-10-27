---
id: 2026-10-27-j029-first-sign-in-shows-onboarding-skipping
title: J-029 First sign-in shows onboarding; skipping both steps
status: planned
created: '2026-10-27'
updated: '2026-10-27'
journey_type: user
scope_type: section
scope: frontend
actor: New signed-in user
trigger: '`users.onboarding_completed = 0` (default).'
verification_owner: unassigned (owner to set)
source_revision: null
checked_at: null
modules: &id001
- worker/src/index.ts
code_paths: *id001
related: []
docs:
- docs/launch-readiness/journeys/JOURNEYS.md
priority: P1
core: 'yes'
external_service: Google OAuth
legacy_id: J-029
---

## Purpose and scope

First sign-in shows onboarding; skipping both steps. Priority P1, CORE yes. Imported from journey J-029 in docs/launch-readiness/journeys/JOURNEYS.md.

## Actor, trigger and prerequisites

Persona: New signed-in user. Preconditions: `users.onboarding_completed = 0` (default).

## Steps and information flow

1. Sign in; the `OnboardingModal` ("Connect your accounts") appears.
2. Click "Skip for now →" (label becomes "Continue →" if an integration exists).
3. On "Content source" click "Skip, I'll add later →".

## Modules and code map

frontend/src/features/onboarding/OnboardingModal.tsx, frontend/src/features/onboarding/ConnectAccountsGrid.tsx, frontend/src/App.tsx (`handleCompleteOnboarding`), worker/src/index.ts (`completeOnboarding`)

Code anchors that exist: worker/src/index.ts

## Success and acceptance

`ACTION completeOnboarding {}` returns `{"ok":true}`; D1 `users.onboarding_completed=1`; browser navigates to `/connections` via `window.location.assign`. Next `bootstrap` returns `onboardingCompleted:true`; the modal does not reappear.

## Failure, edge cases and recovery

Failure behaviour is described in the steps and pass check above. Defects found on this journey are linked from their backlog records (their journeys field names this record).

## Verification evidence

Not verified. Nothing was executed; the journey was derived from reading the code. Status stays planned until the steps are run at a named revision.

## Gaps and linked work

Linked work is derived from the backlog records whose journeys field names this record.

## Next actions

Run the steps on a fresh clone and the pass check; record the outcome in Verification evidence; resolve every linked backlog item before marking verified.
