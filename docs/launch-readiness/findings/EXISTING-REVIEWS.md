# Existing-review reconciliation items

One entry per row of launch-release/findings/raw/existing-reviews.md (all statuses). Aliases are the source row IDs. Read-only; nothing executed.

### CONS-001 P1 frontend/navigation - Sidebar grouped under Plan/Make/Ship/Configure/Admin
- **Source:** launch-release/findings/raw/existing-reviews.md section 1, row C01-1
- **Alias:** C01-1
- **Original tag:** HIGH (mapped to P1)
- **Current status:** open
- **Evidence:** components/workspace/AppSidebar.tsx (flat link() list, admin gating inline ~L269) (no group headers)
- **Covered by:** FZ-001

### CONS-002 P1 frontend/navigation - Breadcrumb in WorkspaceHeader
- **Source:** launch-release/findings/raw/existing-reviews.md section 1, row C01-2
- **Alias:** C01-2
- **Original tag:** HIGH (mapped to P1)
- **Current status:** partial
- **Evidence:** components/workspace/WorkspaceHeader.tsx:47; WorkspaceChromeContext.tsx:19 (only on topic-review routes via headerOverride, not derived from location)
- **Covered by:** FZ-001

### CONS-003 P2 frontend/navigation - ? help button / workflows modal
- **Source:** launch-release/findings/raw/existing-reviews.md section 1, row C01-3
- **Alias:** C01-3
- **Original tag:** MED (mapped to P2)
- **Current status:** partial
- **Evidence:** App.tsx:125-134, components/HelpOverlay.tsx:4-9 (? key opens shortcuts overlay; no visible header button, no workflows content)
- **Covered by:** FZ-001

### CONS-004 P2 frontend/navigation - Sidebar search
- **Source:** launch-release/findings/raw/existing-reviews.md section 1, row C01-4
- **Alias:** C01-4
- **Original tag:** MED (mapped to P2)
- **Current status:** open
- **Evidence:** AppSidebar.tsx (none)
- **Covered by:** FZ-001

### CONS-005 P2 frontend/navigation - useRouteContext hook
- **Source:** launch-release/findings/raw/existing-reviews.md section 1, row C01-5
- **Alias:** C01-5
- **Original tag:** MED (mapped to P2)
- **Current status:** open
- **Evidence:** grep: no hit
- **Covered by:** FZ-001

### CONS-006 P2 frontend/navigation - RecentlyViewed topics
- **Source:** launch-release/findings/raw/existing-reviews.md section 1, row C01-6
- **Alias:** C01-6
- **Original tag:** MED (mapped to P2)
- **Current status:** open
- **Evidence:** grep: no hit
- **Covered by:** FZ-001

### CONS-007 P2 frontend/navigation - Mobile sidebar scrim-tap Drawer
- **Source:** launch-release/findings/raw/existing-reviews.md section 1, row C01-7
- **Alias:** C01-7
- **Original tag:** MED (mapped to P2)
- **Current status:** unverified
- **Evidence:** AppSidebar.tsx mobileOpen props (not inspected)
- **Covered by:** none

### CONS-008 P1 frontend/navigation - Deep-link hard-refresh audit
- **Source:** launch-release/findings/raw/existing-reviews.md section 1, row C01-8
- **Alias:** C01-8
- **Original tag:** HIGH (mapped to P1)
- **Current status:** unverified
- **Evidence:** App.tsx:262 stored-path restore (mechanism exists (post-auth return path); no audit seen)
- **Covered by:** none

### CONS-009 P2 frontend/navigation - Global command palette (cmd+k)
- **Source:** launch-release/findings/raw/existing-reviews.md section 1, row C01-9
- **Alias:** C01-9
- **Original tag:** MED (mapped to P2)
- **Current status:** open
- **Evidence:** grep CommandPalette: none (Cmd-K only focuses settings nav search (DashboardSettingsDrawer.tsx:1225))
- **Covered by:** FZ-001

### CONS-010 P2 frontend/navigation - RouteGuard role wrapper
- **Source:** launch-release/findings/raw/existing-reviews.md section 1, row C01-10
- **Alias:** C01-10
- **Original tag:** MED (mapped to P2)
- **Current status:** open
- **Evidence:** grep: none (admin gating still inline)
- **Covered by:** FZ-001

### CONS-011 P1 frontend/feed - Feed: persistent 👍👎✂ (not hover)
- **Source:** launch-release/findings/raw/existing-reviews.md section 1, row C02-1
- **Alias:** C02-1
- **Original tag:** HIGH (mapped to P1)
- **Current status:** open
- **Evidence:** features/feed/components/FeedArticleCard.tsx:~97 (opacity-0 group-hover:opacity-100 pointer-events-none) (touch users cannot vote/clip from stream; 26px targets (<40px AC))
- **Covered by:** LR-095

### CONS-012 P1 frontend/feed - Favicon next to source
- **Source:** launch-release/findings/raw/existing-reviews.md section 1, row C02-2
- **Alias:** C02-2
- **Original tag:** HIGH (mapped to P1)
- **Current status:** fixed
- **Evidence:** FeedArticleCard.tsx:76-83
- **Covered by:** none

### CONS-013 P1 frontend/feed - Thumbnail 96px aspect-[4/3]
- **Source:** launch-release/findings/raw/existing-reviews.md section 1, row C02-3
- **Alias:** C02-3
- **Original tag:** HIGH (mapped to P1)
- **Current status:** open
- **Evidence:** FeedArticleCard.tsx (no img at all) (cards are text-only)
- **Covered by:** FZ-002

### CONS-014 P1 frontend/feed - 2-line summary default
- **Source:** launch-release/findings/raw/existing-reviews.md section 1, row C02-4
- **Alias:** C02-4
- **Original tag:** HIGH (mapped to P1)
- **Current status:** fixed
- **Evidence:** FeedArticleCard.tsx:~69 line-clamp-2 + content fallback
- **Covered by:** none

### CONS-015 P1 frontend/feed - Search input in feed (+desc toggle)
- **Source:** launch-release/findings/raw/existing-reviews.md section 1, row C02-5
- **Alias:** C02-5
- **Original tag:** MED/HIGH (mixed tag, higher taken: P1)
- **Current status:** partial
- **Evidence:** FeedPage.tsx:109-111, 536-575 (debounced client filter on loaded items) (no "search description" toggle)
- **Covered by:** FZ-002

### CONS-016 P2 frontend/feed - Source brand colour badge
- **Source:** launch-release/findings/raw/existing-reviews.md section 1, row C02-6
- **Alias:** C02-6
- **Original tag:** MED (mapped to P2)
- **Current status:** partial
- **Evidence:** FeedArticleCard.tsx:6-10,86 hash-colour square
- **Covered by:** none

### CONS-017 P2 frontend/feed - j/k/o/c keyboard nav
- **Source:** launch-release/findings/raw/existing-reviews.md section 1, row C02-7
- **Alias:** C02-7
- **Original tag:** MED (mapped to P2)
- **Current status:** fixed
- **Evidence:** features/feed/hooks/useFeedKeyboard.ts:38; FeedPage.tsx:586-596
- **Covered by:** none

### CONS-018 P2 frontend/feed - Batch 20 + append skeleton
- **Source:** launch-release/findings/raw/existing-reviews.md section 1, row C02-8
- **Alias:** C02-8
- **Original tag:** MED (mapped to P2)
- **Current status:** partial
- **Evidence:** FeedLeftPanel.tsx:39 BATCH_SIZE=20; :28,:116 skeletons (skeleton only on initial load; "Load more" fallback exists :206)
- **Covered by:** FZ-002

### CONS-019 P1 frontend/feed - Filter bar Latest/Trending/For You
- **Source:** launch-release/findings/raw/existing-reviews.md section 1, row C02-9
- **Alias:** C02-9
- **Original tag:** HIGH (mapped to P1)
- **Current status:** partial
- **Evidence:** FeedPage.tsx:56,522-534,1063 ("For You" = hide downvoted only (:530); no per-topic pill beyond interest groups)
- **Covered by:** FZ-002

### CONS-020 P1 frontend/feed - Two-panel layout, trending rail top carousel <lg
- **Source:** launch-release/findings/raw/existing-reviews.md section 1, row C02-10
- **Alias:** C02-10
- **Original tag:** HIGH (mapped to P1)
- **Current status:** open
- **Evidence:** FeedPage.tsx:1340 hidden lg:flex, no carousel (rail simply disappears on tablet/phone)
- **Covered by:** LR-095

### CONS-021 P1 frontend/feed - 2-col masonry
- **Source:** launch-release/findings/raw/existing-reviews.md section 1, row C02-11
- **Alias:** C02-11
- **Original tag:** HIGH (mapped to P1)
- **Current status:** open
- **Evidence:** FeedLeftPanel.tsx (single column)
- **Covered by:** FZ-002

### CONS-022 P2 frontend/feed - Detail as side-sheet not full-screen
- **Source:** launch-release/findings/raw/existing-reviews.md section 1, row C02-12
- **Alias:** C02-12
- **Original tag:** MED (mapped to P2)
- **Current status:** fixed
- **Evidence:** FeedPage.tsx:1375-1405 (480px sheet, asSheet) (overlay darkens feed (modal))
- **Covered by:** none

### CONS-023 P2 frontend/feed - Evergreen sort uses real signal
- **Source:** launch-release/findings/raw/existing-reviews.md section 1, row C02-13
- **Alias:** C02-13
- **Original tag:** MED (mapped to P2)
- **Current status:** open
- **Evidence:** FeedCuratedPanel.tsx:89-92,152-154 (description length) (Top10 also uses desc length + recency)
- **Covered by:** LR-174

### CONS-024 P2 frontend/feed - Source dedupe grouping
- **Source:** launch-release/findings/raw/existing-reviews.md section 1, row C02-14
- **Alias:** C02-14
- **Original tag:** MED (mapped to P2)
- **Current status:** open
- **Evidence:** FeedLeftPanel.tsx (none)
- **Covered by:** FZ-002

### CONS-025 P2 frontend/feed - Curated panel compact + trending-word chips
- **Source:** launch-release/findings/raw/existing-reviews.md section 1, row C02-15
- **Alias:** C02-15
- **Original tag:** MED (mapped to P2)
- **Current status:** partial
- **Evidence:** FeedCuratedPanel.tsx:279-285 (words/topics clickable (FeedPage.tsx:1363-1364))
- **Covered by:** FZ-002

