# Launch readiness plan — LinkedInPost

Status: **review phase (read-only)**. No tests, builds, installs, or deploys were run for this review. Every finding is a code-reading hypothesis until someone reproduces it, so each one carries `Verified: read-only` until an executor confirms it.

## Core promise (product-owner lens)

A signed-in approved user turns a topic or a clipped article into a LinkedIn (and other channel) post: generate drafts, edit them, and publish or schedule them, without touching Google APIs or channel tokens in the browser.

Core value criteria:

1. **First run works.** Sign-in, onboarding, and connecting Sheets / channels never dead-end.
2. **Drafts are right.** The generated content matches the topic, the tone, and the approved rules. No wrong or stale facts are served.
3. **Publishing is safe.** The right channel gets the right text at the right time. No double posts, no silent failures, no lost schedules.
4. **Data is safe.** Tokens, tenant data, and drafts are never leaked or cross-tenant exposed. Nothing is lost on a retry.
5. **Setup is part of the product.** `setup.py` / `start.sh` / SETUP.md must produce a working deployment on a clean machine.

Anything that does not serve these criteria is out of scope for this release.

## Feature freeze

No new capability. Make what exists work: wire it, fix it, verify it. A needed new capability is recorded under *Frozen* in [LEDGER.md](LEDGER.md) with the smallest in-scope alternative.

## Roles (review pass)

| Role | Output | Mode |
|---|---|---|
| Journey designer | [journeys/JOURNEYS.md](journeys/JOURNEYS.md) | read-only |
| Existing-review reconciler | `findings/raw/existing-reviews.md` | read-only |
| Code reviewers (one per area) | `findings/raw/<area>.md` | read-only |
| Architecture auditor | `findings/ARCH-AUDIT.md` (docs vs code) | read-only |
| Ledger CEO | merges raw findings into [LEDGER.md](LEDGER.md), dedupes, assigns Sev | writes ledger |
| Executor | `findings/EXEC-RESULTS.md` | **not run in this pass** (no test execution was requested) |
| Fixer | `fixes/` | **not run in this pass** |

## Finding format

- **ID** — `<AREA>-<NNN>` in raw files; the ledger assigns `LR-NNN` and keeps the raw ID as an alias.
- **Sev** — P0 data loss / crash / wrong context served / cross-tenant exposure; P1 core flow broken or too slow; P2 degraded with a workaround; P3 polish.
- **Area** — feature or module (e.g. `worker/auth`, `frontend/editor`).
- **Journeys** — journey IDs from JOURNEYS.md that the item blocks or degrades.
- **Evidence** — `file:line` plus the reasoning in one or two sentences.
- **Repro** — the steps a human or executor would run to confirm (not run yet).
- **Fix hint** — the smallest change that fixes the root cause.
- **Status** — `open` / `in-progress` / `fixed` / `accepted` / `frozen`.
- **Verified** — `read-only: <what was read>` until an executor runs the repro, then `command → result`.

## Rules

- Read code, docs, and config only. Do not run tests, dev servers, builds, `tsc`, `wrangler`, or `npm install`.
- Do not change product code in this pass. Only files under `launch-release/` are written.
- Prefer existing docs as the spec (`docs/ARCHITECTURE.md`, `USE-CASES.md`, `SETUP.md`), then check the code against them.
- Skip vendored code (`video-pipeline/vendor`, `video-pipeline/.venv`, `node_modules`) and generated files (`*/generated/*`).
- Anything already fixed on `main` is recorded as `fixed` with evidence, not re-filed.

## Scope

In scope: `frontend/src`, `worker/src`, `generation-worker/src`, `packages/`, `setup/`, `setup.py`, `start.sh`, `scripts/`, `wrangler.jsonc`, `.env.example`, `features.yaml`, `SETUP.md`, `README.md`, `AGENTS.md`, `docs/ARCHITECTURE.md`, `USE-CASES.md`, `cons/`, `.github/workflows`.

Out of scope for this pass: `video-pipeline/` (separate product, vendored submodules), `automations/` beyond a glance, `docs/research/`, `docs/plans/` historical plans (used only as context).
