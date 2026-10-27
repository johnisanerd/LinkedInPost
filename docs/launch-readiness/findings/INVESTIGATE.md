# Items to investigate

Each item needs a check before anyone acts. Read-only; nothing executed. Owner is blank on purpose.

### INV-001 P1 frontend/feed - Do feed and clip REST calls fail because VITE_WORKER_URL is unset? (FEB-002 vs FEA-027)
- **Question:** FEB-002 says getFeed, createFeedItem, getClipsPage and createClipPage read globalThis.VITE_WORKER_URL, which is never set, so they hit the frontend host. FEA-027 says /api/clips is not routed by the worker. Which is right?
- **Why it matters:** If FEB-002 holds, clipping an article does nothing visible on a deployed Pages site and clips never persist (FeedPage swallows the error). If FEA-027 were right the fix would be on the worker side instead.
- **How to settle it:** Run on a Pages build: open /feed, click Clip, check the network tab for the request host (expect the Pages host, 404). Also run `cd frontend && grep -rn "globalThis" src vite.config.ts` and confirm nothing assigns VITE_WORKER_URL. Fix test: use this.endpointUrl in backendApi.ts:827,844,867,884 then re-click Clip.
- **Related items:** LR-027, FEB-002, FEA-027
- **Owner:** 

### INV-002 P1 worker/llm - Does Gemini return usageMetadata at the top level of the response? (WKB-013)
- **Question:** gemini.ts reads payload.candidates?.[0]?.usageMetadata. Is usageMetadata actually a top-level field of the generateContent response, so the code logs 0 tokens?
- **Why it matters:** If true, llm_usage_log token sums stay 0 and checkTokenBudget never trips: the per-user budget does nothing for Gemini calls.
- **How to settle it:** Make one live Gemini generateContent call with a test key and log Object.keys(payload); or read the current Gemini API reference for GenerateContentResponse.usageMetadata. Then run one generation and `SELECT prompt_tokens, completion_tokens FROM llm_usage_log ORDER BY created_at DESC LIMIT 1` on the local D1.
- **Related items:** LR-061, WKB-013
- **Owner:** 

### INV-003 P1 worker/integrations - Does LinkedIn rest/posts truncate commentary at unescaped reserved characters? (WKB-022)
- **Question:** The multi-image path sends commentary: request.text raw to /rest/posts. Does LinkedIn parse commentary as little text format so that characters such as ( ) [ ] @ # truncate the visible post?
- **Why it matters:** LLM drafts routinely contain parentheses and hashtags, so multi-image LinkedIn posts could publish cut off at the first reserved character.
- **How to settle it:** Read the LinkedIn Posts API 'little text' documentation, then on a test LinkedIn account publish a 2-image post with the text 'Results (up 40%) #growth' through worker/src/integrations/linkedin/index.ts and compare with the rendered post.
- **Related items:** LR-152, WKB-022
- **Owner:** 

### INV-004 P0 worker/auth - Is an empty ADMIN_EMAILS an owner-admin P0 or a P2? (J-127 vs ARCH-012)
- **Question:** The journey designer rates J-127 P0 (CORE) because an empty ADMIN_EMAILS makes 99pratyush@gmail.com admin on any deployment. ARCH-012 and LR-134 rate it P2. Which severity is right?
- **Why it matters:** On a customer or fork deployment missing the variable, the project author gets admin over that tenant. Severity decides whether it blocks launch.
- **How to settle it:** Read worker/src/index.ts:3020-3027 (resolveAdminEmailAllowlist). Decide whether launch is single-owner (then P2) or hands the repo to customers (then P0). To settle: deploy to a fresh test Worker with ADMIN_EMAILS unset and sign in as the default address; also check setup/worker_config.py always writes ADMIN_EMAILS.
- **Related items:** LR-134, J-127, ARCH-012
- **Owner:** 

### INV-005 P0 generation-worker/auth - Is an unset WORKER_SHARED_SECRET on the generation worker P0 or P1? (J-060 vs ARCH-003)
- **Question:** J-060 is P0 (CORE) in the journeys; ARCH-003 and GWP-003 rate the same defect P1 (LR-050). Which severity?
- **Why it matters:** A manually deployed generation worker without the secret lets anyone run the LLM pipeline on the operator's keys. The setup path generates the secret, so the exposure depends on how people deploy.
- **How to settle it:** Read generation-worker/src/index.ts:41-45 (checkAuth) and setup/worker_config.py + setup/cloudflare.py to see whether every supported deploy path sets the secret. To settle: `curl -X POST <gen-worker>/v1/generate` against a test deploy with the secret unset (expect 401 after the fix).
- **Related items:** LR-050, J-060, ARCH-003, GWP-003
- **Owner:** 

