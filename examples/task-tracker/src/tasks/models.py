"""Task model and validation. Governed by modules-tasks-create and modules-tasks-complete."""
from dataclasses import dataclass
from datetime import date, datetime
from typing import Optional

TITLE_MAX = 200  # tasks.title VARCHAR(200), architecture-core-database


@dataclass
class Task:
    id: str
    title: str
    owner_id: str
    due_date: date
    status: str = "open"
    created_by: str = ""
    created_at: Optional[datetime] = None
    completed_at: Optional[datetime] = None
    completed_by: Optional[str] = None


def validate_new_task(payload: dict) -> list:
    """Return every failing field (modules-tasks-create, constraint 1)."""
    errors = []
    title = (payload.get("title") or "").strip()
    if not title or len(title) > TITLE_MAX:
        errors.append("title")
    if not payload.get("due_date"):
        errors.append("due_date")
    return errors
