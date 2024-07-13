from flask import Flask, g
from flask_restx import Api
from config import Config
from utils import RedisClient

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    redis_client = RedisClient()
    app.redis_client = redis_client

    @app.before_request
    def before_request():
        g.redis_client = redis_client

    api = Api(app, version=Config.API_VERSION, title=Config.API_TITLE,
              description=Config.API_DESCRIPTION)

    from routes import tasks_bp, users_bp, projects_bp
    api.add_namespace(tasks_bp, path='/api/tasks')
    api.add_namespace(users_bp, path='/api/users')
    api.add_namespace(projects_bp, path='/api/projects')

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
