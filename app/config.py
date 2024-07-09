import os

class Config:
    """Config

    This class contains the variables that house the
    environment details for the application
    """
    REDIS_URL = os.environ.get('REDIS_URL') or 'redis://localhost:6379/0'

    API_TITLE="Task Management API"
    API_VERSION=0.2
    API_DESCRIPTION="Task Management API is an API that helps to facilitate the task distribution between people & projects."