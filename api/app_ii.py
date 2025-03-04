""" 
Flask RESTful API with Mongo Db
"""

# Import libraries
import os
import json
import pymongo
from flask import Flask,  Response

# Define flask object as application
app = Flask(__name__)

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["students"]

# Create index route for landing page
@app.route('/', methods=['GET'])
def index():
    return '<p>Welcome to Flask API</p>'

# Students list route in JSON format
@app.route('/api/students', methods = ['GET'])
def students ():
    student_list = [
        {
            'name':'Asabeneh',
            'country':'Finland',
            'city':'Helsinki',
            'skills':['HTML', 'CSS','JavaScript','Python']
        },
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
    return Response(json.dumps(student_list), mimetype='application/json')

# Deployment entry point
if __name__ == '__main__':
    # for deployment
    # to make it work for both production and development
    port = int(os.environ.get("PORT", 5001))
    app.run(debug=True, host='0.0.0.0', port=port)