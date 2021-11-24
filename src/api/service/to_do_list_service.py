from typing import Optional, List

from src.api.models.dto.create_to_do_list_request_dto import CreateToDoListRequestDto
from src.domain.entities.to_do_list import ToDoList
from src.infrastructure.persistance.repositories.to_do_list_repository import ToDoListRepository


class ToDoListService:
    def __init__(self):
        self.to_do_list_repository = ToDoListRepository()

    def get_all_to_do_lists(self) -> List[ToDoList]:
        return self.to_do_list_repository.all()

    def get_to_do_list(self, to_do_list_id: str) -> Optional[ToDoList]:
        return self.to_do_list_repository.get(to_do_list_id)

    def create_to_do_list(self, create_to_do_list_dto: CreateToDoListRequestDto) -> ToDoList:
        to_do_list = ToDoList.create(create_to_do_list_dto.name)
        self.to_do_list_repository.insert(to_do_list)
        return to_do_list
