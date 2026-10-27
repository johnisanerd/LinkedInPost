# Journey delta items

Every "CODE-READING FINDING" in launch-release/journeys/JOURNEYS.md (47 journeys, 50 findings counting J-056 x2 and J-083 x3) was checked against REVIEW-ITEMS.md, INVESTIGATE.md and EXISTING-REVIEWS.md. Items below are the ones no existing item describes. Read-only; nothing executed.

### JRN-001 P0 worker/generation - Send to Generation updates a table that does not exist (pipeline_rows), so the status flip throws after the generation worker has already started
- **Journeys:** J-056
- **Covers:** none (LR-056 is closest but describes the unconsumed stream and non-atomic claim, not the missing table)
- **Confidence:** confirmed-by-reading
- **Evidence:** worker/src/index.ts:1212,1219,1227 (UPDATE pipeline_rows); no migration in worker/migrations defines pipeline_rows (the table is pipeline_state)
- **Repro:** Create a Draft topic, click "Send to Generation". Expect HTTP 400 with a D1 "no such table: pipeline_rows" error while the generation worker run is already started; the topic never reaches Pending via this path. The revert-to-Draft handlers fail the same way.
- **Fix hint:** Change the three statements to the real table and columns (pipeline_state), or call the existing pipeline status helper; add a test that runs the handler against the migrated schema.

### JRN-002 P1 worker/schedule - The scheduled-publish alarm never checks the user's status, so a suspended user's already-queued posts still publish
- **Journeys:** J-128
- **Covers:** none (LR-013 and LR-014 are about the dropped userId and silent skips; LR-188 is about admin suspend edge cases)
- **Confidence:** confirmed-by-reading
- **Evidence:** worker/src/index.ts:4750-4800 (executeScheduledPublish has no checkUserAccess / status read); worker/src/scheduled-publish/ScheduledPublishAlarm.ts:85-100; status is only checked in worker/src/index.ts:3071 on the request path
- **Repro:** User U arms a post for 2 minutes ahead; admin clicks Suspend on U; wait for the alarm. Pass: no post goes out and the row records why. Today the alarm calls publishContent without any access check.
- **Fix hint:** Persist userId in the DO task (LR-013), then in executeScheduledPublish call checkUserAccess for that user and skip with a logged reason when suspended or removed; cancel the user's alarms when an admin suspends.

### JRN-003 P2 worker/tenancy - Deleting a topic removes images and D1 data before the sheet row, so a Sheets failure leaves the row visible with its media gone
- **Journeys:** J-039
- **Covers:** none (LR-073 is about trusting the client row index)
- **Confidence:** confirmed-by-reading
- **Evidence:** worker/src/index.ts:2289-2299 (deleteGcsObjectsForTopicRow, then Promise.all of D1 deletes, then sheets.deleteRow last)
- **Repro:** Make Sheets fail (revoke the share) and delete a topic. Expect the GCS images and pipeline_state row gone, the sheet row still present, and the topic reappearing as a sheet-only row on the next list. Pass: delete is all-or-nothing or the error tells the user what remains.
- **Fix hint:** Delete the sheet row first (or tolerate its absence), then D1 and GCS; return a partial-failure message if any step fails.

### JRN-004 P2 worker/db - When the Sheets merge fails, the topic list silently falls back to D1 rows with no signal to the user that the sheet is out of sync
- **Journeys:** J-129
- **Covers:** none (LR-091 is the feed load error state; LR-055 is addTopic)
- **Confidence:** confirmed-by-reading
- **Evidence:** worker/src/index.ts:1559-1569 (catch logs to console and returns pipeline.getRowsByUserId())
- **Repro:** Unshare the sheet from the service account, open the queue. Expect rows to load with no banner; edits then diverge from the sheet. Pass: a visible "sheet unavailable, showing saved copy" notice.
- **Fix hint:** Return a flag (for example sheetSyncOk:false) alongside the fallback rows and have the queue show a banner.

### JRN-005 P2 frontend/shell - An expired Google token signs the user out and unmounts the dashboard, so unsaved editor text can be lost
- **Journeys:** J-021
- **Covers:** LR-024, LR-106, LR-089 (closest; none says auth expiry drops the editor state)
- **Confidence:** hypothesis
- **Evidence:** frontend/src/App.tsx:374-380 (handleAuthExpired clears the token and sets session to null)
- **Repro:** Type in the editor without saving, expire the token (edit the stored id token), click Save. Pass: the text is still there after sign-in, or the user is warned before sign-out.
- **Fix hint:** Persist editor text to localStorage on change (LR-024 recovery path) and restore it after re-sign-in; or refresh the token instead of signing out.

## Rejected after reading the code

- J-045 (assignClipToPost does not check postId ownership): worker/src/db/clips.ts:169-195 and worker/src/index.ts:1865-1868 scope the clip by user_id; postId is stored only in that user's own clip row, so there is no cross-tenant effect.
- J-047 (fabricated debate article offered for Clip with no AI label): frontend/src/features/feed/components/DebateModeView.tsx:214 labels the generated card "AI-generated opposing perspective"; the Clip button at line 114 is on the real source article, not the generated one.
- J-132 (shared token saved before the encryption key is required): worker/src/index.ts:4218 calls requireSecretEncryptionKey inside persistLinkedInConnection before the KV put at 4221, so the flow fails before anything is saved. The swallowed per-user save failure is already LR-151.

## Covered by existing items

- J-003 -> LR-019, LR-020
- J-005 -> LR-129
- J-010 -> LR-180
- J-017 -> LR-009
- J-018 -> LR-160 (the access request endpoint is the waitlist handler, worker/src/modes/saas/waitlist.ts)
- J-021 -> new JRN-005
- J-022 -> LR-105
- J-028 -> LR-133
- J-030 -> LR-030
- J-031 -> LR-072, INV-006
- J-036 -> LR-060
- J-039 -> new JRN-003
- J-045 -> rejected
- J-047 -> rejected
- J-056 finding 1 -> new JRN-001
- J-056 finding 2 -> LR-056
- J-057 -> LR-016
- J-058 -> LR-060
- J-060 -> LR-050, INV-005
- J-067 -> LR-157
- J-072 -> LR-141
- J-075 -> LR-023
- J-083 A, B -> LR-013
- J-083 C -> LR-014
- J-084 -> LR-071
- J-086 -> LR-031
- J-087 -> LR-002, LR-014
- J-088 -> LR-070
- J-089 -> LR-070
- J-092 -> LR-014, LR-070, INV-020
- J-098 -> LR-034
- J-099 -> LR-108
- J-101 -> LR-034
- J-102 -> LR-012 (fallback to the shared token after disconnect)
- J-103 -> LR-012
- J-105 -> LR-012 (fix hint: throw when undecryptable)
- J-111 -> LR-053
- J-112 -> LR-010
- J-113 -> LR-187, INV-014
- J-115 -> LR-161
- J-116 -> LR-137, INV-007
- J-126 -> LR-051, INV-018
- J-127 -> LR-134, INV-004
- J-128 -> new JRN-002
- J-129 -> new JRN-004
- J-132 -> rejected (swallowed save failure is LR-151)
- J-135 -> LR-017
- J-136 -> LR-001
- J-141 -> LR-074
