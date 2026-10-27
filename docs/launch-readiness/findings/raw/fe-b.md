# Raw findings: frontend shell, pages, auth/API client, connections, campaign, saas, onboarding (FEB)

Counts: P0=1 P1=6 P2=15 P3=7 (total 29)
Scope read: frontend/src/App.tsx, services/backendApi.ts, components/dashboard/index.tsx, GoogleLoginButton, pages/connections, features (onboarding, saas, campaign newsletter/bulk, feed, trending, automations api, videos, setup-wizard), plugins/dev-google-auth-bypass, .github/workflows/deploy-pages.yml. All static reasoning, nothing executed.
Journey IDs are tagged by area from JOURNEYS.md headings I could not fully re-map; the ledger CEO should re-map where marked "(area)".

### FEB-001 E2E bypass secret is baked into the public GitHub Pages bundle
- **Sev:** P0
- **Area:** .github/workflows/deploy-pages.yml, frontend/src/plugins/dev-google-auth-bypass/token.ts, worker/src/plugins/dev-google-auth-bypass/resolve-session.ts
- **Journeys:** sign-in / auth (area), all admin journeys
- **Evidence:** deploy-pages.yml:52 sets `VITE_E2E_BYPASS_SECRET: ${{ secrets.E2E_BYPASS_SECRET }}` for the production build. token.ts:14 reads `import.meta.env.VITE_E2E_BYPASS_SECRET`, so Vite inlines the literal secret in the shipped JS. The worker accepts that exact string as `idToken` and returns `isAdmin: true` (resolve-session.ts:20-34). If the worker holds the same value (the only way the cloud E2E can work), anyone who reads the bundle is an admin of the deployment.
- **Repro:** static reasoning. Build with the secret set, grep `frontend/dist/assets/*.js` for the value, POST `{action:"bootstrap",idToken:"<value>"}` to the worker.
- **Fix hint:** Never ship a bypass secret in a public bundle. Drop the E2E bypass from the Pages build (use a real test Google account or a separate non-prod worker + separate bundle). Remove `VITE_E2E_BYPASS_SECRET` from deploy-pages.yml and ensure `DEV_GOOGLE_AUTH_BYPASS_SECRET` is unset on the prod worker.
- **Status:** open
- **Verified:** read-only: deploy-pages.yml, token.ts, config.ts, resolve-session.ts

### FEB-002 Clip/feed REST calls use `globalThis.VITE_WORKER_URL` (never set), so they hit the frontend host
- **Sev:** P1
- **Area:** frontend/src/services/backendApi.ts:827,844,867,884 (getFeed, createFeedItem, getClipsPage, createClipPage); consumer features/feed/FeedPage.tsx:283,308
- **Journeys:** clip an article, feed browsing (area)
- **Evidence:** these methods read `(globalThis as {VITE_WORKER_URL}).VITE_WORKER_URL`, which nothing assigns (vite.config.ts `define` only sets `__APP_BUILD_LABEL__`; the rest of the client uses `this.endpointUrl` / `import.meta.env`). `workerUrl` is `''`, so the fetch goes to `/api/clips` on the Pages host and 404s. FeedPage swallows the error (`catch { // DB failed — silently skip }`, lines 293-296 and 314-316), so clicking Clip does nothing visible and clips never persist server-side.
- **Repro:** deploy to GitHub Pages, open /feed, click Clip on an article, watch network: request goes to `https://<user>.github.io/api/clips` (404). Static reasoning.
- **Fix hint:** use `this.endpointUrl` in all seven spots (as `post()` and `getTokenUsage` do). Surface the error in FeedPage.
- **Status:** open
- **Verified:** read-only: backendApi.ts 700-900, FeedPage.tsx 190-330, vite.config.ts, grep of globalThis.VITE_WORKER_URL

