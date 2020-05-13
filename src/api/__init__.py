from flask import Flask
from flask_restplus import Api

app = Flask(__name__)                  #  Create a Flask WSGI application
api = Api(app)                         #  Create a Flask-RESTPlus API


from api import task
