---
id: product-notifications
type: product
status: deprecated
dependencies: []
last_updated: 2026-09-10
deprecated_date: 2026-09-10
original_path: .dds/product/epics/notifications/notifications.dds.md
description: Daily email digest of late tasks; abandoned because no email provider had a signed DPA (C3).
---

> ⚠️ DEPRECATED: This business requirement/epic was abandoned on 2026-09-10. Reason: constraint C3 of `product-constraints` (no third-party email provider under a signed data processing agreement); the in-app late list of `product-vision` replaces the digest.

# EPIC: Notifications

## [0] BUSINESS_VISION_AND_VALUE
The Notifications epic sent a Team Lead a daily email digest of late tasks, so that late work surfaced without opening the app.

## [1] TARGET_PERSONAS
- **Team Lead:** Wanted the late list in the inbox at 08:00.

## [2] KEY_PERFORMANCE_INDICATORS (KPIs)
- Digest opened by 60% of Team Leads on workdays.

## [3] USER_STORIES_AND_ACCEPTANCE_CRITERIA
<user_stories>
- **Story:** As a Team Lead, I want a daily email listing my team's late tasks, so that I see them before stand-up.
- **Acceptance:** The system MUST send one email per Team Lead per workday at 08:00 local time.
</user_stories>

## Changelog
- [2026-09-10]: Abandoned; every candidate email provider processes personal data (email, task titles) without a signed DPA, which constraint C3 forbids.
- [2026-08-25]: Document created as `status: draft`.
