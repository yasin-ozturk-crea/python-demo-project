from dataclasses import dataclass

from src.infrastructure.entities.base_entity import BaseIntEntity


@dataclass
class ListItemStatus(BaseIntEntity):
    status: str
