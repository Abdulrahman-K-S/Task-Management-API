from flask import request, jsonify, g
from services import ProjectService
from flask_restx import abort

class ProjectController:
    """ProjectController

    This class handles the HTTP requests for projects, including creating, retrieving,
    updating, and deleting projects.
    """

    @staticmethod
    def create_project():
        """create_project

        Handles the HTTP POST request to create a new project.

        Return:
            (Response): A Flask response object containing the created project data and a success message.
        """
        data = request.json

        if not data or 'name' not in data:
            abort(400, 'Project name is required')

        project = ProjectService.create_project(data)
        return {"message": "Project created successfully", "project": project}, 201

    @staticmethod
    def get_project(project_id):
        """get_project

        Handles the HTTP GET request to retrieve a project by its ID.

        Arguments:
            project_id (str): The ID of the project to retrieve.

        Return:
            (Response): A Flask response object containing the project data if found, else an error message.
        """
        project = ProjectService.get_project(project_id)
        
        if not project:
            abort(404, 'Project not found')

        return {"project": project}, 200

    @staticmethod
    def update_project(project_id):
        """update_project

        Handles the HTTP PUT request to update an existing project.

        Arguments:
            project_id (str): The ID of the project to update.

        Return:
            (Response): A Flask response object containing the updated project data and a success message.
        """
        data = request.json

        if not data:
            abort(400, 'No data provided')
        if ProjectService.get_project(project_id) is None:
            abort(404, 'Project not found')

        project = ProjectService.update_project(project_id, data)
        return {"message": "Project updated successfully", "project": project}, 200

    @staticmethod
    def delete_project(project_id):
        """delete_project

        Handles the HTTP DELETE request to delete a project by its ID.

        Arguments:
            project_id (str): The ID of the project to delete.

        Return:
            (Response): A Flask response object containing a success message if the project was deleted, else an error message.
        """
        if ProjectService.get_project(project_id) is None:
            abort(404, "Project not found")
        ProjectService.delete_project(project_id)
        return {"message": "Project deleted successfully"}, 200

    @staticmethod
    def get_all_projects():
        """get_all_projects

        Handles the HTTP GET request to retrieve all projects.

        Return:
            (Response): A Flask response object containing all projects data.
        """
        projects = ProjectService.get_all_projects()
        return {"projects": projects}, 200