### CONS-026 P2 frontend/feed - SaveForLater
- **Source:** launch-release/findings/raw/existing-reviews.md section 1, row C02-16
- **Alias:** C02-16
- **Original tag:** MED (mapped to P2)
- **Current status:** open
- **Evidence:** FeedArticleCard.tsx:~131 Bookmark button only calls stopPropagation (no-op button shipped (see NEW-1))
- **Covered by:** LR-173

### CONS-027 P2 frontend/feed - Compose post from article CTA on card
- **Source:** launch-release/findings/raw/existing-reviews.md section 1, row C02-17
- **Alias:** C02-17
- **Original tag:** MED (mapped to P2)
- **Current status:** open
- **Evidence:** FeedArticleCard.tsx
- **Covered by:** FZ-002

### CONS-028 P2 frontend/feed - Per-source mute/boost
- **Source:** launch-release/findings/raw/existing-reviews.md section 1, row C02-18
- **Alias:** C02-18
- **Original tag:** MED (mapped to P2)
- **Current status:** open
- **Evidence:** none given
- **Covered by:** FZ-002

### CONS-029 P1 frontend/clips - ClipsDock visible trash (not right-click)
- **Source:** launch-release/findings/raw/existing-reviews.md section 1, row C03-1
- **Alias:** C03-1
- **Original tag:** HIGH (mapped to P1)
- **Current status:** partial
- **Evidence:** features/feed/components/ClipsDock.tsx:206 onContextMenu confirm; hover-only Edit/Delete :~236 (delete still via right-click or hover buttons)
- **Covered by:** LR-175

### CONS-030 P1 frontend/clips - Drop-zone affordance + toast
- **Source:** launch-release/findings/raw/existing-reviews.md section 1, row C03-2
- **Alias:** C03-2
- **Original tag:** HIGH (mapped to P1)
- **Current status:** partial
- **Evidence:** ClipsDock.tsx:332-367 (dragOver highlight "Drop to assign") (no success toast on drop)
- **Covered by:** LR-175

### CONS-031 P1 frontend/clips - "Compose post from clips" CTA
- **Source:** launch-release/findings/raw/existing-reviews.md section 1, row C03-3
- **Alias:** C03-3
- **Original tag:** HIGH (mapped to P1)
- **Current status:** fixed
- **Evidence:** ClipsDock.tsx:133-145
- **Covered by:** none

### CONS-032 P1 frontend/clips - Floating pill dock, count badge
- **Source:** launch-release/findings/raw/existing-reviews.md section 1, row C03-4
- **Alias:** C03-4
- **Original tag:** HIGH (mapped to P1)
- **Current status:** partial
- **Evidence:** ClipsDock.tsx:158 (magnifying vertical strip + expand panel) (still always-on right strip)
- **Covered by:** none

### CONS-033 P2 frontend/clips - Bulk select clips
- **Source:** launch-release/findings/raw/existing-reviews.md section 1, row C03-5
- **Alias:** C03-5
- **Original tag:** MED (mapped to P2)
- **Current status:** open
- **Evidence:** ClipsDock.tsx
- **Covered by:** FZ-003

### CONS-034 P1 frontend/clips - Per-clip "Add to topic" menu (touch)
- **Source:** launch-release/findings/raw/existing-reviews.md section 1, row C03-6
- **Alias:** C03-6
- **Original tag:** HIGH/MED (mixed tag, higher taken: P1)
- **Current status:** open
- **Evidence:** ClipsDock.tsx (drag-drop only) (touch users cannot assign)
- **Covered by:** LR-095

### CONS-035 P1 frontend/clips - Passage clipping from stream (SelectionClipper in card)
- **Source:** launch-release/findings/raw/existing-reviews.md section 1, row C03-7
- **Alias:** C03-7
- **Original tag:** HIGH (mapped to P1)
- **Current status:** open
- **Evidence:** grep: SelectionClipper only used in ArticleDetailView.tsx:11,150 (cons doc says toast was added; toast exists (SelectionClipper.tsx:19-23) but card wiring absent)
- **Covered by:** FZ-003

### CONS-036 P2 frontend/clips - Detail: Read-full primary, lightbox, details wrapper, opinion textarea
- **Source:** launch-release/findings/raw/existing-reviews.md section 1, row C03-8
- **Alias:** C03-8
- **Original tag:** MED (mapped to P2)
- **Current status:** partial
- **Evidence:** ArticleDetailView.tsx:397,404 <details>; no lightbox grep hit
- **Covered by:** FZ-004

### CONS-037 P2 frontend/clips - Single scrollable stack vs tabs
- **Source:** launch-release/findings/raw/existing-reviews.md section 1, row C03-9
- **Alias:** C03-9
- **Original tag:** MED (mapped to P2)
- **Current status:** open
- **Evidence:** ArticleDetailView.tsx:134,472-557 (Opinion/Perspectives/Connection/Debate tabs)
- **Covered by:** FZ-004

### CONS-038 P2 frontend/clips - clipGroupId / groups
- **Source:** launch-release/findings/raw/existing-reviews.md section 1, row C03-10
- **Alias:** C03-10
- **Original tag:** MED (mapped to P2)
- **Current status:** open
- **Evidence:** grep: none
- **Covered by:** FZ-003

### CONS-039 P1 frontend/clips - Cached AI analysis on worker
- **Source:** launch-release/findings/raw/existing-reviews.md section 1, row C03-11
- **Alias:** C03-11
- **Original tag:** HIGH (mapped to P1)
- **Current status:** unverified
- **Evidence:** worker index.ts:1919 analyzeFeedArticle (cache not checked)
- **Covered by:** none

### CONS-040 P1 frontend/queue - Queue row primary CTA always visible
- **Source:** launch-release/findings/raw/existing-reviews.md section 1, row C04-1
- **Alias:** C04-1
- **Original tag:** HIGH (mapped to P1)
- **Current status:** fixed
- **Evidence:** components/dashboard/tabs/DashboardQueue.tsx:~852,896,925 (only delete column is dimmed (opacity-40, :942))
- **Covered by:** none

### CONS-041 P1 frontend/queue - Per-row channel pill
- **Source:** launch-release/findings/raw/existing-reviews.md section 1, row C04-2
- **Alias:** C04-2
- **Original tag:** HIGH (mapped to P1)
- **Current status:** open
- **Evidence:** DashboardQueue.tsx (only StatusPill at :768; CHANNEL_OPTIONS used only in bulk/confirm :1017,1274) (onboarding Tour copy at :435 claims "channel pill shows where a post will publish" - it does not)
- **Covered by:** LR-097

### CONS-042 P1 frontend/queue - Unified status pill
- **Source:** launch-release/findings/raw/existing-reviews.md section 1, row C04-3
- **Alias:** C04-3
- **Original tag:** HIGH (mapped to P1)
- **Current status:** fixed
- **Evidence:** components/ui/StatusPill.tsx; DashboardQueue.tsx:20,768 (adoption elsewhere (calendar, newsletter) unchecked)
- **Covered by:** none

### CONS-043 P1 frontend/queue - Empty state starter templates + tour
- **Source:** launch-release/findings/raw/existing-reviews.md section 1, row C04-4
- **Alias:** C04-4
- **Original tag:** HIGH (mapped to P1)
- **Current status:** fixed
- **Evidence:** DashboardQueue.tsx:431-435,585-588
- **Covered by:** none

### CONS-044 P1 frontend/queue - AddTopic save toast / "Saved Ns ago"
- **Source:** launch-release/findings/raw/existing-reviews.md section 1, row C04-5
- **Alias:** C04-5
- **Original tag:** HIGH (mapped to P1)
- **Current status:** open
- **Evidence:** features/add-topic/AddTopicPage.tsx:296 onSaved only; no toast system exists in app
- **Covered by:** LR-183

### CONS-045 P2 frontend/queue - Required-field asterisk + error summary
- **Source:** launch-release/findings/raw/existing-reviews.md section 1, row C04-6
- **Alias:** C04-6
- **Original tag:** MED (mapped to P2)
- **Current status:** partial
- **Evidence:** AddTopicPage.tsx:275 inline title error (no asterisk on title)
- **Covered by:** LR-178

### CONS-046 P2 frontend/queue - Persona delete visible + confirm
- **Source:** launch-release/findings/raw/existing-reviews.md section 1, row C04-7
- **Alias:** C04-7
- **Original tag:** MED (mapped to P2)
- **Current status:** unverified
- **Evidence:** AddTopicPage.tsx:~660-691
- **Covered by:** none

### CONS-047 P2 frontend/queue - Generate-with-AI determinate progress
- **Source:** launch-release/findings/raw/existing-reviews.md section 1, row C04-8
- **Alias:** C04-8
- **Original tag:** MED (mapped to P2)
- **Current status:** open
- **Evidence:** AddTopicPage.tsx
- **Covered by:** none

### CONS-048 P2 frontend/queue - Topic Duplicate action
- **Source:** launch-release/findings/raw/existing-reviews.md section 1, row C04-9
- **Alias:** C04-9
- **Original tag:** MED (mapped to P2)
- **Current status:** open
- **Evidence:** grep: none in AddTopicPage
- **Covered by:** none

### CONS-049 P2 frontend/queue - Merge Trending+Research tab, rename Analysis
- **Source:** launch-release/findings/raw/existing-reviews.md section 1, row C04-10
- **Alias:** C04-10
- **Original tag:** MED (mapped to P2)
- **Current status:** open
- **Evidence:** add-topic/TopicRightPanel.tsx:52-54 (still Trending/Research/Analysis)
- **Covered by:** none

### CONS-050 P3 frontend/queue - MicButton 3 states
- **Source:** launch-release/findings/raw/existing-reviews.md section 1, row C04-11
- **Alias:** C04-11
- **Original tag:** LOW (mapped to P3)
- **Current status:** partial
- **Evidence:** add-topic/MicButton.tsx:23,34,43 (spinner + stop label) (no pulsing recording dot verified)
- **Covered by:** none

### CONS-051 P1 frontend/queue - AI-Draft modal not nested in drawer
- **Source:** launch-release/findings/raw/existing-reviews.md section 1, row C04-12
- **Alias:** C04-12
- **Original tag:** HIGH (mapped to P1)
- **Current status:** fixed
- **Evidence:** DashboardQueue.tsx:161,187-220 (dialog owned by queue) (TopicDetailPanel is a separate overlay (:55))
- **Covered by:** none

