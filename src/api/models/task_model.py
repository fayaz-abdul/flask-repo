from marshmallow import Schema, fields, post_load


class Task:
    def __init__(self, id, description, created_time):
        self.id = id
        self.description = description
        self.created_time = created_time


class TaskSchema(Schema):
    id = fields.UUID()
    description = fields.Str()
    created_time = fields.DateTime()

    @post_load
    def create_task(self, data, **kwargs):
        return Task(**data)

