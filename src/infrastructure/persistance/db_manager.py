from typing import Callable

from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy_utils import database_exists, create_database

from src.config import GlobalConfig
from src.infrastructure.mappings.map_manager import MapManager


class DBManager:
    engine: Engine
    session_factory: Callable[..., Session]

    @classmethod
    def start_db(cls, config: GlobalConfig, app: Flask) -> None:
        cls.engine = create_engine(config.SQLALCHEMY_DATABASE_URI)

        cls.session_factory = sessionmaker(
            autocommit=False,
            autoflush=True,
            bind=cls.engine
        )

        metadata = MapManager.map_entities()

        with app.app_context():
            db = SQLAlchemy(metadata=metadata)
            db.init_app(app)

            migration = Migrate(app, db)
            # migration.init_app(app)

            if config.ENVIRONMENT == 'dev' and not database_exists(cls.engine.url):
                create_database(cls.engine.url, encoding='utf8mb4')

    @classmethod
    def new_session(cls) -> Session:
        return cls.session_factory()
