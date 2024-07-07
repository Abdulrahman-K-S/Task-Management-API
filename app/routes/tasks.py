from flask import Blueprint, request, jsonify, current_app
from controllers import TaskController

tasks_bp = Blueprint('tasks', __name__)

@tasks_bp.route('/tasks', methods=['POST'])
def create_task():
    """Create a new task"""
    return TaskController.create_task(request.json, current_app.redis_client)

@tasks_bp.route('/tasks/<task_id>', methods=['GET'])
def get_task(task_id):
    """Retrieve a task by ID"""
    return TaskController.get_task(task_id, current_app.redis_client)

@tasks_bp.route('/tasks/<task_id>', methods=['PUT'])
def update_task(task_id):
    """Update a task by ID"""
    return TaskController.update_task(task_id, request.json, current_app.redis_client)

@tasks_bp.route('/tasks/<task_id>', methods=['DELETE'])
def delete_task(task_id):
    """Delete a task by ID"""
    return TaskController.delete_task(task_id, current_app.redis_client)
