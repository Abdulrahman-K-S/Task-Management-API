from flask import Flask
from config import Config
from utils.redis_client import RedisClient

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    redis_client = RedisClient(app.config['REDIS_URL'])

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)