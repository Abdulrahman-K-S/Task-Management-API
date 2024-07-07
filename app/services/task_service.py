import uuid
from flask import g
from models import Task

class TaskService:
    """TaskService

    This class contains the business logic handlers for tasks which
    includes creating the task, updating the task, and deleting the task
    """
    @staticmethod
    def create_task(data):
        """create_task

        This method creates a new task and stores it into the redis client.

        Arguments:
            data (dict): A dictionary containing the task data.

        Return:
            (dict): A dictionary containing the task created and a success message.
        """
        task_id = str(uuid.uuid4())
        task = Task(
            task_id=task_id,
            title=data['title'],
            description=data.get('description', '')
        )
        g.redis_client.set(task_id, task.to_dict())
        return {
            'message': 'Task created succesfully',
            'task': task.to_dict()
        }

    @staticmethod
    def get_task(task_id):
        """get_task

        Retrieves a task from Redis by its ID.

        Arguments:
            task_id (str): The ID of the task to retrieve.

        Return:
            (dict): A dictionary containing the task data if found, else an error message.
        """
        task_data = g.redis_client.get(task_id)
        if task_data:
            task = Task.from_dict(task_data)
            return task.to_dict()
        else:
            return {'error': 'Task not found'}

    @staticmethod
    def update_task(task_id, data):
        """update_task

        Updates an existing task in Redis.

        Arguments:
            task_id (str): The ID of the task to update.
            data (dict): A dictionary containing the updated task data.

        Return:
            (dict): A dictionary containing the updated task data and a success message.
        """
        task_data = g.redis_client.get(task_id)
        if task_data:
            task = Task.from_dict(task_data)
            task.title = data.get('title', task.title)
            task.description = data.get('description', task.description)
            task.status = data.get('status', task.status)
            g.redis_client.set(task_id, task.to_dict())
            return {
                'message': 'Task updated successfully',
                'task': task.to_dict()
            }
        else:
            return {'error': 'Task not found'}

    @staticmethod
    def delete_task(task_id):
        """delete_task

        Deletes a task from Redis by its ID.

        Arguments:
            task_id (str): The ID of the task to delete.

        Return:
            (dict): A dictionary containing a success message if the task was deleted,
            else an error message.
        """
        task_data = g.redis_client.get(task_id)
        if task_data:
            g.redis_client.delete(task_id)
            return {'message': 'Task deleted successfully'}
        else:
            return {'error': 'Task not found'}
