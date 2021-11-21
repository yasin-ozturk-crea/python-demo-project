import os
from pathlib import Path
from typing import Optional

from pydantic import BaseSettings, Field, Extra

# get root directory: root/src/config.py -> root
# then create envs directory: root/envs/
envs_dir = os.path.join(Path(__file__).parent.parent.absolute(), 'envs')


class GlobalConfig(BaseSettings):
    """Global Configuration"""

    ENVIRONMENT: str = Field('dev', env='ENVIRONMENT')

    MYSQL_HOST: Optional[str]
    MYSQL_PASSWORD: Optional[str]
    MYSQL_USER: Optional[str]
    MYSQL_DB_NAME: Optional[str]

    SQLALCHEMY_DATABASE_URI: Optional[str]
    SQLALCHEMY_TRACK_MODIFICATIONS: Optional[bool] = Field(False)

    class Config:
        extra = Extra.allow

    def create_db_uri(self) -> str:
        self.SQLALCHEMY_DATABASE_URI \
            = f'mysql+mysqldb://{self.MYSQL_USER}:{self.MYSQL_PASSWORD}@{self.MYSQL_HOST}/{self.MYSQL_DB_NAME}?charset=utf8mb4'
        return self.SQLALCHEMY_DATABASE_URI


class DevConfig(GlobalConfig):
    class Config:
        env_file: str = os.path.join(envs_dir, 'dev.env')


class ProdConfig(GlobalConfig):
    class Config:
        env_file: str = os.path.join(envs_dir, 'prod.env')


class ConfigManager:
    config: GlobalConfig

    @classmethod
    def init_config(cls) -> GlobalConfig:
        environment = GlobalConfig().ENVIRONMENT
        if environment == 'dev':
            cls.config = DevConfig()
        elif environment == 'prod':
            cls.config = ProdConfig()
        else:
            raise Exception('Environment is not found')  # TODO: create custom error

        cls.config.create_db_uri()
        return cls.config
