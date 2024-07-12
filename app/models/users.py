class User:
    """User

    This class represents a user with attributes such as id, username, and email.
    """
    def __init__(self, user_id, username, email, password):
        self.user_id = user_id
        self.username = username
        self.email = email
        self.password = password  # In a real application, make sure to hash passwords

    def to_dict(self):
        """to_dict

        Converts the User instance to a dictionary.

        Return:
            (dict): A dictionary representation of the User instance.
        """
        return {
            'user_id': self.user_id,
            'username': self.username,
            'email': self.email,
            'password': self.password  # In a real application, exclude the password or use a hashed version
        }

    @staticmethod
    def from_dict(data):
        """from_dict

        Creates a User instance from a dictionary.

        Arguments:
            data (dict): A dictionary containing user data.

        Return:
            (User): A User instance created from the given data.
        """
        return User(
            user_id=data['user_id'],
            username=data['username'],
            email=data['email'],
            password=data['password']
        )
