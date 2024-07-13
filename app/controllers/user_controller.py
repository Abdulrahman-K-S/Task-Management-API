from flask import request, jsonify, g
from services import UserService
from flask_restx import abort

class UserController:
    """UserController

    This class handles the HTTP requests for users, including creating, retrieving,
    updating, and deleting users.
    """

    @staticmethod
    def create_user():
        """create_user

        Handles the HTTP POST request to create a new user.

        Return:
            (Response): A Flask response object containing the created user data and a success message.
        """
        data = request.json

        if not data or 'name' not in data or 'email' not in data or 'password' not in data:
            abort(400, 'Name, email, and password are required')

        user = UserService.create_user(data)
        return {"message": "User created successfully", "user": user}, 201

    @staticmethod
    def get_user(user_id):
        """get_user

        Handles the HTTP GET request to retrieve a user by its ID.

        Arguments:
            user_id (str): The ID of the user to retrieve.

        Return:
            (Response): A Flask response object containing the user data if found, else an error message.
        """
        user = UserService.get_user(user_id)
        
        if not user:
            abort(404, 'User not found')

        return {"user": user}, 200

    @staticmethod
    def update_user(user_id):
        """update_user

        Handles the HTTP PUT request to update an existing user.

        Arguments:
            user_id (str): The ID of the user to update.

        Return:
            (Response): A Flask response object containing the updated user data and a success message.
        """
        data = request.json

        if not data:
            abort(400, 'No data provided')
        if UserService.get_user(user_id) is None:
            abort(404, 'User not found')

        user = UserService.update_user(user_id, data)
        return {"message": "User updated successfully", "user": user}, 200

    @staticmethod
    def delete_user(user_id):
        """delete_user

        Handles the HTTP DELETE request to delete a user by its ID.

        Arguments:
            user_id (str): The ID of the user to delete.

        Return:
            (Response): A Flask response object containing a success message if the user was deleted, else an error message.
        """
        if UserService.get_user(user_id) is None:
            abort(404, 'User not found')
        UserService.delete_user(user_id)
        return {"message": "User deleted successfully"}, 200
