""" 
Flask Integrated API
"""

# libraries
import os
import json
import requests
from flask import Flask,  Response

# Flask object as application
app = Flask(__name__)

# External API url
url = 'https://jsonplaceholder.typicode.com/todos'

# Users database
users = [
        {
            'name':'David',
            'country':'UK',
            'city':'London',
            'skills':['Python','MongoDB']
        },
        {
            'name':'John',
            'country':'Sweden',
            'city':'Stockholm',
            'skills':['Java','C#']
        }
    ]

# Index route for landing page
@app.route('/', methods=['GET'])
def index():
    return '<p>Welcome to Unified API</p>'

# List of users
@app.route('/users', methods = ['GET'])
def students ():
    return Response(json.dumps(users), mimetype='application/json')

# Get all todos
@app.route('/todos', methods=['GET'])
def get_todos():
    response = requests.get(url)
    return response.json()

# Get single item
@app.route('/todo', methods=['GET'])
def get_todo():
    response = requests.get(url + '/1')
    return response.json()

# Generate new data
@app.route('/todo', methods=['POST'])
def add_todo():
    todo = {"userId": 1, "title": "Buy milk", "completed": False}
    response = requests.post(url,json=todo)
    return response.json()

# Update existing data
@app.route('/todo', methods=['PUT'])
def update_todo():
    todo = {"userId": 1, "title": "Buy milk", "completed": False}
    response = requests.put(url + '/1', json=todo)
    return response.json()

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5001))
    app.run(debug=True, host='0.0.0.0', port=port)