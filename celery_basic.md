### Bound tasks
A task being bound means the first argument to the task will always be the task instance (self), just like Python bound methods
```python

logger = get_task_logger(__name__)

@app.task(bind=True)
def add(self, x, y):
    logger.info(self.request.id)
```
### Names
very task must have a unique name.

If no explicit name is provided the task decorator will generate one for you, and this name will be based on 1) the module the task is defined in, and 2) the name of the task function.

Example setting explicit name:
```python
@app.task(name='sum-of-two-numbers')
def add(x, y):
    return x + y
```
> add.name
> 'sum-of-two-numbers'

A best practice is to use the module name as a name-space, this way names won’t collide if there’s already a task with that name defined in another module.
```python
@app.task(name='tasks.add')
def add(x, y):
    return x + y
```
You can tell the name of the task by investigating its .name attribute:
