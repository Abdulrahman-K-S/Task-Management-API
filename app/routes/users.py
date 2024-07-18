from flask_restx import Namespace, Resource, fields
from controllers import UserController

users_bp = Namespace('users', description='User operations')

user_model = users_bp.model('User', {
    'name': fields.String(required=True, description='The user name'),
    'email': fields.String(required=True, description='The user email'),
    'password': fields.String(required=True, description='The user password')
})

@users_bp.route('/')
class UserList(Resource):
    @users_bp.expect(user_model)
    @users_bp.response(201, 'User created successfully')
    def post(self):
        """Create a new user"""
        return UserController.create_user()

    @users_bp.response(200, 'Users retrieved successfully')
    def get(self):
        """Retrieve all users"""
        return UserController.get_all_users()

@users_bp.route('/<user_id>')
@users_bp.param('user_id', 'The user identifier')
class User(Resource):
    @users_bp.response(200, 'User found')
    @users_bp.response(404, 'User not found')
    def get(self, user_id):
        """Fetch a user given its identifier"""
        return UserController.get_user(user_id)

    @users_bp.expect(user_model)
    @users_bp.response(200, 'User updated successfully')
    @users_bp.response(404, 'User not found')
    def put(self, user_id):
        """Update a user given its identifier"""
        return UserController.update_user(user_id)

    @users_bp.response(200, 'User deleted successfully')
    @users_bp.response(404, 'User not found')
    def delete(self, user_id):
        """Delete a user given its identifier"""
        return UserController.delete_user(user_id)

@users_bp.route('/<user_id>/tasks')
@users_bp.param('user_id', 'The user identifier')
class UserTasks(Resource):
    @users_bp.response(200, 'User tasks found')
    def get(self, user_id):
        """Fetch the tasks assigned to user"""
        return UserController.get_tasks_assigned_to_user(user_id)
