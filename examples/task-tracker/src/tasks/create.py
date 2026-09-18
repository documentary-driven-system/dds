"""TaskService.create — governed by modules-tasks-create."""
import uuid
from .models import Task, validate_new_task


class TaskService:
    def __init__(self, repo, users):
        self.repo = repo
        self.users = users

    def create(self, payload: dict, subject: str, idempotency_key: str) -> Task:
        errors = validate_new_task(payload)
        if errors:
            raise ValidationError(errors)                       # HTTP 422, every failing field
        existing = self.repo.by_idempotency_key(idempotency_key)
        if existing:
            return existing                                     # constraint 3: one row per key
        if not self.users.exists(payload["owner_id"]):
            raise NotFound("owner")                             # HTTP 404
        task = Task(id=str(uuid.uuid4()), title=payload["title"].strip(),
                    owner_id=payload["owner_id"], due_date=payload["due_date"], created_by=subject)
        return self.repo.insert(task, idempotency_key)          # created_at from the database clock


class ValidationError(Exception):
    pass


class NotFound(Exception):
    pass
