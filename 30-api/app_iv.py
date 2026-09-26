""" 
API with resources

Write a simple Flask API with resources
"""
from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {'message': 'Hello World!'}

class Todo(Resource):
    def get(self, todo_id):
        return {'task': f'Todo {todo_id}'}
    def put(self, todo_id):
        return {'task': f'Updated Todo {todo_id}'}

api.add_resource(HelloWorld, '/')
api.add_resource(Todo, '/todos/<int:todo_id>')

if __name__ == '__main__':
    app.run(debug=True)