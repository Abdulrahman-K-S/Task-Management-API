from flask import request, jsonify, g
from services import TaskService
from flask_restx import abort

class TaskController:
    """TaskController

    This class handles the HTTP requests for tasks, including creating, retrieving,
    updating, and deleting tasks.
    """

    @staticmethod
    def create_task():
        """create_task

        Handles the HTTP POST request to create a new task.

        Return:
            (Response): A Flask response object containing the created task data and a success message.
        """
        data = request.json

        if not data or 'title' not in data:
            abort(400, 'Task title is required')

        task = TaskService.create_task(data)
        return {"message": "Task created successfully", "task": task}, 201

    @staticmethod
    def get_task(task_id):
        """get_task

        Handles the HTTP GET request to retrieve a task by its ID.

        Arguments:
            task_id (str): The ID of the task to retrieve.

        Return:
            (Response): A Flask response object containing the task data if found, else an error message.
        """
        task = TaskService.get_task(task_id)
        if not task:
            abort(404, 'Task not found')
        return {"task": task}, 200

    @staticmethod
    def update_task(task_id):
        """update_task

        Handles the HTTP PUT request to update an existing task.

        Arguments:
            task_id (str): The ID of the task to update.

        Return:
            (Response): A Flask response object containing the updated task data and a success message.
        """
        data = request.json

        if not data:
            abort(400, 'No data provided')
        if TaskService.get_task(task_id) is None:
            abort(404, 'Task not found')
        
        task = TaskService.update_task(task_id, data)
        return {"message": "Task updated successfully", "task": task}, 200

    @staticmethod
    def delete_task(task_id):
        """delete_task

        Handles the HTTP DELETE request to delete a task by its ID.

        Arguments:
            task_id (str): The ID of the task to delete.

        Return:
            (Response): A Flask response object containing a success message if the task was deleted, else an error message.
        """
        if TaskService.get_task(task_id) is None:
            abort(404, "Task not found")
        TaskService.delete_task(task_id)
        return {"message": "Task deleted successfully"}, 200
