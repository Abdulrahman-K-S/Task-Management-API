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
        g.redis_client.set(f"task:{task_id}", task.to_dict())
        return task.to_dict()

    @staticmethod
    def get_task(task_id):
        """get_task

        Retrieves a task from Redis by its ID.

        Arguments:
            task_id (str): The ID of the task to retrieve.

        Return:
            (dict): A dictionary containing the task data if found, else an error message.
        """
        task_data = g.redis_client.get(f"task:{task_id}")
        if task_data['deleted'] == 'True':
            return None
        if task_data:
            return task_data
        return None

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
        task_data = g.redis_client.get(f"task:{task_id}")
        if not task_data:
            return None
        if task_data['deleted'] == True:
            return None
        
        task = Task(**task_data)
        execluded = ['string', '']
        if data.get('title', task.title) not in execluded:
            task.title = data.get('title', task.title)
        if data.get('description', task.description) not in execluded:
            task.description = data.get('description', task.description)
        if data.get('status', task.status) not in execluded:
            task.status = data.get('status', task.status)
        g.redis_client.set(f"task:{task_id}", task.to_dict())
        return task.to_dict()

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
        task_data = g.redis_client.get(f"task:{task_id}")
        
        task = Task(**task_data)
        task.deleted = "True"
        g.redis_client.set(f"task:{task_id}", task.to_dict())

    @staticmethod
    def get_all_tasks():
        """get_all_tasks

        Retrieves all tasks from Redis.

        Return:
            (list): A list of dictionaries containing all tasks.
        """
        return g.redis_client.get_all_with_prefix("task")
