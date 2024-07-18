class User:
    """User

    This class represents a user with attributes such as id, name, email, and password.
    """
    def __init__(self, user_id, name, email, password, deleted='False'):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.password = password
        self.deleted = deleted

    def to_dict(self):
        """to_dict

        Converts the User instance to a dictionary.

        Return:
            (dict): A dictionary representation of the User instance.
        """
        return {
            'user_id': self.user_id,
            'name': self.name,
            'email': self.email,
            'password': self.password,
            'deleted': self.deleted
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
            name=data['name'],
            email=data['email'],
            password=data['password'],
            deleted=data.get['deleted', 'false']
        )
