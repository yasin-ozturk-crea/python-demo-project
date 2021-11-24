from typing import List

from flask import Response, request
from flask_restx import Namespace, Resource

from src.api.models.base_response import BaseResponse
from src.api.models.dto.create_to_do_list_request_dto import CreateToDoListRequestDto
from src.api.service.to_do_list_service import ToDoListService
from src.domain.entities.to_do_list import ToDoList

api = Namespace('to do', description='API for to do list', path='/to_do_lists')


# request dto
create_to_do_list_request = api.schema_model('create_to_do_list_request_dto', CreateToDoListRequestDto.schema())

# response dto
to_do_list_response = api.schema_model('to_do_list_response_dto', BaseResponse[ToDoList].schema())
to_do_lists_response = api.schema_model('to_do_lists_response_dto', BaseResponse[List[ToDoList]].schema())

# model
to_do_list_model = api.schema_model('ToDoList', ToDoList.schema())


@api.route('')
class GetCreateToDoList(Resource):
    @api.response(200, 'OK', to_do_lists_response)
    def get(self) -> Response:
        to_do_list_service = ToDoListService()
        to_do_lists = to_do_list_service.get_all_to_do_lists()

        return BaseResponse.create_response(message='To do lists obtained', data=to_do_lists)

    @api.response(200, 'OK', to_do_lists_response)
    @api.expect(to_do_list_model, create_to_do_list_request)
    def post(self) -> Response:
        data = request.get_json()
        create_to_do_list_dto = CreateToDoListRequestDto.parse_obj(data)

        to_do_list_service = ToDoListService()
        to_do_list = to_do_list_service.create_to_do_list(create_to_do_list_dto)

        return BaseResponse.create_response(message='To do list created', data=to_do_list)


@api.route('/<to_do_list_id>')
class GetToDoList(Resource):
    @api.response(200, 'OK', to_do_lists_response)
    @api.response(404, 'Not Found')
    def get(self, to_do_list_id: str) -> Response:
        to_do_list_service = ToDoListService()
        to_do_list = to_do_list_service.get_to_do_list(to_do_list_id)

        if not to_do_list:
            return BaseResponse.create_response(success=False, message='No to do list found', status_code=404)
        return BaseResponse.create_response(message='To do list obtained', data=to_do_list)

    @api.response(200, 'OK')
    def post(self, to_do_list_id: str) -> Response:
        # to do list güncelleme
        pass