### CONS-052 P1 frontend/queue - Deterministic drop-menu in AddTopic
- **Source:** launch-release/findings/raw/existing-reviews.md section 1, row C04-13
- **Alias:** C04-13
- **Original tag:** HIGH (mapped to P1)
- **Current status:** unverified
- **Evidence:** none given
- **Covered by:** none

### CONS-053 P2 frontend/queue - useTopicDraft localStorage hook
- **Source:** launch-release/findings/raw/existing-reviews.md section 1, row C04-14
- **Alias:** C04-14
- **Original tag:** MED (mapped to P2)
- **Current status:** open
- **Evidence:** grep: none
- **Covered by:** none

### CONS-054 P2 frontend/queue - List filters (status/channel/needs-action/sort)
- **Source:** launch-release/findings/raw/existing-reviews.md section 1, row C04-15
- **Alias:** C04-15
- **Original tag:** MED (mapped to P2)
- **Current status:** unverified
- **Evidence:** DashboardQueue.tsx (not inspected)
- **Covered by:** none

### CONS-055 P2 frontend/queue - Bulk select + bulk delete/reschedule/channel
- **Source:** launch-release/findings/raw/existing-reviews.md section 1, row C04-16
- **Alias:** C04-16
- **Original tag:** MED (mapped to P2)
- **Current status:** partial
- **Evidence:** DashboardQueue.tsx:146-149,755-760 (checkbox, bulk channel/schedule dialogs)
- **Covered by:** none

### CONS-056 P2 frontend/queue - Republish tooltip; no withdraw
- **Source:** launch-release/findings/raw/existing-reviews.md section 1, row C04-17
- **Alias:** C04-17
- **Original tag:** MED (mapped to P2)
- **Current status:** partial
- **Evidence:** DashboardQueue.tsx:925 title="Republish to channel" (tooltip does not say "creates new draft"; no withdraw)
- **Covered by:** LR-178

### CONS-057 P2 frontend/queue - "Drafting..." describes what is happening
- **Source:** launch-release/findings/raw/existing-reviews.md section 1, row C04-18
- **Alias:** C04-18
- **Original tag:** MED (mapped to P2)
- **Current status:** unverified
- **Evidence:** none given
- **Covered by:** none

### CONS-058 P1 frontend/schedule - datetime-local in EditorScreen -> ScheduleEditor
- **Source:** launch-release/findings/raw/existing-reviews.md section 1, row C05-1
- **Alias:** C05-1
- **Original tag:** HIGH (mapped to P1)
- **Current status:** open
- **Evidence:** features/review-editor/screens/EditorScreen.tsx:310 (editor still has bare input)
- **Covered by:** LR-169

### CONS-059 P1 frontend/schedule - TopicDetailPanel uses ScheduleEditor
- **Source:** launch-release/findings/raw/existing-reviews.md section 1, row C05-2
- **Alias:** C05-2
- **Original tag:** HIGH (mapped to P1)
- **Current status:** fixed
- **Evidence:** components/dashboard/components/TopicDetailPanel.tsx:369
- **Covered by:** none

### CONS-060 P1 frontend/schedule - Calendar uses ScheduleEditor
- **Source:** launch-release/findings/raw/existing-reviews.md section 1, row C05-3
- **Alias:** C05-3
- **Original tag:** HIGH (mapped to P1)
- **Current status:** fixed
- **Evidence:** content-schedule-calendar/ContentScheduleCalendar.tsx:367 (so 2 of 3 entry points unified; editor remains)
- **Covered by:** none

### CONS-061 P2 frontend/schedule - Timezone caption
- **Source:** launch-release/findings/raw/existing-reviews.md section 1, row C05-4
- **Alias:** C05-4
- **Original tag:** MED (mapped to P2)
- **Current status:** open
- **Evidence:** components/schedule/ScheduleEditor.tsx (no tz hit) (editor posts UTC string (useReviewFlowActions.ts:690-697))
- **Covered by:** LR-031

### CONS-062 P2 frontend/schedule - Mobile sticky footer in editor
- **Source:** launch-release/findings/raw/existing-reviews.md section 1, row C05-5
- **Alias:** C05-5
- **Original tag:** MED (mapped to P2)
- **Current status:** unverified
- **Evidence:** EditorScreen.tsx
- **Covered by:** none

### CONS-063 P2 frontend/schedule - Drag-confirm "these items will move" list
- **Source:** launch-release/findings/raw/existing-reviews.md section 1, row C05-6
- **Alias:** C05-6
- **Original tag:** MED (mapped to P2)
- **Current status:** unverified
- **Evidence:** content-schedule-calendar/EventDetailAndEdit.tsx
- **Covered by:** none

### CONS-064 P2 frontend/schedule - ScheduledPublishBanner abs+relative time, destructive Cancel
- **Source:** launch-release/findings/raw/existing-reviews.md section 1, row C05-7
- **Alias:** C05-7
- **Original tag:** MED (mapped to P2)
- **Current status:** partial
- **Evidence:** scheduled-publish/ScheduledPublishBanner.tsx:42-44 ("Cancel schedule") (no countdown)
- **Covered by:** LR-169

### CONS-065 P2 frontend/schedule - Recipient-missing warning in editor footer
- **Source:** launch-release/findings/raw/existing-reviews.md section 1, row C05-8
- **Alias:** C05-8
- **Original tag:** MED (mapped to P2)
- **Current status:** unverified
- **Evidence:** none given
- **Covered by:** none

### CONS-066 P1 frontend/schedule - Single ChannelPicker component
- **Source:** launch-release/findings/raw/existing-reviews.md section 1, row C05-9
- **Alias:** C05-9
- **Original tag:** HIGH (mapped to P1)
- **Current status:** fixed
- **Evidence:** components/channels (imported DashboardDelivery.tsx:7, TopicsRightRail.tsx:6,258,390) (bulk modal still separate (DashboardQueue.tsx:1017))
- **Covered by:** none

### CONS-067 P1 frontend/schedule - deliveryChannels[] multi-channel
- **Source:** launch-release/findings/raw/existing-reviews.md section 1, row C05-10
- **Alias:** C05-10
- **Original tag:** HIGH (mapped to P1)
- **Current status:** open
- **Evidence:** grep: none (single channel only)
- **Covered by:** FZ-005

### CONS-068 P2 frontend/schedule - Connection Health panel / Test connection
- **Source:** launch-release/findings/raw/existing-reviews.md section 1, row C05-11
- **Alias:** C05-11
- **Original tag:** MED (mapped to P2)
- **Current status:** open
- **Evidence:** grep ConnectionHealth/testConnection: none
- **Covered by:** FZ-006

### CONS-069 P2 frontend/schedule - Calendar pending-publish state
- **Source:** launch-release/findings/raw/existing-reviews.md section 1, row C05-12
- **Alias:** C05-12
- **Original tag:** MED (mapped to P2)
- **Current status:** unverified
- **Evidence:** none given
- **Covered by:** none

### CONS-070 P1 frontend/schedule - Recurrence/rrule, per-channel timing
- **Source:** launch-release/findings/raw/existing-reviews.md section 1, row C05-13
- **Alias:** C05-13
- **Original tag:** HIGH (mapped to P1)
- **Current status:** n-a
- **Evidence:** future phase
- **Covered by:** none

### CONS-071 P1 frontend/editor - EditorSidebar 8 tabs -> 3 groups
- **Source:** launch-release/findings/raw/existing-reviews.md section 1, row C06-1
- **Alias:** C06-1
- **Original tag:** HIGH (mapped to P1)
- **Current status:** partial
- **Evidence:** features/review-editor/components/EditorSidebar.tsx:91-98 (now 5 base tabs (+Email) not 3 groups)
- **Covered by:** FZ-008

### CONS-072 P1 frontend/editor - Dimension slider ? tooltips
- **Source:** launch-release/findings/raw/existing-reviews.md section 1, row C06-2
- **Alias:** C06-2
- **Original tag:** HIGH (mapped to P1)
- **Current status:** open
- **Evidence:** EditorSidebar.tsx:25-35,360-400 (only label + level pill)
- **Covered by:** LR-170

### CONS-073 P1 frontend/editor - Three discard dialogs differentiated
- **Source:** launch-release/findings/raw/existing-reviews.md section 1, row C06-3
- **Alias:** C06-3
- **Original tag:** HIGH (mapped to P1)
- **Current status:** open
- **Evidence:** features/review/components/ReviewDialogs.tsx:60,95,110 all "Discard current editor changes?"
- **Covered by:** LR-089

### CONS-074 P1 frontend/editor - Passive autosave restore
- **Source:** launch-release/findings/raw/existing-reviews.md section 1, row C06-4
- **Alias:** C06-4
- **Original tag:** HIGH (mapped to P1)
- **Current status:** fixed
- **Evidence:** ReviewDialogs.tsx:43 "Restore previous draft?"; useReviewFlowState.ts:645 autoSaveTrigger
- **Covered by:** none

### CONS-075 P1 frontend/editor - beforeunload in editor
- **Source:** launch-release/findings/raw/existing-reviews.md section 1, row C06-5
- **Alias:** C06-5
- **Original tag:** HIGH (mapped to P1)
- **Current status:** open
- **Evidence:** grep beforeunload: only DashboardSettingsDrawer.tsx:1242 (leaving editor with unsaved edits is unguarded at browser level)
- **Covered by:** LR-089

### CONS-076 P2 frontend/editor - Variant badge font + tooltip
- **Source:** launch-release/findings/raw/existing-reviews.md section 1, row C06-6
- **Alias:** C06-6
- **Original tag:** MED (mapped to P2)
- **Current status:** unverified
- **Evidence:** variant/components/VariantCarousel.tsx
- **Covered by:** none

### CONS-077 P2 frontend/editor - ResizeHandle a11y
- **Source:** launch-release/findings/raw/existing-reviews.md section 1, row C06-7
- **Alias:** C06-7
- **Original tag:** MED (mapped to P2)
- **Current status:** unverified
- **Evidence:** EditorScreen.tsx:24-29
- **Covered by:** none

### CONS-078 P1 frontend/editor - Flip split to editor 60-65%
- **Source:** launch-release/findings/raw/existing-reviews.md section 1, row C06-8
- **Alias:** C06-8
- **Original tag:** HIGH (mapped to P1)
- **Current status:** open
- **Evidence:** EditorScreen.tsx:234,244 (sidebar 58%, editor 42%)
- **Covered by:** FZ-008