### INV-006 P0 frontend/tenancy - Is a non-admin without a connected sheet locked out of everything? (J-031 vs FEB-003)
- **Question:** J-031 is P0 (CORE); FEB-003 is a P1 hypothesis. Does the 'Workspace setup pending' wall block every route, including /connections, for a non-admin with no spreadsheetId?
- **Why it matters:** If true, a new SaaS user who skipped the sheet step cannot reach Connections to fix it and the copy blames an admin who has nothing to do.
- **How to settle it:** In frontend/src/components/dashboard/index.tsx read where the early return (line 581) sits relative to <Routes> and whether /connections is rendered by this component or by App.tsx (App.tsx:449-465). To settle: sign in as a fresh non-admin test user with no sheet and visit /connections directly.
- **Related items:** LR-072, J-031, FEB-003
- **Owner:** 

### INV-007 P1 worker/automations - Is the Gmail push webhook unauthenticated, and is it P1 or P2? (J-116 vs WKB-031)
- **Question:** J-116 is P1; WKB-031 is P2 (LR-137). Does the Gmail push endpoint accept any caller, and does anything write the oauth:gmail:<address> KV key it needs?
- **Why it matters:** An unauthenticated webhook lets anyone trigger auto-replies; a missing KV key means registration always fails, so the feature may not work at all.
- **How to settle it:** Read worker/src/automations/routes.ts:55-58,253-263 and worker/src/automations/platforms/gmail.ts:38-116; `grep -rn "oauth:gmail" worker/src`. To settle: POST a forged Pub/Sub body to the push endpoint on a test Worker without any token.
- **Related items:** LR-137, J-116, WKB-031
- **Owner:** 

### INV-008 P2 frontend/trending - Can production users see mock trending data? (FEB-020, NEW-6, U-J11)
- **Question:** useTrending returns MOCK_TRENDING_DATA when useRealApis is false. Is the sample data labelled in the UI, and can the flag be false in production?
- **Why it matters:** Invented YouTube videos and topics would be shown as real trends.
- **How to settle it:** Read frontend/src/features/trending/hooks/useTrending.ts:196-225,280-292 and where useRealApis is computed; open trending with no API keys on a test build and look for a Sample label.
- **Related items:** LR-094
- **Owner:** 

### INV-009 P2 frontend/saas-admin - Does waitlist approve update zero rows because it passes the email as the user id? (FEB-017)
- **Question:** The admin panel calls approve with r.email, and the worker does setUserStatus(db, userId, 'active') with that value. Is users.id an email or a Google sub?
- **Why it matters:** Approving someone who never signed in would silently do nothing and the person stays blocked.
- **How to settle it:** Read worker/src/db/users.ts (id column and setUserStatus) and the access_requests table. To settle: add a pending request for a test email, approve it from /admin, then check the users and access_requests rows.
- **Related items:** LR-101
- **Owner:** 

### INV-010 P2 worker/db - Does migration 0010 orphan legacy rows and rewrite topic_key? (WKA-027)
- **Question:** The backfill sets user_id from users.spreadsheet_id, but the admin sheet is copied from KV lazily after deploy. Do legacy rows end up unreachable?
- **Why it matters:** Data loss-like behaviour on upgrading an existing deployment.
- **How to settle it:** Copy the production D1 data to a scratch database, apply worker/migrations/0010_pipeline_user_primary.sql, and compare row counts per user and topic_key values before and after.
- **Related items:** LR-147
- **Owner:** 

### INV-011 P2 worker/image-gen - Do the dall-e and Stability providers return usable images with default settings? (WKB-027)
- **Question:** Default model is gpt-image-1, which returns b64_json not url; sizes are DALL-E 3 sizes; Stability 4:3 is claimed invalid.
- **Why it matters:** Image generation would throw after billing for users with default settings.
- **How to settle it:** Read worker/src/image-gen/providers/dall-e.ts:4-15 and stability.ts:4-12, check current provider API docs, then call generateImageFromText once per provider with a test key.
- **Related items:** LR-149
- **Owner:** 

### INV-012 P2 worker/publish - Does the worker reject over-length posts before changing status? (FEA-025)
- **Question:** The frontend has only an empty-text check. Does the worker validate channel length limits, or does the provider error appear after the row is set to Approved?
- **Why it matters:** Long posts could leave a row Approved but unpublished with a provider error.
- **How to settle it:** Read publishContent in worker/src/index.ts and frontend/src/features/review/context/useReviewFlowActions.ts:624-721. To settle: paste more than 3000 characters and click Publish to LinkedIn on a test account; note the row status afterwards.
- **Related items:** LR-159
- **Owner:** 

