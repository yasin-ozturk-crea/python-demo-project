from flask import Flask

from src.config import ConfigManager


def create_app() -> Flask:
    app = Flask(__name__)

    config = ConfigManager.init_config()
    app.config.from_object(config)

    from src.infrastructure.persistance.db_manager import DBManager
    DBManager.start_db(config, app)

    from src.api.helpers.api_manager import APIManager
    APIManager(app)

    return app
