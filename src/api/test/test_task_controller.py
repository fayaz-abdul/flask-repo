from api import app
import json
import pytest


def test_add_task(capsys):
    app.testing = True
    with app.test_client() as c:
        data = {'description': 'first task' }
        r = c.post(
            '/task',
            data = json.dumps(data),
            content_type = 'application/json'
        )

        assert r.status_code == 200
        assert r.json["description"] == data["description"]
        assert len(r.json["id"]) != 0
        assert len(r.json["created_time"]) != 0

        r = c.post(
            '/task',
            data=json.dumps({'description': 'second task' }),
            content_type='application/json'
        )

def test_get_all_tasks(capsys):
    app.testing = True
    with app.test_client() as c:
        r = c.get('/task')
        print(r.json)
        assert r.status_code == 200
        assert len(r.json) == 2


def test_get_task_by_id(capsys):
    app.testing = True
    with app.test_client() as c:
        r = c.get('/task')
        print(r.json)
        assert r.status_code == 200
        assert len(r.json) == 2

        for task in r.json:
            if task.get("description", None) and task["description"] in "first task":
                id = task["id"]

        # Ensure there is atleast one task with description "first task"
        assert id

        # Now use this id to fetch that task and check if description matches.
        r = c.get('/task/{}'.format(id))
        print(r.json)
        assert r.status_code == 200
        assert r.json["description"] == "first task"
        assert len(r.json["created_time"]) != 0

        # Test if non existent id gives 404 error.
        r = c.get('/task/{}'.format("dummy_id"))
        assert r.status_code == 404


def test_update_task(capsys):
    app.testing = True
    with app.test_client() as c:
        r = c.get('/task')
        print(r.json)
        assert r.status_code == 200
        assert len(r.json) == 2

        for task in r.json:
            if task.get("description", None) and task["description"] in "second task":
                id = task["id"]

        # Ensure there is atleast one task with description "second task"
        assert id

        # Now use this id to update the task. Then assert if the proper response is received.
        data = {'description': 'updated second task' }
        r = c.put(
            '/task/{}'.format(id),
            data = json.dumps(data),
            content_type = 'application/json'
        )

        assert r.status_code == 200
        assert r.json["description"] == data["description"]
        assert r.json["id"] == id
        assert len(r.json["created_time"]) != 0

        # Fetch the task using id and check if the task is actually updated.
        r = c.get('/task/{}'.format(id))
        print(r.json)
        assert r.status_code == 200
        assert r.json["description"] == data["description"]
        assert r.json["id"] == id
        assert len(r.json["created_time"]) != 0

        # Test if non existent id update gives 404 error.
        r = c.put(
            '/task/{}'.format("dummy_id"),
            data=json.dumps(data),
            content_type='application/json'
        )
        assert r.status_code == 404


if __name__ == "__main__":
    pytest.main()