### INV-013 P3 frontend/editor - Does Generate-and-save return null because the card is built inside a setState updater? (FEA-029)
- **Question:** newCard is assigned inside the setGeneratedCards updater and returned immediately. Is the updater run before the return?
- **Why it matters:** If not, the workflow is never saved and the user sees no error.
- **How to settle it:** Read frontend/src/features/review/context/useReviewFlowActions.ts:344-357. To settle: Styles tab, pick a card, click Generate and save, check whether a custom workflow appears.
- **Related items:** LR-168
- **Owner:** 

### INV-014 P3 worker/api - Does getNodeCatalog return an empty node list to the Enrichment page? (WKA-036)
- **Question:** The case returns Response.json({nodes}); the caller wraps it as {ok:true,data:<Response>}. Does the dispatcher unwrap a Response or serialise it as {}?
- **Why it matters:** The Enrichment node list would arrive empty.
- **How to settle it:** Read the action dispatcher in worker/src/index.ts around the getNodeCatalog case (line 1875) and its caller. To settle: call ACTION getNodeCatalog on a local worker and inspect data.
- **Related items:** LR-187
- **Owner:** 

### INV-015 P3 worker/generation - Does the shared lifecycle event bus leak node metadata between users? (WKA-037)
- **Question:** lifecycleEventBus is a module singleton and each /api/generate/stream request subscribes with no run or user filter. Is it also contradicted by WKB-044 (engine never run)?
- **Why it matters:** Another user's node ids and durations could appear in a stream; handlers may leak on early return.
- **How to settle it:** Read worker/src/index.ts:859-890 and worker/src/engine/events/LifecycleEventBus.ts:51; check whether the engine runs in production (WKB-044). To settle: run two concurrent generations on a local worker and compare the streamed events.
- **Related items:** LR-191
- **Owner:** 

### INV-016 P3 worker/llm - Are the static Gemini model ids retired? (WKB-045)
- **Question:** The fallback catalog and GOOGLE_MODEL_DEFAULT use gemini-2.0-flash, 1.5-flash and 1.5-pro. Are they still served?
- **Why it matters:** Users would see 404 errors when live model discovery fails.
- **How to settle it:** Compare worker/src/llm/providers/gemini.ts:4-9 and worker/src/llm/google-model-policy.ts:1 against the current Gemini models list endpoint with a test key.
- **Related items:** LR-193
- **Owner:** 

### INV-017 P2 frontend/editor - Do two rows with the same topic text share one editor state? (FEA-014)
- **Question:** initKey is built from row.topic, so a published post and its draft copy get the same key. Does Save Draft then write into the previous row?
- **Why it matters:** Edits could be saved onto the wrong post.
- **How to settle it:** Read frontend/src/features/review/context/useReviewFlowState.ts:376-397. To settle: open published post P, then its copy via browser history, edit, Save Draft, and check which row changed.
- **Related items:** LR-083
- **Owner:** 

### INV-018 P1 setup/config - Does the wizard's DEPLOYMENT_MODE setting reach the deployed Worker? (SET-034)
- **Question:** The wizard regex-replaces DEPLOYMENT_MODE in worker/wrangler.jsonc, but the key is absent from the tracked vars. Does the worker read it from env or from generated features.ts?
- **Why it matters:** If it never reaches the Worker, selfHosted installs run with SaaS token budgets and can block generation.
- **How to settle it:** Read setup/wizard/steps/mode.py and `grep -n DEPLOYMENT_MODE worker/wrangler.jsonc worker/src/index.ts`. To settle: choose selfHosted in the wizard, deploy to a test account, and call a generation action.
- **Related items:** LR-051
- **Owner:** 

### INV-019 P1 worker/generation - Is a topic stranded Pending when the user leaves during Send to Generation? (FEA-004)
- **Question:** The raw item is P1 with a hypothesis on worker-side cancellation: if the client navigates away, does the worker keep running and save a result?
- **Why it matters:** A topic could stay Pending forever with no refresh or error.
- **How to settle it:** Read frontend/src/services/backendApi.ts (sendTopicToGeneration) and worker/src/index.ts:1165-1270. To settle: click Send to Generation, navigate away at once, and watch the sheet row and the worker log.
- **Related items:** LR-056
- **Owner:** 

### INV-020 P1 worker/schedule - Can a rethrown alarm error replay a publish and double-post? (ARCH-010)
- **Question:** ScheduledPublishAlarm rethrows on error so the runtime retries; executeScheduledPublish has no already-published guard. Does a retry after a successful send post twice?
- **Why it matters:** Duplicate LinkedIn posts, which cannot be undone.
- **How to settle it:** Read worker/src/scheduled-publish/ScheduledPublishAlarm.ts:85-100 and executeScheduledPublish in worker/src/index.ts:4756-4783 for a status or published-flag check. To settle: on a test Worker, force the post-send mark step to fail and let the alarm retry.
- **Related items:** LR-070
- **Owner:** 
