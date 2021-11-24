from typing import Optional

from flask import Flask
from flask_restx import Api

from src.api.controllers import to_do_list_api
from src.api.controllers.to_do_list_controller import api as to_do_api
from src.api.controllers.list_item_controller import api as list_item_api


class APIManager:
    def __init__(self, app: Flask) -> None:
        self.api: Optional[Api] = None
        self.init_apis(app)

    def init_apis(self, app: Flask) -> None:
        self.api = Api(
            to_do_list_api,
            title='To Do List API',
            version='0.0.1',
            description='First version of the to do list API'
        )

        self.api.add_namespace(to_do_api)
        self.api.add_namespace(list_item_api)

        app.register_blueprint(to_do_list_api)
