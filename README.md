# Flask test

## Overview
This will happen in 2 phases, each of which is materialised by a pull request:
1. Agree on the model, with a swagger
2. Build the REST API

## Contents

1. [File Layout](#layout)
2. [How to run the app](#how-to-app)
3. [Testing the app](#how-to-test)
4. [Postman](#postman)

## File Layout <a id="layout"></a>
```
├── README.md
├── postman
│   └── flask-test.json
├── src
│   ├── api
│   │   ├── __init__.py
│   │   ├── controllers
│   │   │   ├── __init__.py
│   │   │   └── task_controller.py
│   │   ├── models
│   │   │   ├── __init__.py
│   │   │   └── task_model.py
│   │   ├── task.py
│   │   └── test
│   │       ├── __init__.py
│   │       └── test_task_controller.py
│   ├── api.py
│   └── requirements.txt
└── swagger
    ├── README.md
    └── model.yaml      
```
## How to run the app <a id="how-to"></a>
Clone the repo and run as below


```
python3 -m venv flask-test-env
source flask-test-env/bin/activate
cd src
python3 -m pip install install -r requirements.txt
python3 api.py
 * Serving Flask app "api" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Running on http://127.0.0.1:8080/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 189-198-217


```

## Testing the app <a id="how-to-test"></a>
Clone the repo and run as below

```
cd src/api/test
pytest -s -W ignore::DeprecationWarning
=============================================== test session starts ================================================
platform darwin -- Python 3.7.4, pytest-5.4.2, py-1.8.1, pluggy-0.13.1
rootdir: /Users/fayazabdul/work/tafzs/flask/git/flask-repo/src/api/test
collected 4 items

test_task_controller.py In task -> post
In task -> post
.[{'id': '73290c42-954d-11ea-8775-acde48001122', 'description': 'first task', 'created_time': '2020-05-13T20:10:46.531239'}, {'id': '732995c2-954d-11ea-8775-acde48001122', 'description': 'second task', 'created_time': '2020-05-13T20:10:46.534715'}]
.[{'id': '73290c42-954d-11ea-8775-acde48001122', 'description': 'first task', 'created_time': '2020-05-13T20:10:46.531239'}, {'id': '732995c2-954d-11ea-8775-acde48001122', 'description': 'second task', 'created_time': '2020-05-13T20:10:46.534715'}]
{'id': '73290c42-954d-11ea-8775-acde48001122', 'description': 'first task', 'created_time': '2020-05-13T20:10:46.531239'}
.[{'id': '73290c42-954d-11ea-8775-acde48001122', 'description': 'first task', 'created_time': '2020-05-13T20:10:46.531239'}, {'id': '732995c2-954d-11ea-8775-acde48001122', 'description': 'second task', 'created_time': '2020-05-13T20:10:46.534715'}]
{'id': '732995c2-954d-11ea-8775-acde48001122', 'description': 'updated second task', 'created_time': '2020-05-13T20:10:46.534715'}
.

================================================ 4 passed in 0.27s =================================================


```

## Postman <a id="postman"></a>

Import the postman/flask-test.json file into postman and test after running the app.