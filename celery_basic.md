### Bound tasks
A task being bound means the first argument to the task will always be the task instance (self), just like Python bound methods
```python

logger = get_task_logger(__name__)

@app.task(bind=True)
def add(self, x, y):
    logger.info(self.request.id)
```