### FEB-003 Non-admin user without a spreadsheet is blocked from every route, including /connections (hypothesis)
- **Sev:** P1
- **Area:** frontend/src/components/dashboard/index.tsx:581-595, App.tsx:449-465
- **Journeys:** first-run onboarding, connect sheet (area)
- **Evidence:** the early return "Workspace setup pending ... An admin still needs to finish setup" renders instead of `<Routes>` for any non-admin with no `session.config.spreadsheetId`. Onboarding step 2 lets that same user connect a sheet and then `window.location.assign('/connections')` (App.tsx:458). If they skipped the sheet, they land on the pending wall with no way to reach Connections to add it, and the copy blames an admin who has nothing to do. Hypothesis because the SaaS tenant config may populate `spreadsheetId` elsewhere.
- **Repro:** sign in as an approved non-admin tenant, skip the sheet in onboarding, observe /connections shows the pending card.
- **Fix hint:** gate only the queue pages on spreadsheet; always allow /connections, /usage, /rules. Make the copy self-service for SaaS.
- **Status:** open
- **Verified:** read-only: dashboard/index.tsx 575-600, 805-945, App.tsx

### FEB-004 Onboarding marks itself complete even when the sheet connect fails, with no message
- **Sev:** P1
- **Area:** frontend/src/App.tsx:449-465, features/onboarding/OnboardingModal.tsx:31-40
- **Journeys:** first-run onboarding (area)
- **Evidence:** `handleCompleteOnboarding` catches a failed `connectSpreadsheet`, logs to console, calls `completeOnboarding` anyway, hides the modal and redirects. Likewise the Drive consent `onError` calls `onComplete(undefined, undefined)` immediately, so the `shareError` text it just set is never seen (modal unmounts). The user ends first run with no sheet, no error, and the onboarding never reappears (`onboardingCompleted` true).
- **Repro:** paste a sheet URL the service account cannot share, click Connect & start; modal closes silently. Static reasoning.
- **Fix hint:** on failure keep the modal open and show the error; only call `completeOnboarding` after success or an explicit Skip.
- **Status:** open
- **Verified:** read-only: App.tsx, OnboardingModal.tsx

### FEB-005 OAuth connect hangs forever when the popup is blocked
- **Sev:** P1
- **Area:** frontend/src/App.tsx:397-418
- **Journeys:** connect LinkedIn / Instagram / Gmail / YouTube / WhatsApp (area)
- **Evidence:** `window.open` may return `null`; the poll uses `popup?.closed`, which is `undefined`, so the promise never resolves, the `message` listener stays, and `connecting` is never cleared. The Connect button is disabled and shows "Connecting..." until reload. No blocked-popup message exists.
- **Repro:** block popups, click Connect LinkedIn. Static reasoning.
- **Fix hint:** if `!popup` show an alert and return; always clear interval and remove the listener when the popup closes.
- **Status:** open
- **Verified:** read-only: App.tsx 382-437

### FEB-006 OAuth and disconnect failures are only logged to the console
- **Sev:** P2
- **Area:** frontend/src/App.tsx:432-447
- **Journeys:** connect/disconnect channels (area)
- **Evidence:** the popup posts `{ok:false,error}` (worker index.ts:3514+) and the handler rejects with it, but the catch only does `console.error`. A user whose LinkedIn consent was refused, or whose disconnect call failed, sees the button revert and nothing else. Closing the popup manually also resolves silently and shows no "cancelled" state.
- **Repro:** deny consent in the popup. Static reasoning.
- **Fix hint:** route errors through `AlertProvider`; set a per-provider error state.
- **Status:** open
- **Verified:** read-only: App.tsx

### FEB-007 CSV campaign import splits on commas and newlines, so bodies are truncated or misaligned
- **Sev:** P1
- **Area:** frontend/src/features/campaign/CampaignPage.tsx:~497-515 (`handleFileRead`)
- **Journeys:** bulk campaign import (area)
- **Evidence:** `text.split('\n')` then `line.split(',')` with only a leading/trailing quote strip. A quoted body containing a comma or a newline (normal for LinkedIn posts) is cut into extra columns; `channels` and `body` shift, and the preview shows wrong posts that are then written to the sheet by `bulkImportCampaign`.
- **Repro:** upload a CSV whose body cell is `"Hello, world"`; preview shows `Hello` as body. Static reasoning.
- **Fix hint:** use a real CSV parser (papaparse) with quoted-field support, or drop CSV and require the JSON path.
- **Status:** open
- **Verified:** read-only: CampaignPage.tsx 440-520