### CONS-079 P2 frontend/editor - Versions as toolbar drawer
- **Source:** launch-release/findings/raw/existing-reviews.md section 1, row C06-9
- **Alias:** C06-9
- **Original tag:** MED (mapped to P2)
- **Current status:** open
- **Evidence:** review-editor/components/VersionHistoryStrip.tsx
- **Covered by:** FZ-008

### CONS-080 P2 frontend/editor - Variant compare 2-up
- **Source:** launch-release/findings/raw/existing-reviews.md section 1, row C06-10
- **Alias:** C06-10
- **Original tag:** MED (mapped to P2)
- **Current status:** partial
- **Evidence:** ReviewDialogs.tsx:133 compare preview
- **Covered by:** FZ-008

### CONS-081 P2 frontend/editor - Edit-selection vs whole toggle
- **Source:** launch-release/findings/raw/existing-reviews.md section 1, row C06-11
- **Alias:** C06-11
- **Original tag:** MED (mapped to P2)
- **Current status:** partial
- **Evidence:** editor/DraftEditor scope toolbar (USE-CASES step 6) (not verified)
- **Covered by:** FZ-008

### CONS-082 P1 frontend/publish - Confirm modal before publish (rendered preview+channel+time)
- **Source:** launch-release/findings/raw/existing-reviews.md section 1, row C07-1
- **Alias:** C07-1
- **Original tag:** HIGH (mapped to P1)
- **Current status:** partial
- **Evidence:** DashboardQueue.tsx:163,852,896,1274 (queue has publishConfirmRow) (editor footer "Publish to X" calls handlePublishNow directly (EditorScreen.tsx:~393; useReviewFlowActions.ts:~700) - no confirm)
- **Covered by:** LR-026

### CONS-083 P1 frontend/publish - Success toast with "View on channel" permalink
- **Source:** launch-release/findings/raw/existing-reviews.md section 1, row C07-2
- **Alias:** C07-2
- **Original tag:** HIGH (mapped to P1)
- **Current status:** open
- **Evidence:** useDashboardQueue.ts:587 modal showAlert 'Success'; grep permalink: none for publish (USE-CASES claims link; not present)
- **Covered by:** LR-088

### CONS-084 P1 frontend/publish - Scheduled state copy + "Send now anyway"
- **Source:** launch-release/findings/raw/existing-reviews.md section 1, row C07-3
- **Alias:** C07-3
- **Original tag:** HIGH (mapped to P1)
- **Current status:** open
- **Evidence:** EditorScreen.tsx:~397 (button just disabled with tooltip)
- **Covered by:** LR-169

### CONS-085 P1 frontend/publish - Footer regroup Save/Schedule/Send
- **Source:** launch-release/findings/raw/existing-reviews.md section 1, row C07-4
- **Alias:** C07-4
- **Original tag:** HIGH (mapped to P1)
- **Current status:** open
- **Evidence:** EditorScreen.tsx:340-430 (Approve, Save edits, Publish, Save draft all present)
- **Covered by:** LR-026

### CONS-086 P2 frontend/publish - Live countdown on banner
- **Source:** launch-release/findings/raw/existing-reviews.md section 1, row C07-5
- **Alias:** C07-5
- **Original tag:** MED (mapped to P2)
- **Current status:** open
- **Evidence:** ScheduledPublishBanner.tsx
- **Covered by:** LR-169

### CONS-087 P1 frontend/publish - Merge Approve+Publish semantics
- **Source:** launch-release/findings/raw/existing-reviews.md section 1, row C07-6
- **Alias:** C07-6
- **Original tag:** HIGH (mapped to P1)
- **Current status:** open
- **Evidence:** EditorScreen.tsx:357,382 handleApprove still in footer
- **Covered by:** LR-026

### CONS-088 P1 frontend/publish - Undo send window
- **Source:** launch-release/findings/raw/existing-reviews.md section 1, row C07-7
- **Alias:** C07-7
- **Original tag:** HIGH (mapped to P1)
- **Current status:** open
- **Evidence:** grep revoke/undo send: none
- **Covered by:** FZ-007

### CONS-089 P2 frontend/publish - Multi-channel chips
- **Source:** launch-release/findings/raw/existing-reviews.md section 1, row C07-8
- **Alias:** C07-8
- **Original tag:** MED (mapped to P2)
- **Current status:** open
- **Evidence:** depends C05-10
- **Covered by:** FZ-005

### CONS-090 P1 frontend/newsletter - Newsletter live preview (desktop/mobile)
- **Source:** launch-release/findings/raw/existing-reviews.md section 1, row C08-1
- **Alias:** C08-1
- **Original tag:** HIGH (mapped to P1)
- **Current status:** fixed
- **Evidence:** campaign/components/newsletter/NewsletterConfigDrawer.tsx:44-51,97-101,192-200 ([x] in doc is correct)
- **Covered by:** none

### CONS-091 P1 frontend/newsletter - Inline validation (name/subject/emails)
- **Source:** launch-release/findings/raw/existing-reviews.md section 1, row C08-2
- **Alias:** C08-2
- **Original tag:** HIGH (mapped to P1)
- **Current status:** partial
- **Evidence:** NewsletterConfigDrawer.tsx:125-137 (no char counts verified)
- **Covered by:** LR-176

### CONS-092 P1 frontend/newsletter - Approve/Send always visible
- **Source:** launch-release/findings/raw/existing-reviews.md section 1, row C08-3
- **Alias:** C08-3
- **Original tag:** HIGH (mapped to P1)
- **Current status:** unverified
- **Evidence:** NewsletterListView.tsx / NewsletterCard.tsx (doc ticks it [x]; not confirmed in code)
- **Covered by:** none

### CONS-093 P1 frontend/newsletter - Mini-calendar >=220px
- **Source:** launch-release/findings/raw/existing-reviews.md section 1, row C08-4
- **Alias:** C08-4
- **Original tag:** HIGH (mapped to P1)
- **Current status:** unverified
- **Evidence:** NewsletterCalendarView.tsx (doc ticks [x]; not confirmed)
- **Covered by:** none

### CONS-094 P2 frontend/newsletter - Voice&Topics collapsed summary chip
- **Source:** launch-release/findings/raw/existing-reviews.md section 1, row C08-5
- **Alias:** C08-5
- **Original tag:** MED (mapped to P2)
- **Current status:** open
- **Evidence:** NewsletterConfigDrawer.tsx (no "Tone:" hit)
- **Covered by:** FZ-009

### CONS-095 P2 frontend/newsletter - Send test to me
- **Source:** launch-release/findings/raw/existing-reviews.md section 1, row C08-6
- **Alias:** C08-6
- **Original tag:** MED (mapped to P2)
- **Current status:** fixed
- **Evidence:** NewsletterConfigDrawer.tsx:187,304-308
- **Covered by:** none

