from __future__ import annotations

from src.domain.entities.base_entity import BaseStrEntity


class ToDoList(BaseStrEntity):
    name: str

    class Config:
        orm_mode = True

    @classmethod
    def create(cls, name: str) -> ToDoList:
        return cls(name=name)