### FEB-008 Newsletter Send/Approve/Reject have no confirmation and swallow errors
- **Sev:** P1
- **Area:** frontend/src/features/campaign/components/newsletter/NewsletterDashboard.tsx:229-260 (and NewsletterTab.tsx:173)
- **Journeys:** newsletter send (area)
- **Evidence:** `handleSendIssue` calls `api.sendNewsletterIssue` on click with no confirm dialog, no in-flight disable at the handler level, and `catch { /* ignore */ }`. A failed send looks identical to a successful one (list reloads), and a double click can issue two sends. Same pattern for create draft, toggle active, preview.
- **Repro:** click Send on an approved issue with the worker returning an error; no feedback. Static reasoning.
- **Fix hint:** confirm dialog stating recipient count, per-issue pending state, show the error from the thrown message.
- **Status:** open
- **Verified:** read-only: NewsletterDashboard.tsx 150-260, grep in newsletter/

### FEB-009 OAuth `message` listener does not check `event.origin` or `event.source`
- **Sev:** P2
- **Area:** frontend/src/App.tsx:407-417
- **Journeys:** connect channels (area)
- **Evidence:** any window able to post `{source:'channel-bot-oauth', ok:true, payload}` is trusted. For WhatsApp the payload's `connectionId` is passed to `completeWhatsAppConnection` (App.tsx:426-428). The worker side uses a specific `targetOrigin` (index.ts:4419), but the receiver never verifies it. The listener is also never removed when the popup closes without a message (leak, can fire later).
- **Repro:** from the console of another window sharing the opener, post a forged message. Static reasoning.
- **Fix hint:** require `event.origin === new URL(workerUrl).origin && event.source === popup`; remove listener in the closed branch.
- **Status:** open
- **Verified:** read-only: App.tsx, worker index.ts 4400-4425 grep

### FEB-010 WhatsApp connect silently picks the first phone number
- **Sev:** P2
- **Area:** frontend/src/App.tsx:420-429
- **Journeys:** connect WhatsApp, publish to WhatsApp (area)
- **Evidence:** when several numbers are returned, `options[0].phoneNumberId` is completed with no chooser, so messages can be sent from the wrong business number.
- **Repro:** WABA with two numbers. Static reasoning.
- **Fix hint:** show a picker listing `verifiedName / displayPhoneNumber` before `completeWhatsAppConnection`.
- **Status:** open
- **Verified:** read-only: App.tsx

### FEB-011 Disconnecting a channel has no confirmation and no error state
- **Sev:** P2
- **Area:** frontend/src/pages/connections/ConnectionsPage.tsx:408-416, SocialAccountCard.tsx:139, App.tsx:439-447
- **Journeys:** manage connections, scheduled publish (area)
- **Evidence:** the red Disconnect button calls `deleteIntegration` directly, dropping the token even if posts are scheduled against it; failure is console-only. The Sheet disconnect (SheetConnectionCard.tsx:105-111) has the same shape with a bare `catch {}`.
- **Repro:** click Disconnect with a scheduled post. Static reasoning.
- **Fix hint:** confirm with the count of scheduled posts on that channel; show failures.
- **Status:** open
- **Verified:** read-only: ConnectionsPage.tsx, SheetConnectionCard.tsx grep

### FEB-012 Onboarding requests full Google Drive scope and forwards the access token to the worker
- **Sev:** P2
- **Area:** frontend/src/features/onboarding/OnboardingModal.tsx:30-33, App.tsx:453-455
- **Journeys:** onboarding sheet connect (area)
- **Evidence:** `scope: 'https://www.googleapis.com/auth/drive'` gives read/write on the user's entire Drive just to share one sheet. The token is posted as `driveAccessToken`. Needed scope is narrower (`drive.file` plus picker, or manual share with the service account email, which SheetConnectionCard already supports).
- **Repro:** static reasoning.
- **Fix hint:** use `drive.file` + Google Picker, or the manual share path; verify the worker does not persist the token.
- **Status:** open
- **Verified:** read-only: OnboardingModal.tsx, App.tsx

### FEB-013 Auth-error detection by regex can sign users out on unrelated errors
- **Sev:** P2
- **Area:** frontend/src/services/backendApi.ts:471, 526; callers in dashboard hooks, CampaignPage.tsx:486, GlobalRulesPage.tsx
- **Journeys:** all signed-in journeys
- **Evidence:** `/unauthorized|invalid token|expired|sign in again|not allowed/i` is applied to any error message. The worker returns every error as HTTP 400 text, so messages such as "OAuth session expired", "Scheduled time has expired", "Action not allowed for this channel" force logout and discard unsaved work. Conversely a real expiry whose text differs is shown as a plain error with a stale session.
- **Repro:** trigger a worker error containing "expired" (e.g. LinkedIn state expired). Static reasoning.
- **Fix hint:** return 401 with an `code: 'AUTH'` field from the worker and key off it in `post()`.
- **Status:** open
- **Verified:** read-only: backendApi.ts 470-595, grep isAuthErrorMessage

