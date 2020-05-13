from api.models.task_model import Task, TaskSchema
from api import api
from uuid import uuid1
import datetime as dt

tasks = {}

def add_task(description):
    global tasks

    task = Task(
        id= uuid1(),
        description=description,
        created_time= dt.datetime.now()
    )

    schema = TaskSchema()
    task_dict = schema.dump(task)

    #@Todo conisder writing getter function
    tasks[task_dict["id"]] = task
    return schema.dump(task)


def get_all_tasks():
    global tasks
    schema = TaskSchema()
    return [schema.dump(task_obj) for id, task_obj in tasks.items()]

def get_task_by_id(id):
    global tasks
    schema = TaskSchema()
    try:
        return schema.dump(tasks[id])
    except:
        return {}

def update_task(description, id):
    global tasks
    schema = TaskSchema()
    try:
        old_data = schema.dump(tasks[id])

        # make this setter function probably.
        tasks[id] = schema.load({
            "id" : old_data["id"],
            "description" : description,
            "created_time" : old_data["created_time"]
        })
        return schema.dump(tasks[id])
    except:
        return {}