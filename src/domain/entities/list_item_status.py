from typing import Dict, List

from pydantic import Field

from src.domain.entities.base_entity import BaseIntEntity


class ListItemStatus(BaseIntEntity):
    status: str = Field(..., min_length=3, max_length=30)

    class Config:
        orm_mode = True
        allow_mutation = False


class ListItemStatuses:
    pending = ListItemStatus.construct(id=1, status='Pending')
    completed = ListItemStatus.construct(id=2, status='Completed')
    deleted = ListItemStatus.construct(id=3, status='Deleted')

    _statuses: Dict[int, ListItemStatus] = {
        1: pending,
        2: completed,
        3: deleted
    }

    @classmethod
    def get_status(cls, status_id: int) -> ListItemStatus:
        if status_id in cls._statuses:
            return cls._statuses[status_id]
        raise Exception(f'Status ID {status_id} does not exist in the predefined list item statuses.')

    @classmethod
    def get_all(cls) -> List[ListItemStatus]:
        return list(cls._statuses.values())
