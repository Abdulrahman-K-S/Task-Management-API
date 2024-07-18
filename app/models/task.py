class Task:
    """Task

    This class represents a task with a attributes such as
    id, title, and status.
    """
    def __init__(self, task_id, title, description, status='pending', deleted='false'):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.status = status
        self.deleted = deleted

    def to_dict(self):
        """to_dict

        Converts the Task instance to a dictionary.

        Return:
            (dict): A dictionary representation of the Task instance.
        """
        return {
            'task_id': self.task_id,
            'title': self.title,
            'description': self.description,
            'status': self.status,
            'deleted': self.deleted
        }

    @staticmethod
    def from_dict(data):
        """from_dict

        Creates a Task instance from a dictionary.

        Arguments:
            data (dict): A dictionary containing task data.

        Return:
            (Task): A Task instance created from the given data.
        """
        return Task(
            task_id=data['task_id'],
            title=data['title'],
            description=data.get('description', ''),
            status=data.get('status', 'pending'),
            deleted=data.get('deleted', 'false')
        )
