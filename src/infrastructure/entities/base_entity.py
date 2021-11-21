from dataclasses import dataclass
from datetime import datetime
from typing import Union


@dataclass
class BaseEntity:
    created_date: datetime
    modified_date: datetime
    id: Union[str, int]


@dataclass
class BaseStrEntity:
    id: str


@dataclass
class BaseIntEntity:
    id: int
