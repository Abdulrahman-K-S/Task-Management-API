from flask import request, jsonify, g
from services import TaskService

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
        data = request.get_json()
        response = TaskService.create_task(data)
        print("In taskcontroller create_task")
        return jsonify(response), 201

    @staticmethod
    def get_task(task_id):
        """get_task

        Handles the HTTP GET request to retrieve a task by its ID.

        Arguments:
            task_id (str): The ID of the task to retrieve.

        Return:
            (Response): A Flask response object containing the task data if found, else an error message.
        """
        response = TaskService.get_task(task_id)
        return jsonify(response), 200 if 'error' not in response else 404

    @staticmethod
    def update_task(task_id):
        """update_task

        Handles the HTTP PUT request to update an existing task.

        Arguments:
            task_id (str): The ID of the task to update.

        Return:
            (Response): A Flask response object containing the updated task data and a success message.
        """
        data = request.get_json()
        response = TaskService.update_task(task_id, data)
        return jsonify(response), 200 if 'error' not in response else 404

    @staticmethod
    def delete_task(task_id):
        """delete_task

        Handles the HTTP DELETE request to delete a task by its ID.

        Arguments:
            task_id (str): The ID of the task to delete.

        Return:
            (Response): A Flask response object containing a success message if the task was deleted, else an error message.
        """
        response = TaskService.delete_task(task_id)
        return jsonify(response), 200 if 'error' not in response else 404
