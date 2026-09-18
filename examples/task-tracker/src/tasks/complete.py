"""TaskService.complete / reopen — governed by modules-tasks-complete."""
from datetime import timedelta

REOPEN_WINDOW = timedelta(hours=24)


def complete(repo, clock, task_id: str, subject: str, is_team_lead: bool):
    task = repo.get(task_id)
    if task.owner_id != subject and not is_team_lead:
        raise Forbidden()                                       # HTTP 403
    return repo.mark_done(task_id, completed_by=subject)        # one UPDATE sets status, completed_at, completed_by


def reopen(repo, clock, task_id: str):
    task = repo.get(task_id)
    if task.completed_at is None or clock.now() - task.completed_at > REOPEN_WINDOW:
        raise Conflict()                                        # HTTP 409
    return repo.reopen(task_id)


class Forbidden(Exception):
    pass


class Conflict(Exception):
    pass
