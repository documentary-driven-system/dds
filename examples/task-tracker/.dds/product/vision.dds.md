---
id: product-vision
type: product
status: active
dependencies: []
last_updated: 2026-09-18
description: Why TaskTracker exists, who uses it, and how success is measured.
---

# PRODUCT: TaskTracker Vision

## [0] BUSINESS_VISION_AND_VALUE
TaskTracker gives a small team one place to record, assign, and close work items, so that a Team Lead sees late work without asking and a Team Member sees their own work without searching.

## [1] TARGET_PERSONAS
- **Team Lead:** Runs a team of 3 to 15 people; needs the list of late tasks every morning without building the list by hand.
- **Team Member:** Owns tasks; needs one list of open work and a one-step way to close an item.

## [2] KEY_PERFORMANCE_INDICATORS (KPIs)
- Tasks closed on or before their due date: 85% of closed tasks per month.
- Time from task creation to first assignment: under 1 business day for 90% of tasks.

## [3] USER_STORIES_AND_ACCEPTANCE_CRITERIA
<user_stories>
- **Story:** As a Team Lead, I want to see every late task of my team on one screen, so that I can act before the customer notices.
- **Acceptance:** The system MUST list every task whose due date has passed and whose status is not `done`, grouped by owner.
</user_stories>

## Changelog
- [2026-09-18]: Promoted from draft after review by the product owner.
