from __future__ import annotations

from typing import Optional

from src.domain.entities.base_entity import BaseStrEntity
from src.domain.entities.list_item_status import ListItemStatus, ListItemStatuses
from src.domain.entities.to_do_list import ToDoList


class ListItem(BaseStrEntity):
    list_id: str
    title: str
    description: Optional[str]
    status_id: int

    to_do_list: Optional[ToDoList]
    status: Optional[ListItemStatus]

    class Config:
        orm_mode = True

    @classmethod
    def create(cls, list_id: str, title: str, description: Optional[str]) -> ListItem:
        return cls(list_id=list_id,
                   title=title,
                   description=description,
                   status_id=ListItemStatuses.pending.id,
                   status=ListItemStatuses.pending)
