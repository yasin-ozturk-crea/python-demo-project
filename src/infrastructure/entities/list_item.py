from dataclasses import dataclass

from src.infrastructure.entities.base_entity import BaseStrEntity


@dataclass
class ListItem(BaseStrEntity):
    list_id: str
    title: str
    description: str
    status_id: int
