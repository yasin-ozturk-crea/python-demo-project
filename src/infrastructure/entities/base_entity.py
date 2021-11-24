import inspect
from dataclasses import dataclass
from datetime import datetime
from typing import Union, TypeVar, Type, Dict, Any

TEntity = TypeVar('TEntity', bound='BaseEntity')


@dataclass
class BaseEntity:
    created_date: datetime
    modified_date: datetime
    id: Union[str, int]

    @classmethod
    def from_dict(cls: Type[TEntity], env: Dict[str, Any]) -> TEntity:
        return cls(**{
            k: v for k, v in env.items()
            if k in inspect.signature(cls).parameters
        })


@dataclass
class BaseStrEntity(BaseEntity):
    id: str


@dataclass
class BaseIntEntity(BaseEntity):
    id: int
