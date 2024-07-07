import os

class Config:
    """Config

    This class contains the variables that house the
    environment details for the application
    """
    REDIS_URL = os.environ.get('REDIS_URL') or 'redis://localhost:6379/0'