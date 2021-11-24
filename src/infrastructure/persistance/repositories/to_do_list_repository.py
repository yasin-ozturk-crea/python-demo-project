from typing import Optional, List

from src.domain.entities.to_do_list import ToDoList as DomainToDoList
from src.infrastructure.entities.to_do_list import ToDoList
from src.infrastructure.persistance.db_manager import DBManager


class ToDoListRepository:
    def __init__(self) -> None:
        pass

    def get(self, to_do_list_id: str) -> Optional[DomainToDoList]:
        session = DBManager.new_session()
        to_do_list = session.query(ToDoList).get(to_do_list_id)
        if to_do_list:
            return DomainToDoList.parse_obj(to_do_list.__dict__)
        return None

    def all(self) -> List[DomainToDoList]:
        session = DBManager.new_session()
        to_do_lists = session.query(ToDoList).all()
        return [DomainToDoList.parse_obj(to_do_list.__dict__) for to_do_list in to_do_lists]

    def insert(self, to_do_list: DomainToDoList) -> None:
        session = DBManager.new_session()
        session.add(ToDoList.from_dict(to_do_list.to_orm()))
        session.commit()
