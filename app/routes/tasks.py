from flask import request, jsonify
from flask_restx import Namespace, Resource, fields
from controllers import TaskController

tasks_bp = Namespace('tasks', description='Task operations')

task_model = tasks_bp.model('Task', {
    'title': fields.String(required=True, description='The task title'),
    'description': fields.String(required=True, description='The task description'),
    'status': fields.String(description='The task status'),
    'assigned_to': fields.String(description='The user whom is assigned to the task'),
})

@tasks_bp.route('/')
class TaskList(Resource):
    @tasks_bp.expect(task_model)
    @tasks_bp.response(201, 'Task created successfully')
    def post(self):
        """Create a new task"""
        return TaskController.create_task()
    
    @tasks_bp.response(200, 'Tasks retrieved successfully')
    def get(self):
        """Get all tasks"""
        return TaskController.get_all_tasks()

@tasks_bp.route('/<task_id>')
@tasks_bp.param('task_id', 'The task identifier')
class Task(Resource):
    @tasks_bp.response(200, 'Task found')
    @tasks_bp.response(404, 'Task not found')
    def get(self, task_id):
        """Fetch a task given its identifier"""
        return TaskController.get_task(task_id)

    @tasks_bp.expect(task_model)
    @tasks_bp.response(200, 'Task updated successfully')
    @tasks_bp.response(404, 'Task not found')
    def put(self, task_id):
        """Update a task given its identifier"""
        return TaskController.update_task(task_id)

    @tasks_bp.response(200, 'Task deleted successfully')
    @tasks_bp.response(404, 'Task not found')
    def delete(self, task_id):
        """Delete a task given its identifier"""
        return TaskController.delete_task(task_id)

@tasks_bp.route('/<task_id>/<user_id>')
@tasks_bp.param('task_id', 'The task identifier')
@tasks_bp.param('user_id', 'The user identifier')
class TaskUser(Resource):
    @tasks_bp.response(200, 'Task assigned successfylly')
    @tasks_bp.response(404, 'Task not found')
    def put(self, task_id, user_id):
        """Update the task assigning it to user"""
        return TaskController.assign_task_to_user(task_id, user_id)
