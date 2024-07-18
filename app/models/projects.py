class Project:
    """Project

    This class represents a project with attributes such as id, name, description, and status.
    """
    def __init__(self, project_id, name, description, status='active', deleted='false'):
        self.project_id = project_id
        self.name = name
        self.description = description
        self.status = status
        self.deleted = deleted

    def to_dict(self):
        """to_dict

        Converts the Project instance to a dictionary.

        Return:
            (dict): A dictionary representation of the Project instance.
        """
        return {
            'project_id': self.project_id,
            'name': self.name,
            'description': self.description,
            'status': self.status,
            'deleted': self.deleted
        }

    @staticmethod
    def from_dict(data):
        """from_dict

        Creates a Project instance from a dictionary.

        Arguments:
            data (dict): A dictionary containing project data.

        Return:
            (Project): A Project instance created from the given data.
        """
        return Project(
            project_id=data['project_id'],
            name=data['name'],
            description=data.get('description', ''),
            status=data.get('status', 'active'),
            deleted=data.get('deleted', 'false')
        )