### FEB-014 Google ID token is stored in localStorage and never refreshed; most screens ignore expiry
- **Sev:** P2
- **Area:** frontend/src/components/GoogleLoginButton.tsx:94, App.tsx:49-61, 293-367; features/automations/api.ts, pages/connections, features/feed, pages/UsagePage.tsx, features/saas/AdminPanel.tsx
- **Journeys:** all signed-in journeys
- **Evidence:** the credential is a ~1h Google ID token kept in localStorage (readable by any XSS) and reused on reload. After it expires mid-session, only bootstrap, dashboard hooks, Campaign and Rules call `onAuthExpired`; Automations, Connections, Feed, Usage, Admin and the SSE streams just show raw errors or fail silently while the session UI stays up.
- **Repro:** leave a tab open past 1h, then click Connect or Clip. Static reasoning.
- **Fix hint:** central handling in `BackendApi.post/fetch` (401 -> callback), or exchange the ID token for a worker session cookie/JWT.
- **Status:** open
- **Verified:** read-only: GoogleLoginButton.tsx, App.tsx, automations/api.ts, FeedPage.tsx

### FEB-015 Waitlist signup shows success when the server rejects it
- **Sev:** P2
- **Area:** frontend/src/services/backendApi.ts:1612-1622, features/saas/Landing.tsx:179-191
- **Journeys:** waitlist / access request (area)
- **Evidence:** `submitWaitlist` never checks `res.ok` and returns `res.json()`; Landing sets `submitted=true` after any resolved promise, including `{ok:false,...}` (bad email, rate limit, 500 with JSON). Prospects believe they are on the list.
- **Repro:** worker returns 400 `{ok:false}`; thank-you state still appears. Static reasoning.
- **Fix hint:** throw when `!res.ok || !body.ok`.
- **Status:** open
- **Verified:** read-only: backendApi.ts, Landing.tsx

### FEB-016 Admin panel actions have no error handling and Suspend has no confirmation
- **Sev:** P2
- **Area:** frontend/src/features/saas/AdminPanel.tsx:63-81, 150-260
- **Journeys:** admin approve/suspend (area)
- **Evidence:** `handleApprove`, `handleSuspend`, `handleBudget` await API calls without try/catch (called as `void handle...`), so a failure is an unhandled rejection with no UI feedback; Suspend (which locks a paying user out) fires on one click. `load()` runs once with an empty deps array.
- **Repro:** static reasoning.
- **Fix hint:** try/catch with inline error; confirm before suspend.
- **Status:** open
- **Verified:** read-only: AdminPanel.tsx, worker/src/modes/saas/admin.ts

### FEB-017 Waitlist approve passes the email as the user id (hypothesis)
- **Sev:** P2
- **Area:** frontend/src/features/saas/AdminPanel.tsx (waitlist row `handleApprove(r.email)`), worker/src/modes/saas/admin.ts:27-34
- **Journeys:** admin approve (area)
- **Evidence:** the pending-requests list calls `approveUserAccess(email)`, and the worker does `setUserStatus(db, userId, 'active')` and `resolveAccessRequest(db, userId,...)` with that value. If `users.id` is not the email (it is a Google sub elsewhere in UI: `u.id`), approval updates nothing and the person stays "Access not granted". Needs a read of db/users.ts to confirm.
- **Repro:** approve a waitlist entry, then sign in as that person.
- **Fix hint:** approve by access-request id/email via a dedicated worker route that creates/activates the user.
- **Status:** open
- **Verified:** read-only: AdminPanel.tsx, admin.ts (db/users.ts not read)

### FEB-018 Feed clips are cached in a shared localStorage key, not scoped to the user
- **Sev:** P2
- **Area:** frontend/src/features/feed/FeedPage.tsx:114-180 (`feed-clips-v2`, `read_articles`, `feed-followed-groups`)
- **Journeys:** clip an article (area), multi-account on shared browser
- **Evidence:** keys are global. Sign out and sign in as another account on the same browser: the second user's clips state initialises from the first user's clips (and shows them until the server response replaces it, which, per FEB-002, may never happen). Logout does not clear them.
- **Repro:** static reasoning.
- **Fix hint:** suffix keys with user id/email or clear on logout.
- **Status:** open
- **Verified:** read-only: FeedPage.tsx

