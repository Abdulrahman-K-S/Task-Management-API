from flask_restx import Namespace, Resource, fields
from controllers import ProjectController

projects_bp = Namespace('projects', description='Project operations')

project_model = projects_bp.model('Project', {
    'name': fields.String(required=True, description='The project name'),
    'description': fields.String(required=True, description='The project description'),
    'status': fields.String(description='The project status')
})

@projects_bp.route('/')
class ProjectList(Resource):
    @projects_bp.expect(project_model)
    @projects_bp.response(201, 'Project created successfully')
    def post(self):
        """Create a new project"""
        return ProjectController.create_project()
    
    @projects_bp.response(200, 'Users retrieved successfully')
    def get(self):
        """Retrieve all users"""
        return ProjectController.get_all_projects()

@projects_bp.route('/<project_id>')
@projects_bp.param('project_id', 'The project identifier')
class Project(Resource):
    @projects_bp.response(200, 'Project found')
    @projects_bp.response(404, 'Project not found')
    def get(self, project_id):
        """Fetch a project given its identifier"""
        return ProjectController.get_project(project_id)

    @projects_bp.expect(project_model)
    @projects_bp.response(200, 'Project updated successfully')
    @projects_bp.response(404, 'Project not found')
    def put(self, project_id):
        """Update a project given its identifier"""
        return ProjectController.update_project(project_id)

    @projects_bp.response(200, 'Project deleted successfully')
    @projects_bp.response(404, 'Project not found')
    def delete(self, project_id):
        """Delete a project given its identifier"""
        return ProjectController.delete_project(project_id)

@projects_bp.route('/<project_id>/<task_id>')
@projects_bp.param('project_id', 'The project identifier')
@projects_bp.param('task_id', 'The task identifier')
class ProjectTask(Resource):
    @projects_bp.response(200, 'Tasks found')
    @projects_bp.response(404, 'Project not found or no tasks assigned')
    def put(self, project_id, task_id):
        """Update a task to the project's list"""
        return ProjectController.assign_task_to_project(task_id, project_id)

@projects_bp.route('/<project_id>/tasks')
@projects_bp.param('project_id', 'The project identifier')
class ProjectTasks(Resource):
    @projects_bp.response(200, 'Tasks found')
    @projects_bp.response(404, 'Project not found or no tasks assigned')
    def get(self, project_id):
        """Fetch all tasks assigned to a project"""
        return ProjectController.get_tasks_for_project(project_id)