### CONS-096 P2 frontend/newsletter - Subject {{variable}} autocomplete / end-to-end vars
- **Source:** launch-release/findings/raw/existing-reviews.md section 1, row C08-7
- **Alias:** C08-7
- **Original tag:** MED (mapped to P2)
- **Current status:** open
- **Evidence:** grep {{subscriber: none (doc itself leaves "[ ] Subject template variables work end-to-end")
- **Covered by:** LR-176

### CONS-097 P1 frontend/newsletter - Full-page editor vs drawer
- **Source:** launch-release/findings/raw/existing-reviews.md section 1, row C08-8
- **Alias:** C08-8
- **Original tag:** HIGH (mapped to P1)
- **Current status:** open
- **Evidence:** still drawer
- **Covered by:** FZ-009

### CONS-098 P1 frontend/newsletter - Dedicated issue view
- **Source:** launch-release/findings/raw/existing-reviews.md section 1, row C08-9
- **Alias:** C08-9
- **Original tag:** HIGH (mapped to P1)
- **Current status:** partial
- **Evidence:** newsletter/IssueDetailDrawer.tsx, NewsletterIssuePanel.tsx exist (still drawer-based)
- **Covered by:** FZ-009

### CONS-099 P2 frontend/newsletter - CodeMirror for HTML
- **Source:** launch-release/findings/raw/existing-reviews.md section 1, row C08-10
- **Alias:** C08-10
- **Original tag:** MED (mapped to P2)
- **Current status:** open
- **Evidence:** grep: none
- **Covered by:** FZ-009

### CONS-100 P2 frontend/newsletter - Status badge redesign
- **Source:** launch-release/findings/raw/existing-reviews.md section 1, row C08-11
- **Alias:** C08-11
- **Original tag:** MED (mapped to P2)
- **Current status:** unverified
- **Evidence:** none given
- **Covered by:** none

### CONS-101 P1 frontend/newsletter - Subject A/B, analytics, segmentation
- **Source:** launch-release/findings/raw/existing-reviews.md section 1, row C08-12
- **Alias:** C08-12
- **Original tag:** HIGH (mapped to P1)
- **Current status:** n-a
- **Evidence:** future phase
- **Covered by:** FZ-009

### CONS-102 P1 frontend/settings - Settings -> /settings page w/ left nav
- **Source:** launch-release/findings/raw/existing-reviews.md section 1, row C09-1
- **Alias:** C09-1
- **Original tag:** HIGH (mapped to P1)
- **Current status:** partial
- **Evidence:** DashboardSettingsDrawer.tsx (2251 lines; left nav + grouped list ~L1285-1390; /settings route exists) (still a monolith component; not split per section)
- **Covered by:** LR-179

### CONS-103 P1 frontend/settings - URL subpaths /settings/llm
- **Source:** launch-release/findings/raw/existing-reviews.md section 1, row C09-2
- **Alias:** C09-2
- **Original tag:** HIGH (mapped to P1)
- **Current status:** open
- **Evidence:** grep: none
- **Covered by:** LR-179

### CONS-104 P1 frontend/settings - Cmd-K settings search
- **Source:** launch-release/findings/raw/existing-reviews.md section 1, row C09-3
- **Alias:** C09-3
- **Original tag:** HIGH (mapped to P1)
- **Current status:** fixed
- **Evidence:** DashboardSettingsDrawer.tsx:1225-1228,1305 (scoped to settings only)
- **Covered by:** none

### CONS-105 P1 frontend/settings - Unsaved-changes guard
- **Source:** launch-release/findings/raw/existing-reviews.md section 1, row C09-4
- **Alias:** C09-4
- **Original tag:** HIGH (mapped to P1)
- **Current status:** partial
- **Evidence:** DashboardSettingsDrawer.tsx:1235-1244 beforeunload; :1247-1256 saved toast (no in-app route-change guard; save only for admin (:1282))
- **Covered by:** LR-179

### CONS-106 P1 frontend/settings - Section one-line descriptions
- **Source:** launch-release/findings/raw/existing-reviews.md section 1, row C09-5
- **Alias:** C09-5
- **Original tag:** HIGH (mapped to P1)
- **Current status:** open
- **Evidence:** SettingsSectionCard titles only (e.g. :1417,1441) (descriptions exist for a few model lists only)
- **Covered by:** LR-179

### CONS-107 P1 frontend/settings - Test connection per credential
- **Source:** launch-release/findings/raw/existing-reviews.md section 1, row C09-6
- **Alias:** C09-6
- **Original tag:** HIGH (mapped to P1)
- **Current status:** open
- **Evidence:** grep: none (frontend/worker) (highest support-cost item)
- **Covered by:** FZ-006

### CONS-108 P1 frontend/settings - Enrichment skill tooltips
- **Source:** launch-release/findings/raw/existing-reviews.md section 1, row C09-7
- **Alias:** C09-7
- **Original tag:** HIGH (mapped to P1)
- **Current status:** partial
- **Evidence:** DashboardSettingsDrawer.tsx:481-492 shows meta.description
- **Covered by:** none

### CONS-109 P1 frontend/settings - Sticky ToC
- **Source:** launch-release/findings/raw/existing-reviews.md section 1, row C09-8
- **Alias:** C09-8
- **Original tag:** HIGH (mapped to P1)
- **Current status:** fixed
- **Evidence:** DashboardSettingsDrawer.tsx ~L1317-1390
- **Covered by:** none

### CONS-110 P1 frontend/settings - Setup wizard progress "Step N of M"
- **Source:** launch-release/findings/raw/existing-reviews.md section 1, row C09-9
- **Alias:** C09-9
- **Original tag:** HIGH (mapped to P1)
- **Current status:** fixed
- **Evidence:** features/setup-wizard/SetupWizard.tsx:91-105
- **Covered by:** none

### CONS-111 P1 frontend/settings - Wizard label rename
- **Source:** launch-release/findings/raw/existing-reviews.md section 1, row C09-10
- **Alias:** C09-10
- **Original tag:** HIGH (mapped to P1)
- **Current status:** fixed
- **Evidence:** SetupWizard.tsx:77-89 ("Trending Sources","Image Generation","Voice Transcription")
- **Covered by:** none

### CONS-112 P1 frontend/settings - Wizard Back buttons
- **Source:** launch-release/findings/raw/existing-reviews.md section 1, row C09-11
- **Alias:** C09-11
- **Original tag:** HIGH (mapped to P1)
- **Current status:** fixed
- **Evidence:** SetupWizard.tsx:538-636; EnvVarsStep.tsx:438
- **Covered by:** none

### CONS-113 P1 frontend/settings - EnvVars grouped w/ docs links
- **Source:** launch-release/findings/raw/existing-reviews.md section 1, row C09-12
- **Alias:** C09-12
- **Original tag:** HIGH (mapped to P1)
- **Current status:** fixed
- **Evidence:** EnvVarsStep.tsx:456-532 (groups + links) (example values not verified)
- **Covered by:** none

### CONS-114 P2 frontend/settings - Save diff toast, inline validators (Telegram ID etc.)
- **Source:** launch-release/findings/raw/existing-reviews.md section 1, row C09-13
- **Alias:** C09-13
- **Original tag:** MED (mapped to P2)
- **Current status:** open
- **Evidence:** useDashboardSettings.ts; no regex hits
- **Covered by:** LR-179

### CONS-115 P2 frontend/settings - ChannelSettingsCard extraction
- **Source:** launch-release/findings/raw/existing-reviews.md section 1, row C09-14
- **Alias:** C09-14
- **Original tag:** MED (mapped to P2)
- **Current status:** open
- **Evidence:** grep: none (6 channel sections still copy/paste)
- **Covered by:** LR-179

### CONS-116 P2 frontend/settings - Connection health page
- **Source:** launch-release/findings/raw/existing-reviews.md section 1, row C09-15
- **Alias:** C09-15
- **Original tag:** MED (mapped to P2)
- **Current status:** open
- **Evidence:** pages/connections exists (OAuth cards) but no last-error/retry
- **Covered by:** FZ-006

### CONS-117 P2 frontend/settings - Deployment-mode card comparison
- **Source:** launch-release/findings/raw/existing-reviews.md section 1, row C09-16
- **Alias:** C09-16
- **Original tag:** MED (mapped to P2)
- **Current status:** unverified
- **Evidence:** SetupWizard.tsx:28,64
- **Covered by:** none

### CONS-118 P3 frontend/settings - Copy install logs button
- **Source:** launch-release/findings/raw/existing-reviews.md section 1, row C09-17
- **Alias:** C09-17
- **Original tag:** LOW (mapped to P3)
- **Current status:** open
- **Evidence:** none given
- **Covered by:** none

### CONS-119 P1 frontend/enrichment - Progress to non-admins in editor
- **Source:** launch-release/findings/raw/existing-reviews.md section 1, row C10-1
- **Alias:** C10-1
- **Original tag:** HIGH (mapped to P1)
- **Current status:** fixed
- **Evidence:** EditorSidebar.tsx:417; GenerationPanel.tsx:312 (EnrichmentProgressPanel)
- **Covered by:** none

### CONS-120 P1 frontend/enrichment - Node-failure warning toast + re-run
- **Source:** launch-release/findings/raw/existing-reviews.md section 1, row C10-2
- **Alias:** C10-2
- **Original tag:** HIGH (mapped to P1)
- **Current status:** open
- **Evidence:** EnrichmentProgressPanel.tsx (no failed/rerun hits)
- **Covered by:** LR-171

### CONS-121 P1 frontend/enrichment - nodeProgressLabels full coverage
- **Source:** launch-release/findings/raw/existing-reviews.md section 1, row C10-3
- **Alias:** C10-3
- **Original tag:** HIGH (mapped to P1)
- **Current status:** unverified
- **Evidence:** features/generation/nodeProgressLabels.ts
- **Covered by:** none

### CONS-122 P1 frontend/enrichment - DAG page for standard users
- **Source:** launch-release/findings/raw/existing-reviews.md section 1, row C10-4
- **Alias:** C10-4
- **Original tag:** HIGH (mapped to P1)
- **Current status:** open
- **Evidence:** AppSidebar.tsx:269 admin-only
- **Covered by:** FZ-013

### CONS-123 P1 frontend/enrichment - Re-run from node / edit-prompt deep link
- **Source:** launch-release/findings/raw/existing-reviews.md section 1, row C10-5
- **Alias:** C10-5
- **Original tag:** HIGH (mapped to P1)
- **Current status:** open
- **Evidence:** pages/EnrichmentFlowPage.tsx
- **Covered by:** FZ-013

### CONS-124 P2 frontend/enrichment - Last-3 runs expanded, filters, metrics
- **Source:** launch-release/findings/raw/existing-reviews.md section 1, row C10-6
- **Alias:** C10-6
- **Original tag:** MED (mapped to P2)
- **Current status:** open
- **Evidence:** EnrichmentFlowPage.tsx
- **Covered by:** FZ-013

### CONS-125 P2 frontend/enrichment - Persist generationProgress
- **Source:** launch-release/findings/raw/existing-reviews.md section 1, row C10-7
- **Alias:** C10-7
- **Original tag:** MED (mapped to P2)
- **Current status:** unverified
- **Evidence:** none given
- **Covered by:** none

### CONS-126 P1 frontend/signals - Log variant pick signal
- **Source:** launch-release/findings/raw/existing-reviews.md section 1, row C11-1
- **Alias:** C11-1
- **Original tag:** HIGH (mapped to P1)
- **Current status:** open
- **Evidence:** worker index.ts: no pick-logging case
- **Covered by:** FZ-010

### CONS-127 P1 frontend/signals - Feed 👍/👎 persisted
- **Source:** launch-release/findings/raw/existing-reviews.md section 1, row C11-2
- **Alias:** C11-2
- **Original tag:** HIGH (mapped to P1)
- **Current status:** fixed
- **Evidence:** worker index.ts:1812 setArticleFeedback, :1823 get; FeedPage.tsx:1280
- **Covered by:** none

### CONS-128 P1 frontend/signals - Post-publish "was this good?" rating
- **Source:** launch-release/findings/raw/existing-reviews.md section 1, row C11-3
- **Alias:** C11-3
- **Original tag:** HIGH (mapped to P1)
- **Current status:** open
- **Evidence:** grep: none
- **Covered by:** FZ-010

### CONS-129 P1 frontend/signals - Pre-apply diff in GenerationPanel
- **Source:** launch-release/findings/raw/existing-reviews.md section 1, row C11-4
- **Alias:** C11-4
- **Original tag:** HIGH (mapped to P1)
- **Current status:** partial
- **Evidence:** ReviewDialogs.tsx:133 compare preview exists for editor scope (GenerationPanel diff not verified)
- **Covered by:** none

### CONS-130 P1 frontend/admin - Admin: replace prompt() budget edit
- **Source:** launch-release/findings/raw/existing-reviews.md section 1, row C12-1
- **Alias:** C12-1
- **Original tag:** HIGH (mapped to P1)
- **Current status:** open
- **Evidence:** features/saas/AdminPanel.tsx:79 (native prompt; silently returns on invalid input)
- **Covered by:** LR-100

### CONS-131 P1 frontend/admin - Admin: Deny waitlist
- **Source:** launch-release/findings/raw/existing-reviews.md section 1, row C12-2
- **Alias:** C12-2
- **Original tag:** HIGH (mapped to P1)
- **Current status:** open
- **Evidence:** AdminPanel.tsx:172-... only Approve (:69); no deny endpoint in worker/service
- **Covered by:** LR-100

### CONS-132 P1 frontend/admin - Admin: search/sort/batch/audit/CSV
- **Source:** launch-release/findings/raw/existing-reviews.md section 1, row C12-3
- **Alias:** C12-3
- **Original tag:** HIGH/MED (mixed tag, higher taken: P1)
- **Current status:** open
- **Evidence:** AdminPanel.tsx (278 lines, none)
- **Covered by:** FZ-011

### CONS-133 P1 frontend/errors - Strip backend URL / technical hints from user errors
- **Source:** launch-release/findings/raw/existing-reviews.md section 1, row C13-1
- **Alias:** C13-1
- **Original tag:** HIGH (mapped to P1)
- **Current status:** open
- **Evidence:** services/backendApi.ts:485-525 (shows CORS_ALLOWED_ORIGINS, workers.dev, endpoint) (leaks infra detail to end users)
- **Covered by:** LR-110

### CONS-134 P1 frontend/errors - OfflineBanner
- **Source:** launch-release/findings/raw/existing-reviews.md section 1, row C13-2
- **Alias:** C13-2
- **Original tag:** HIGH (mapped to P1)
- **Current status:** open
- **Evidence:** grep online/offline: none
- **Covered by:** LR-111

### CONS-135 P1 frontend/errors - ErrorBanner/EmptyState/LoadingSkeleton primitives adopted
- **Source:** launch-release/findings/raw/existing-reviews.md section 1, row C13-3
- **Alias:** C13-3
- **Original tag:** HIGH (mapped to P1)
- **Current status:** partial
- **Evidence:** components/ui/ErrorBanner.tsx, EmptyState.tsx, LoadingSkeleton.tsx exist; **zero imports elsewhere** (dead code)
- **Covered by:** LR-111

### CONS-136 P1 frontend/errors - Retry action on failures (useAlert)
- **Source:** launch-release/findings/raw/existing-reviews.md section 1, row C13-4
- **Alias:** C13-4
- **Original tag:** HIGH (mapped to P1)
- **Current status:** open
- **Evidence:** components/useAlert.ts / AlertProvider.tsx (modal alert, no actions)
- **Covered by:** LR-111

### CONS-137 P1 frontend/errors - 401/429/5xx copy map; Retry-After backoff
- **Source:** launch-release/findings/raw/existing-reviews.md section 1, row C13-5
- **Alias:** C13-5
- **Original tag:** HIGH (mapped to P1)
- **Current status:** open
- **Evidence:** services/backendApi.ts: no backoff/Retry-After
- **Covered by:** LR-111

### CONS-138 P1 frontend/errors - zod validation
- **Source:** launch-release/findings/raw/existing-reviews.md section 1, row C13-6
- **Alias:** C13-6
- **Original tag:** HIGH (mapped to P1)
- **Current status:** open
- **Evidence:** grep from 'zod' in frontend: none
- **Covered by:** FZ-012

### CONS-139 P1 frontend/errors - Mobile parity (rail, drawer, bulk table scroll)
- **Source:** launch-release/findings/raw/existing-reviews.md section 1, row C13-7
- **Alias:** C13-7
- **Original tag:** HIGH (mapped to P1)
- **Current status:** partial
- **Evidence:** CampaignPage.tsx:852 overflow-x-auto; feed rail hidden (C02-10); settings drawer not verified
- **Covered by:** LR-095

### CONS-140 P2 frontend/errors - A11y labels / focus rings
- **Source:** launch-release/findings/raw/existing-reviews.md section 1, row C13-8
- **Alias:** C13-8
- **Original tag:** MED (mapped to P2)
- **Current status:** partial
- **Evidence:** ~175 aria-label occurrences; feed toolbar buttons labelled (no audit evidence)
- **Covered by:** LR-177

### CONS-141 P2 frontend/errors - Global shortcuts g+t/g+f/?
- **Source:** launch-release/findings/raw/existing-reviews.md section 1, row C13-9
- **Alias:** C13-9
- **Original tag:** MED (mapped to P2)
- **Current status:** fixed
- **Evidence:** App.tsx:126; components/HelpOverlay.tsx:4-9; hooks/useGlobalShortcuts.ts
- **Covered by:** none

### CONS-142 P2 frontend/errors - Telemetry / report-issue / self-healing
- **Source:** launch-release/findings/raw/existing-reviews.md section 1, row C13-10
- **Alias:** C13-10
- **Original tag:** MED (mapped to P2)
- **Current status:** n-a
- **Evidence:** future phase
- **Covered by:** none

### CONS-143 P3 frontend/errors - First-visit tours
- **Source:** launch-release/findings/raw/existing-reviews.md section 1, row C13-11
- **Alias:** C13-11
- **Original tag:** LOW (mapped to P3)
- **Current status:** partial
- **Evidence:** components/Tour.tsx used in DashboardQueue.tsx:431; feed tour FeedPage.tsx:622 (newsletter tour at NewsletterTab.tsx:229)
- **Covered by:** none

### CONS-144 P1 frontend/schedule - Bulk campaign: 3-mode import, file upload
- **Source:** launch-release/findings/raw/existing-reviews.md section 1, row C05b
- **Alias:** C05b
- **Original tag:** HIGH (mapped to P1)
- **Current status:** fixed
- **Evidence:** campaign/CampaignPage.tsx:70,591-603 (Prompt/File/Paste) (audits/05)
- **Covered by:** none

### CONS-145 P1 frontend/schedule - Bulk: inline column schedule/channel (not modals)
- **Source:** launch-release/findings/raw/existing-reviews.md section 1, row C05c
- **Alias:** C05c
- **Original tag:** HIGH (mapped to P1)
- **Current status:** open
- **Evidence:** CampaignPage.tsx:305-308,379-420 dialogs (audits/05)
- **Covered by:** LR-165

### CONS-146 P2 frontend/schedule - Bulk: draft persistence, undo delete
- **Source:** launch-release/findings/raw/existing-reviews.md section 1, row C05d
- **Alias:** C05d
- **Original tag:** MED (mapped to P2)
- **Current status:** fixed
- **Evidence:** CampaignPage.tsx:247-251 localStorage; :469 undo text (audits/05)
- **Covered by:** none

### CONS-147 P2 frontend/schedule - Bulk: template gallery, JSON diff panel
- **Source:** launch-release/findings/raw/existing-reviews.md section 1, row C05e
- **Alias:** C05e
- **Original tag:** MED (mapped to P2)
- **Current status:** open
- **Evidence:** none given (audits/05)
- **Covered by:** LR-165

### CONS-148 P1 frontend/strategy - Phase-3 strategic (personalisation model, closed-loop tuning, A/B recipe, cost dashboard, recurrence, collab)
- **Source:** launch-release/findings/raw/existing-reviews.md section 1, row C-F
- **Alias:** C-F
- **Original tag:** HIGH/MED (mixed tag, higher taken: P1)
- **Current status:** n-a
- **Evidence:** none given (future phase, not itemised)
- **Covered by:** none

### UC-001 P2 frontend/channels - WhatsApp card on /connections
- **Source:** launch-release/findings/raw/existing-reviews.md section 2, row U-052/041
- **Alias:** U-052/041
- **Original tag:** ✅ (no severity given, defaulted to P2)
- **Current status:** fixed
- **Evidence:** pages/connections/ConnectionsPage.tsx:22,60
- **Covered by:** none

### UC-002 P2 frontend/channels - Telegram verification on /connections
- **Source:** launch-release/findings/raw/existing-reviews.md section 2, row U-053
- **Alias:** U-053
- **Original tag:** ✅ (no severity given, defaulted to P2)
- **Current status:** fixed
- **Evidence:** ConnectionsPage.tsx:7,15,23 verifyTelegramChat (worker index.ts:2388)
- **Covered by:** none

### UC-003 P2 frontend/use-cases - listRules/lookupEffectiveRule use checkedFetch
- **Source:** launch-release/findings/raw/existing-reviews.md section 2, row U-057/060
- **Alias:** U-057/060
- **Original tag:** ✅ (no severity given, defaulted to P2)
- **Current status:** fixed
- **Evidence:** features/automations/api.ts:16,30,67
- **Covered by:** none

### UC-004 P2 frontend/use-cases - YouTube: no webhook form
- **Source:** launch-release/findings/raw/existing-reviews.md section 2, row U-062
- **Alias:** U-062
- **Original tag:** ✅ (no severity given, defaulted to P2)
- **Current status:** fixed
- **Evidence:** features/automations/AutomationsTab.tsx:120
- **Covered by:** none

### UC-005 P2 frontend/use-cases - 401 -> token cleared, redirect to sign-in
- **Source:** launch-release/findings/raw/existing-reviews.md section 2, row U-J1.1
- **Alias:** U-J1.1
- **Original tag:** ✅ (no severity given, defaulted to P2)
- **Current status:** unverified
- **Evidence:** services/backendApi.ts (no 401 literal hit; AUTH_ERROR_PATTERN / isAuthErrorMessage :~523, App.tsx onAuthExpired) (message-pattern based, not status based)
- **Covered by:** none

### UC-006 P2 frontend/use-cases - Rows from D1 if Sheets fails, no UI error
- **Source:** launch-release/findings/raw/existing-reviews.md section 2, row U-J1.2
- **Alias:** U-J1.2
- **Original tag:** ✅ (no severity given, defaulted to P2)
- **Current status:** unverified
- **Evidence:** not traced into worker
- **Covered by:** none

### UC-007 P2 frontend/use-cases - Fresh account -> onboarding wizard
- **Source:** launch-release/findings/raw/existing-reviews.md section 2, row U-J1.3
- **Alias:** U-J1.3
- **Original tag:** ✅ (no severity given, defaulted to P2)
- **Current status:** unverified
- **Evidence:** features/onboarding
- **Covered by:** none

### UC-008 P2 frontend/use-cases - AddTopic "7 fields", redirect to /dashboard
- **Source:** launch-release/findings/raw/existing-reviews.md section 2, row U-J1.4
- **Alias:** U-J1.4
- **Original tag:** ✅ (no severity given, defaulted to P2)
- **Current status:** unverified
- **Evidence:** AddTopicPage.tsx:296 navigate (route /dashboard not confirmed)
- **Covered by:** none

### UC-009 P2 frontend/use-cases - analyzeTopicInsights
- **Source:** launch-release/findings/raw/existing-reviews.md section 2, row U-J1.5
- **Alias:** U-J1.5
- **Original tag:** ✅ (no severity given, defaulted to P2)
- **Current status:** fixed
- **Evidence:** worker index.ts:1878; backendApi.ts:1077
- **Covered by:** none

### UC-010 P2 frontend/use-cases - Generate -> GenWorkerDraftField dialog, SSE stream
- **Source:** launch-release/findings/raw/existing-reviews.md section 2, row U-J1.6
- **Alias:** U-J1.6
- **Original tag:** ✅ (no severity given, defaulted to P2)
- **Current status:** partial
- **Evidence:** DashboardQueue.tsx:161,212-220 (dialog exists; "Save & Continue saveDraftVariants" not traced)
- **Covered by:** LR-163

### UC-011 P2 frontend/use-cases - Editor "3-panel layout" w/ tabs Refine/Media/Topic-Rules/Email
- **Source:** launch-release/findings/raw/existing-reviews.md section 2, row U-J1.7
- **Alias:** U-J1.7
- **Original tag:** ✅ (no severity given, defaulted to P2)
- **Current status:** partial
- **Evidence:** EditorScreen.tsx:227-250 (2 panels); EditorSidebar.tsx:91-98 tabs = Writing Styles/Refine/News/Media/Topic Rules(+Email) (doc stale)
- **Covered by:** LR-163

### UC-012 P2 frontend/use-cases - generateQuickChange
- **Source:** launch-release/findings/raw/existing-reviews.md section 2, row U-J1.8
- **Alias:** U-J1.8
- **Original tag:** ✅ (no severity given, defaulted to P2)
- **Current status:** fixed
- **Evidence:** worker index.ts:1572; backendApi.ts:649
- **Covered by:** none

### UC-013 P2 frontend/use-cases - Footer button "Publish Now"
- **Source:** launch-release/findings/raw/existing-reviews.md section 2, row U-J1.9
- **Alias:** U-J1.9
- **Original tag:** ✅ (no severity given, defaulted to P2)
- **Current status:** partial
- **Evidence:** EditorScreen.tsx:~393 label is Publish to <channel>
- **Covered by:** LR-163

### UC-014 P2 frontend/use-cases - Success alert w/ "View on LinkedIn" link
- **Source:** launch-release/findings/raw/existing-reviews.md section 2, row U-J1.10
- **Alias:** U-J1.10
- **Original tag:** ✅ (no severity given, defaulted to P2)
- **Current status:** unverified
- **Evidence:** useDashboardQueue.ts:587 shows generic 'Success' alert; no permalink/“View on” anywhere in frontend or worker (likely false claim)
- **Covered by:** LR-088

### UC-015 P2 frontend/use-cases - Instagram/Gmail/Telegram/WhatsApp channel flows
- **Source:** launch-release/findings/raw/existing-reviews.md section 2, row U-J2-5
- **Alias:** U-J2-5
- **Original tag:** ✅ (no severity given, defaulted to P2)
- **Current status:** unverified
- **Evidence:** not traced end-to-end; Gmail email fields in EditorSidebar (Email tab)
- **Covered by:** none

### UC-016 P2 frontend/channels - All channels configurable from /connections
- **Source:** launch-release/findings/raw/existing-reviews.md section 2, row U-J6
- **Alias:** U-J6
- **Original tag:** ✅ (no severity given, defaulted to P2)
- **Current status:** partial
- **Evidence:** ConnectionsPage.tsx; Telegram/WhatsApp *recipient* config still in Settings drawer (DashboardSettingsDrawer.tsx:1788,1939)
- **Covered by:** LR-163

### UC-017 P2 frontend/use-cases - Scheduled publishing + cancel (Durable Object)
- **Source:** launch-release/findings/raw/existing-reviews.md section 2, row U-J7
- **Alias:** U-J7
- **Original tag:** ✅ (no severity given, defaulted to P2)
- **Current status:** unverified
- **Evidence:** scheduled-publish/ScheduledPublishBanner.tsx:42 cancel UI; worker/src/scheduled-publish present (alarms not traced)
- **Covered by:** none

### UC-018 P2 frontend/use-cases - Bulk campaign "upload CSV -> append Sheet rows"
- **Source:** launch-release/findings/raw/existing-reviews.md section 2, row U-J8
- **Alias:** U-J8
- **Original tag:** ✅ (no severity given, defaulted to P2)
- **Current status:** partial
- **Evidence:** CampaignPage.tsx:597 accepts .json/.jsonc/.csv (doc oversimplified)
- **Covered by:** LR-163

### UC-019 P2 frontend/use-cases - Automations rules admin-only
- **Source:** launch-release/findings/raw/existing-reviews.md section 2, row U-J10
- **Alias:** U-J10
- **Original tag:** ✅ (no severity given, defaulted to P2)
- **Current status:** unverified
- **Evidence:** none given
- **Covered by:** none

### UC-020 P2 frontend/use-cases - Trending: "fallback to mock data"
- **Source:** launch-release/findings/raw/existing-reviews.md section 2, row U-J11
- **Alias:** U-J11
- **Original tag:** ✅ (no severity given, defaulted to P2)
- **Current status:** partial
- **Evidence:** features/trending/hooks/useTrending.ts:280-292 mock-loading timer when !useRealApis (mock fallback is real code - confirm it cannot reach prod users)
- **Covered by:** LR-094

### UC-021 P2 frontend/use-cases - 6 enrichment actions in worker
- **Source:** launch-release/findings/raw/existing-reviews.md section 2, row U-J12
- **Alias:** U-J12
- **Original tag:** ✅ (no severity given, defaulted to P2)
- **Current status:** fixed
- **Evidence:** worker index.ts:1919,2024,2070,2118,2159,2201 (all present, all have backendApi methods (:1086,1726-1745))
- **Covered by:** none

### UC-022 P2 frontend/use-cases - Debate/cluster "in editor"
- **Source:** launch-release/findings/raw/existing-reviews.md section 2, row U-J12b
- **Alias:** U-J12b
- **Original tag:** ✅ (no severity given, defaulted to P2)
- **Current status:** partial
- **Evidence:** consumers are feed/DraftContextView.tsx:111,143,159, ArticleDetailView.tsx:189 (lives in Feed, not editor sidebar)
- **Covered by:** LR-163

### UC-023 P2 frontend/use-cases - E2E matrix items all unchecked; "100% wired" claim
- **Source:** launch-release/findings/raw/existing-reviews.md section 2, row U-E2E
- **Alias:** U-E2E
- **Original tag:** - (no severity given, defaulted to P2)
- **Current status:** open
- **Evidence:** tests/e2e/*.spec.ts exist (editor, scheduling, connections, ...) (doc not updated; journeys not run by this review)
- **Covered by:** LR-163

### FR-001 P2 docs/feed-report - Report is a descriptive snapshot (no open items); stale numbers (FeedPage 639 lines, BATCH 10, 5 platform panels, absolute paths under /Users/praty...
- **Source:** launch-release/findings/raw/existing-reviews.md section 3, row F-1
- **Alias:** F-1
- **Original tag:** - (no severity given, defaulted to P2)
- **Current status:** n-a
- **Evidence:** FeedPage.tsx now 1490 lines; FeedLeftPanel BATCH_SIZE=20 (do not use as source of truth)
- **Covered by:** none

### FR-002 P2 docs/feed-report - Report: right-click delete only; sidebar hidden <lg; hover-only clip
- **Source:** launch-release/findings/raw/existing-reviews.md section 3, row F-2
- **Alias:** F-2
- **Original tag:** info (no severity given, defaulted to P2)
- **Current status:** open
- **Evidence:** ClipsDock.tsx:206; FeedPage.tsx:1340; FeedArticleCard.tsx (same as C02/C03)
- **Covered by:** LR-163

### FR-003 P2 docs/feed-report - MCP-PROGRESS: 24/24 items [x] (python setup files); nothing pending
- **Source:** launch-release/findings/raw/existing-reviews.md section 3, row M-1
- **Alias:** M-1
- **Original tag:** - (no severity given, defaulted to P2)
- **Current status:** n-a
- **Evidence:** launch-release/ledgers-legacy/MCP-PROGRESS.md (nothing to reconcile; not product-user-facing)
- **Covered by:** none

### SP-001 P2 frontend/navigation - AppSidebar active-state / automations nav fix
- **Source:** launch-release/findings/raw/existing-reviews.md section 4, row P1-T1
- **Alias:** P1-T1
- **Original tag:** [ ] (no severity given, defaulted to P2)
- **Current status:** fixed
- **Evidence:** AppSidebar.tsx:116-148 (PAGE_TO_PATH incl. automations; useEnd only topics) (checkboxes never ticked; code landed)
- **Covered by:** none

### SP-002 P2 frontend/trending - TrendingSidebar refresh button + refetch, remove AddTopic debounce
- **Source:** launch-release/findings/raw/existing-reviews.md section 4, row P1-T2
- **Alias:** P1-T2
- **Original tag:** [ ] (no severity given, defaulted to P2)
- **Current status:** fixed
- **Evidence:** add-topic/TrendingSidebar.tsx:8-31; TopicRightPanel.tsx:87,96; useTrending.ts:295-300
- **Covered by:** none

### SP-003 P2 frontend/settings - ContentReview provider revert guard
- **Source:** launch-release/findings/raw/existing-reviews.md section 4, row P1-T3
- **Alias:** P1-T3
- **Original tag:** [ ] (no severity given, defaulted to P2)
- **Current status:** fixed
- **Evidence:** features/content-review/ContentReviewSettings.tsx:58-62 (empty-catalog guard); services/configService.ts:293-308 normalize
- **Covered by:** none

### SP-004 P2 frontend/settings - TopicsRightRail provider/model validation
- **Source:** launch-release/findings/raw/existing-reviews.md section 4, row P1-T4
- **Alias:** P1-T4
- **Original tag:** [ ] (no severity given, defaulted to P2)
- **Current status:** fixed
- **Evidence:** components/dashboard/components/TopicsRightRail.tsx:111-125
- **Covered by:** none

### SP-005 P2 frontend/feed - Feed L/M/Q/R types, 4 worker cases, 4 API methods
- **Source:** launch-release/findings/raw/existing-reviews.md section 4, row P2-T1..3
- **Alias:** P2-T1..3
- **Original tag:** [ ] (no severity given, defaulted to P2)
- **Current status:** fixed
- **Evidence:** worker index.ts:2070,2118,2159,2201; backendApi.ts:1730-1745
- **Covered by:** none

### SP-006 P2 frontend/feed - Tab L connection finder + Debate button
- **Source:** launch-release/findings/raw/existing-reviews.md section 4, row P2-T4
- **Alias:** P2-T4
- **Original tag:** [ ] (no severity given, defaulted to P2)
- **Current status:** fixed
- **Evidence:** ArticleDetailView.tsx:189,571; FeedPage.tsx onDebate
- **Covered by:** none

### SP-007 P2 frontend/feed - DebateModeView + wiring
- **Source:** launch-release/findings/raw/existing-reviews.md section 4, row P2-T5/6
- **Alias:** P2-T5/6
- **Original tag:** [ ] (no severity given, defaulted to P2)
- **Current status:** fixed
- **Evidence:** features/feed/components/DebateModeView.tsx; FeedPage.tsx debateMode
- **Covered by:** none

### SP-008 P2 frontend/feed - DraftContextView Q/R tabs
- **Source:** launch-release/findings/raw/existing-reviews.md section 4, row P2-T7
- **Alias:** P2-T7
- **Original tag:** [ ] (no severity given, defaulted to P2)
- **Current status:** fixed
- **Evidence:** DraftContextView.tsx:143,159
- **Covered by:** none

### SP-009 P2 deploy/build - Final tsc in both packages
- **Source:** launch-release/findings/raw/existing-reviews.md section 4, row P2-T8
- **Alias:** P2-T8
- **Original tag:** [ ] (no severity given, defaulted to P2)
- **Current status:** unverified
- **Evidence:** not run (read-only rule)
- **Covered by:** none

### AC-001 P2 frontend/feed - /feed split layout, group switcher, filters
- **Source:** launch-release/findings/raw/existing-reviews.md section 5, row D3-1
- **Alias:** D3-1
- **Original tag:** spec (no severity given, defaulted to P2)
- **Current status:** fixed
- **Evidence:** FeedPage.tsx; /trending redirects dashboard/index.tsx:899-900
- **Covered by:** none

### AC-002 P2 worker/feed - Interest-group CRUD endpoints
- **Source:** launch-release/findings/raw/existing-reviews.md section 5, row D3-2
- **Alias:** D3-2
- **Original tag:** spec (no severity given, defaulted to P2)
- **Current status:** partial
- **Evidence:** worker index.ts:72,1723-1733 (action-based listInterestGroups etc., db/interestGroups.ts) (not REST /api/interest-groups; design differs, functionally present)
- **Covered by:** none

### AC-003 P2 worker/feed - Clips CRUD (/api/clips) + persistence
- **Source:** launch-release/findings/raw/existing-reviews.md section 5, row D3-3
- **Alias:** D3-3
- **Original tag:** spec (no severity given, defaulted to P2)
- **Current status:** fixed
- **Evidence:** worker index.ts:714-717,804-807 (assign/unassign by action not verified)
- **Covered by:** none

### AC-004 P2 frontend/feed - Hover scissor on text passages in feed cards
- **Source:** launch-release/findings/raw/existing-reviews.md section 5, row D3-4
- **Alias:** D3-4
- **Original tag:** spec (no severity given, defaulted to P2)
- **Current status:** open
- **Evidence:** see C03-7
- **Covered by:** FZ-003

### AC-005 P2 frontend/clips - Dock magnification, expand, drag to draft
- **Source:** launch-release/findings/raw/existing-reviews.md section 5, row D3-5
- **Alias:** D3-5
- **Original tag:** spec (no severity given, defaulted to P2)
- **Current status:** fixed
- **Evidence:** ClipsDock.tsx:158,332-367
- **Covered by:** none

### AC-006 P2 frontend/clips - Draft Context Mode: drag clip into editor as context block
- **Source:** launch-release/findings/raw/existing-reviews.md section 5, row D3-6
- **Alias:** D3-6
- **Original tag:** spec (no severity given, defaulted to P2)
- **Current status:** partial
- **Evidence:** DraftContextView.tsx:259-266 ("Generate Post in Editor"), :571 unassign (drag-into-editor insertion not found)
- **Covered by:** FZ-003

### AC-007 P2 worker/feed - Article intelligence "streamed, cached after first load"
- **Source:** launch-release/findings/raw/existing-reviews.md section 5, row D3-7
- **Alias:** D3-7
- **Original tag:** spec (no severity given, defaulted to P2)
- **Current status:** unverified
- **Evidence:** none given
- **Covered by:** none

### AC-008 P2 worker/generation - Mode 1 author-voice keeps >=80% of words
- **Source:** launch-release/findings/raw/existing-reviews.md section 5, row D2-1
- **Alias:** D2-1
- **Original tag:** AC1 (no severity given, defaulted to P2)
- **Current status:** unverified
- **Evidence:** worker/src/engine/nodes/definitions/draft-generator.ts (no test seen for 80%)
- **Covered by:** none

### AC-009 P2 worker/generation - Industry Trend post type + HOOK->EVIDENCE->... structure
- **Source:** launch-release/findings/raw/existing-reviews.md section 5, row D2-2
- **Alias:** D2-2
- **Original tag:** AC2 (no severity given, defaulted to P2)
- **Current status:** partial
- **Evidence:** worker/src/engine/workflows/definitions/trend-commentary.ts; __tests__/contentPostTypesPlaybook.spec.test.ts
- **Covered by:** none

### AC-010 P2 worker/generation - Per-post dimension override beats workspace
- **Source:** launch-release/findings/raw/existing-reviews.md section 5, row D2-3
- **Alias:** D2-3
- **Original tag:** AC3 (no severity given, defaulted to P2)
- **Current status:** unverified
- **Evidence:** none given
- **Covered by:** none

### AC-011 P2 worker/generation - 4 variants w/ variant_rationale + badges
- **Source:** launch-release/findings/raw/existing-reviews.md section 5, row D2-4
- **Alias:** D2-4
- **Original tag:** AC4 (no severity given, defaulted to P2)
- **Current status:** fixed
- **Evidence:** worker engine/types.ts, draft-generator.ts; frontend VariantCarousel.tsx
- **Covered by:** none

### AC-012 P2 deploy/build - tsc passes both packages
- **Source:** launch-release/findings/raw/existing-reviews.md section 5, row D2-5
- **Alias:** D2-5
- **Original tag:** AC5 (no severity given, defaulted to P2)
- **Current status:** unverified
- **Evidence:** not run
- **Covered by:** none

### AC-013 P2 frontend/editor - Quick change/4-variant preview-only, unsaved marker, explicit Save Variants
- **Source:** launch-release/findings/raw/existing-reviews.md section 5, row DE-1
- **Alias:** DE-1
- **Original tag:** EGW (no severity given, defaulted to P2)
- **Current status:** partial
- **Evidence:** review/context/useReviewFlowActions.ts:~357 openCompare; backendApi.ts saveVariants (UI wording not traced)
- **Covered by:** none

### AC-014 P2 frontend/editor - Compare never replaces without confirmation
- **Source:** launch-release/findings/raw/existing-reviews.md section 5, row DE-2
- **Alias:** DE-2
- **Original tag:** EGW (no severity given, defaulted to P2)
- **Current status:** fixed
- **Evidence:** useReviewFlowActions.ts:~357-372 (compare onConfirm sets editor text)
- **Covered by:** none

### AC-015 P2 frontend/editor - Approval doesn't require Save Variants
- **Source:** launch-release/findings/raw/existing-reviews.md section 5, row DE-3
- **Alias:** DE-3
- **Original tag:** EGW (no severity given, defaulted to P2)
- **Current status:** unverified
- **Evidence:** none given
- **Covered by:** none

### AC-016 P2 frontend/editor - Old refine path removed after parity
- **Source:** launch-release/findings/raw/existing-reviews.md section 5, row DE-4
- **Alias:** DE-4
- **Original tag:** EGW (no severity given, defaulted to P2)
- **Current status:** unverified
- **Evidence:** none given
- **Covered by:** none

### AC-017 P2 frontend/code-health - Modularity (no oversized component)
- **Source:** launch-release/findings/raw/existing-reviews.md section 5, row DE-5
- **Alias:** DE-5
- **Original tag:** EGW (no severity given, defaulted to P2)
- **Current status:** open
- **Evidence:** DashboardSettingsDrawer.tsx 2251 lines; FeedPage.tsx 1490; EditorSidebar large
- **Covered by:** LR-179

### NW-001 P2 frontend/feed - Feed card Bookmark button is a dead control: FeedArticleCard.tsx Bookmark onClick only stopPropagation() (no handler, no prop). Ships an icon that ...
- **Source:** launch-release/findings/raw/existing-reviews.md, row NEW-1
- **Alias:** NEW-1
- **Original tag:** new (not in a source; no severity given, defaulted to P2)
- **Current status:** open
- **Evidence:** none given
- **Covered by:** LR-173

### NW-002 P2 frontend/queue - Onboarding Tour copy in DashboardQueue.tsx:435 promises a channel pill that is not rendered (see C04-2) - misleading first-run text.
- **Source:** launch-release/findings/raw/existing-reviews.md, row NEW-2
- **Alias:** NEW-2
- **Original tag:** new (not in a source; no severity given, defaulted to P2)
- **Current status:** open
- **Evidence:** none given
- **Covered by:** LR-097

### NW-003 P2 frontend/errors - components/ui/ErrorBanner.tsx, EmptyState.tsx, LoadingSkeleton.tsx are unused dead code; cons doc 13 treats them as the fix, but nothing adopts them.
- **Source:** launch-release/findings/raw/existing-reviews.md, row NEW-3
- **Alias:** NEW-3
- **Original tag:** new (not in a source; no severity given, defaulted to P2)
- **Current status:** open
- **Evidence:** none given
- **Covered by:** LR-111

### NW-004 P2 frontend/errors - services/backendApi.ts:485-525 network-failure message tells end users to edit CORS_ALLOWED_ORIGINS, VITE_WORKER_URL and workers.dev firewall rules...
- **Source:** launch-release/findings/raw/existing-reviews.md, row NEW-4
- **Alias:** NEW-4
- **Original tag:** new (not in a source; no severity given, defaulted to P2)
- **Current status:** open
- **Evidence:** none given
- **Covered by:** LR-110

### NW-005 P2 frontend/feedback - No transient toast system in app at all (only modal showAlert); success feedback for Save draft / Approve is absent. Toast exists only locally in S...
- **Source:** launch-release/findings/raw/existing-reviews.md, row NEW-5
- **Alias:** NEW-5
- **Original tag:** new (not in a source; no severity given, defaulted to P2)
- **Current status:** open
- **Evidence:** none given
- **Covered by:** LR-183

### NW-006 P2 frontend/trending - useTrending.ts:280-292 mock-data path still present for !useRealApis; confirm production always has real APIs or users could see mock trending.
- **Source:** launch-release/findings/raw/existing-reviews.md, row NEW-6
- **Alias:** NEW-6
- **Original tag:** new (not in a source; no severity given, defaulted to P2)
- **Current status:** open
- **Evidence:** none given
- **Covered by:** LR-094
