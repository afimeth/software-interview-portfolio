"""Synthetic task-board domain. No external services or model keys."""
def normalize(title):
    if not isinstance(title, str) or not title.strip() or len(title.strip()) > 120:
        raise ValueError('title must contain 1..120 characters')
    return title.strip()

def create(tasks, title):
    task = {'id': len(tasks) + 1, 'title': normalize(title), 'done': False}
    tasks.append(task)
    return task

def complete(tasks, task_id):
    for task in tasks:
        if task['id'] == task_id:
            task['done'] = True
            return task
    raise KeyError(task_id)
