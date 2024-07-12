import uuid
from flask import g
from models import User

class UserService:
    """UserService

    This class contains the business logic handlers for users which
    includes creating the user, updating the user, and deleting the user.
    """
    @staticmethod
    def create_user(data):
        """create_user

        This method creates a new user and stores it into the redis client.

        Arguments:
            data (dict): A dictionary containing the user data.

        Return:
            (dict): A dictionary containing the user created and a success message.
        """
        user_id = str(uuid.uuid4())
        user = User(
            user_id=user_id,
            name=data['name'],
            email=data['email'],
            password=data['password']
        )
        g.redis_client.set(user_id, user.to_dict())
        return user.to_dict()

    @staticmethod
    def get_user(user_id):
        """get_user

        Retrieves a user from Redis by its ID.

        Arguments:
            user_id (str): The ID of the user to retrieve.

        Return:
            (dict): A dictionary containing the user data if found, else an error message.
        """
        user_data = g.redis_client.get(user_id)
        if user_data:
            return user_data
        return None

    @staticmethod
    def update_user(user_id, data):
        """update_user

        Updates an existing user in Redis.

        Arguments:
            user_id (str): The ID of the user to update.
            data (dict): A dictionary containing the updated user data.

        Return:
            (dict): A dictionary containing the updated user data and a success message.
        """
        user_data = g.redis_client.get(user_id)
        if not user_data:
            return None
        
        user = User(**user_data)
        user.name = data.get('name', user.name)
        user.email = data.get('email', user.email)
        user.password = data.get('password', user.password)
        g.redis_client.set(user_id, user.to_dict())
        return user.to_dict()

    @staticmethod
    def delete_user(user_id):
        """delete_user

        Deletes a user from Redis by its ID.

        Arguments:
            user_id (str): The ID of the user to delete.

        Return:
            (dict): A dictionary containing a success message if the user was deleted,
            else an error message.
        """
        g.redis_client.client.delete(user_id)
