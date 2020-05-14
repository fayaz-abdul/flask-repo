from flask_restplus import Resource
from flask import request
from api import api
from .controllers.task_controller import add_task, get_all_tasks, get_task_by_id, update_task


@api.route('/task', methods=['POST', 'GET'])
class Task(Resource):
    def get(self):
        return get_all_tasks()

    @api.doc(params={'description': 'Description of task'})
    def post(self):
        print("In task -> post")
        return add_task(description=request.json["description"])

@api.route('/task/<id>', methods=['PUT', 'GET'])
@api.doc(params={'id': 'id of task'})
class TaskOps(Resource):
    def get(self, id):
        response = get_task_by_id(id)
        if not response:
            return dict({"message": "Task ID could not be found."}), 404
        return response

    @api.doc(params={'description': 'Description of task'})
    def put(self, id):
        response = update_task(description=request.json["description"], id=id)
        if not response:
            return dict({"message": "Task ID could not be found."}), 404
        return response