### FEB-019 Feed refresh, group edits, votes and clip delete fail silently
- **Sev:** P2
- **Area:** frontend/src/features/feed/FeedPage.tsx:193-246, 264-277, 440-458
- **Journeys:** feed/trending (area)
- **Evidence:** over a dozen `catch { /* silent */ }` blocks, including `refreshFeedArticles` (line 246), clip delete (state removed, server not), create/update/delete interest group. The user sees an empty or stale feed with no error or retry.
- **Repro:** worker returns error on refresh. Static reasoning.
- **Fix hint:** error banner with retry for load/refresh; roll back optimistic changes on failure.
- **Status:** open
- **Verified:** read-only: FeedPage.tsx

### FEB-020 Trending falls back to hard-coded mock data when no API is enabled (hypothesis on labelling)
- **Sev:** P2
- **Area:** frontend/src/features/trending/hooks/useTrending.ts:~213-225
- **Journeys:** trending/enrichment (area)
- **Evidence:** when `useRealApis` is false the hook returns `MOCK_TRENDING_DATA` with the user's topic prefixed into titles and `recommendedTopics`. Unless the UI clearly marks it as sample data, users see invented YouTube videos / topics as real trends. I did not read the dashboard component to confirm a label.
- **Repro:** open trending with no keys configured.
- **Fix hint:** return empty + "connect a source" state, or label as sample.
- **Status:** open
- **Verified:** read-only: useTrending.ts 180-260

### FEB-021 Pricing page and landing page contradict each other, and the 14-day no-card trial has no backing flow
- **Sev:** P2
- **Area:** frontend/src/pages/PricingPage.tsx:50-160, frontend/src/features/saas/Landing.tsx:277-315
- **Journeys:** marketing / sign-up (area)
- **Evidence:** Starter is "50 AI-generated posts/month" and "LinkedIn + Instagram publishing" on /pricing but "100 AI drafts/mo" and "5 channels" on the landing page; Pro 200 vs 1,000 drafts. The FAQ promises a "14-day free trial, no credit card required", yet the product is waitlist/approval gated and no billing code exists in the client. Plans also advertise an "Analytics dashboard", "SLA + 24/7 support" and "Dedicated account manager".
- **Repro:** compare the two pages. Static reasoning.
- **Fix hint:** single source of plan data; remove claims with no backing (trial, SLA, analytics) or mark "coming soon".
- **Status:** open
- **Verified:** read-only: PricingPage.tsx, Landing.tsx

### FEB-022 Bulk campaign import has no idempotency or duplicate check
- **Sev:** P2
- **Area:** frontend/src/features/campaign/CampaignPage.tsx:463-493
- **Journeys:** bulk campaign import (area)
- **Evidence:** `bulkImportCampaign` is sent with no request id; on a timeout after the server wrote rows, the error alert invites a retry that adds every topic again (alert says "Import failed", paste text is kept). No confirm step states the number of rows and dates before writing to the sheet.
- **Repro:** import, kill the connection mid-response, retry. Static reasoning.
- **Fix hint:** client-generated import id stored by the worker, or dedupe by topic+date; show a count confirm.
- **Status:** open
- **Verified:** read-only: CampaignPage.tsx

### FEB-023 Deep-link restore after login covers only four route prefixes
- **Sev:** P3
- **Area:** frontend/src/lib/postLoginRedirect.ts:6-16
- **Journeys:** sign-in deep link (area)
- **Evidence:** only `/topics`, `/settings`, `/rules`, `/campaign` are captured. `/connections`, `/feed`, `/usage`, `/videos`, `/admin` land on `/topics` after sign-in, including the OAuth return flow if it relies on /connections.
- **Repro:** open /connections signed out, sign in.
- **Fix hint:** capture any `WORKSPACE_PATHS` value.
- **Status:** open
- **Verified:** read-only: postLoginRedirect.ts, workspaceRoutes.ts

