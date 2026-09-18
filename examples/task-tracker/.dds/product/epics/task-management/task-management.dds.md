---
id: product-task-management
type: product
status: active
dependencies: []
last_updated: 2026-09-18
description: The life of a task from creation to closure; two user stories with acceptance criteria.
---

# EPIC: Task Management

## [0] BUSINESS_VISION_AND_VALUE
The Task Management epic covers the life of a task from creation to closure, so that a team's work is visible and a Team Member closes an item in one step.

## [1] TARGET_PERSONAS
- **Team Lead:** Creates and assigns tasks; reads the late list.
- **Team Member:** Completes assigned tasks; reopens a task closed by mistake.

## [2] KEY_PERFORMANCE_INDICATORS (KPIs)
- Task creation form completed in under 30 seconds for 90% of tasks (measured from open to save).
- Fewer than 2% of completed tasks reopened within 24 hours.

## [3] USER_STORIES_AND_ACCEPTANCE_CRITERIA
<user_stories>
- **Story:** As a Team Lead, I want to create a task with a title, an owner, and a due date, so that the work is assigned the moment it is known.
- **Acceptance:** The system MUST reject a task without a title or a due date and MUST record who created the task and when.
- **Story:** As a Team Member, I want to complete a task in one action, so that my list reflects reality.
- **Acceptance:** The system MUST record the completion time and the person who completed the task, and MUST allow the owner or a Team Lead to reopen the task within 24 hours.
</user_stories>

## Changelog
- [2026-09-18]: Promoted from draft after review.
