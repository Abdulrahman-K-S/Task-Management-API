from flask import Blueprint
from controllers import TaskController

tasks_bp = Blueprint('tasks', __name__)

tasks_bp.route('/tasks', methods=['POST'])(TaskController.create_task)
tasks_bp.route('/tasks/<task_id>', methods=['GET'])(TaskController.get_task)
tasks_bp.route('/tasks/<task_id>', methods=['PUT'])(TaskController.update_task)
tasks_bp.route('/tasks/<task_id>', methods=['DELETE'])(TaskController.delete_task)