### FEB-024 Bootstrap failure screen has no retry, and a timeout leaves a stale token
- **Sev:** P3
- **Area:** frontend/src/App.tsx:301-367, 683-689
- **Journeys:** sign-in (area)
- **Evidence:** a 10s timeout (cold worker) yields "Unable to reach the backend" which does not match the auth regex, so the token stays and the screen "Unable to start the session" offers no Retry button (only the header Log out). Also `accessPending` is decided by substring `Access not granted`/`suspended`.
- **Repro:** static reasoning.
- **Fix hint:** Retry button re-running the bootstrap effect; structured error codes.
- **Status:** open
- **Verified:** read-only: App.tsx

### FEB-025 Dead worker-KV client methods target the generation worker with a Google token
- **Sev:** P3
- **Area:** frontend/src/services/backendApi.ts:708-815, features/review/context/useReviewFlowActions.ts:440-455
- **Journeys:** save variants (area)
- **Evidence:** `saveVariantsToCloudflareKv`, `getSavedVariantsFromCloudflareKv`, `saveClipToKv`, etc. call `/v1/variants/save` and `/v1/clips`, which per docs exist on the generation worker (shared-secret auth), not the main worker; they also use the broken `globalThis.VITE_WORKER_URL`. The one live caller reads `window.__idToken`, which nothing sets, so the "KV backup" never fires.
- **Repro:** grep `__idToken`.
- **Fix hint:** delete the dead code or route via an action on the main worker.
- **Status:** open
- **Verified:** read-only: backendApi.ts, useReviewFlowActions.ts, worker/src/index.ts route grep

### FEB-026 E2E cloud bypass flag logic can never enable with a real secret
- **Sev:** P3
- **Area:** frontend/src/plugins/dev-google-auth-bypass/config.ts:19-21
- **Journeys:** E2E/test only
- **Evidence:** `isE2ECloudBypassEnabled` treats the secret as a boolean flag (`1|true|yes`). A random secret returns false, so the bypass is inert while the secret is still bundled (see FEB-001); the E2E path only works if the secret is literally "true".
- **Repro:** static reasoning.
- **Fix hint:** remove along with FEB-001.
- **Status:** open
- **Verified:** read-only: config.ts, token.ts

### FEB-027 Videos live panel polls http://127.0.0.1:8765 from the deployed app
- **Sev:** P3
- **Area:** frontend/src/features/videos/LiveRunsPanel.tsx:6
- **Journeys:** videos (flag) (area)
- **Evidence:** default base is loopback HTTP; from an HTTPS Pages origin this is blocked as mixed content / private-network access, and the failure is swallowed. Only matters if `FEATURE_VIDEO_EPISODES` is on in production.
- **Repro:** enable flag on a deployed build.
- **Fix hint:** keep flag off for release, or hide the panel unless `VITE_PIPELINE_LIVE_URL` is set.
- **Status:** open
- **Verified:** read-only: LiveRunsPanel.tsx, dashboard/index.tsx route

### FEB-028 Embedded setup wizard hard-codes http://localhost:3456 and is reachable in production at /setup
- **Sev:** P3
- **Area:** frontend/src/features/setup-wizard/setupService.ts:68-132, SetupWizard.tsx:202,466; dashboard/index.tsx /setup route
- **Journeys:** setup wizard (area)
- **Evidence:** admin-only route, but in a deployed build every step fetches loopback ports that do not exist; failures give raw network errors. The `Setup` button is shown in the header to all admins (App.tsx:159-167), and a bare `FinalStep` opens `localhost:5173` while vite uses 5175.
- **Repro:** admin clicks Setup on a deployed site.
- **Fix hint:** hide Setup unless dev/local; align the port.
- **Status:** open
- **Verified:** read-only: setupService.ts grep, FinalStep.tsx:144, vite.config.ts

### FEB-029 Onboarding modal has no dialog semantics, focus trap or escape
- **Sev:** P3
- **Area:** frontend/src/features/onboarding/OnboardingModal.tsx:56-60
- **Journeys:** first-run onboarding (area)
- **Evidence:** a fixed overlay div without `role="dialog"`/`aria-modal`/labelling; keyboard focus can still reach the page behind. Step 1 "Skip for now" works by mouse and keyboard, so it does not strand, hence P3.
- **Repro:** tab through the page while the modal is open.
- **Fix hint:** use the shared Dialog primitive.
- **Status:** open
- **Verified:** read-only: OnboardingModal.tsx
