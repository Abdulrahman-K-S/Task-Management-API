from flask import Flask, g
from config import Config
from utils import RedisClient

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    redis_client = RedisClient(app.config['REDIS_URL'])
    app.redis_client = redis_client

    @app.before_request
    def before_request():
        g.redis_client = redis_client

    from routes import tasks_bp

    app.register_blueprint(tasks_bp, url_prefix='/api')

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)