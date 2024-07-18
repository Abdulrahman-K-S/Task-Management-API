import uuid
from flask import g
from models import Project

class ProjectService:
    """ProjectService

    This class contains the business logic handlers for projects which
    includes creating the project, updating the project, and deleting the project.
    """
    @staticmethod
    def create_project(data):
        """create_project

        This method creates a new project and stores it into the redis client.

        Arguments:
            data (dict): A dictionary containing the project data.

        Return:
            (dict): A dictionary containing the project created and a success message.
        """
        project_id = str(uuid.uuid4())
        project = Project(
            project_id=project_id,
            name=data['name'],
            description=data.get('description', '')
        )
        g.redis_client.set(f"project:{project_id}", project.to_dict())
        return project.to_dict()

    @staticmethod
    def get_project(project_id):
        """get_project

        Retrieves a project from Redis by its ID.

        Arguments:
            project_id (str): The ID of the project to retrieve.

        Return:
            (dict): A dictionary containing the project data if found, else an error message.
        """
        project_data = g.redis_client.get(f"project:{project_id}")
        if project_data['deleted'] == True:
            return None
        if project_data:
            return project_data
        return None

    @staticmethod
    def update_project(project_id, data):
        """update_project

        Updates an existing project in Redis.

        Arguments:
            project_id (str): The ID of the project to update.
            data (dict): A dictionary containing the updated project data.

        Return:
            (dict): A dictionary containing the updated project data and a success message.
        """
        project_data = g.redis_client.get(f"project:{project_id}")
        if not project_data:
            return None
        if project_data['deleted'] == True:
            return None
        
        project = Project(**project_data)
        execluded = ['string', '']
        if data.get('name', project.name) not in execluded:
            project.name = data.get('name', project.name)
        if data.get('description', project.description) not in execluded:
            project.description = data.get('description', project.description)
        if data.get('status', project.status) not in execluded:
            project.status = data.get('status', project.status)
        g.redis_client.set(f"project:{project_id}", project.to_dict())
        return project.to_dict()

    @staticmethod
    def delete_project(project_id):
        """delete_project

        Deletes a project from Redis by its ID.

        Arguments:
            project_id (str): The ID of the project to delete.

        Return:
            (dict): A dictionary containing a success message if the project was deleted,
            else an error message.
        """
        project_data = g.redis_client.get(f"project:{project_id}")
        
        project = Project(**project_data)
        project.deleted = "True"
        g.redis_client.set(f"project:{project_id}", project.to_dict())

    @staticmethod
    def get_all_projects():
        """get_all_projects

        Retrieves all projects from Redis.

        Return:
            (list): A list of dictionaries containing all projects.
        """
        return g.redis_client.get_all_with_prefix("project")
