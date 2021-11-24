from datetime import datetime
from typing import Optional, Dict, Any
from uuid import uuid4

from pydantic import BaseModel, Field


class BaseEntity(BaseModel):
    created_date: datetime = Field(default_factory=datetime.utcnow)
    modified_date: Optional[datetime] = None

    class Config:
        orm_mode = True

    def to_orm(self) -> Dict[str, Any]:
        return self.dict()


class BaseStrEntity(BaseEntity):
    id: str = Field(default_factory=lambda: str(uuid4()))


class BaseIntEntity(BaseEntity):
    id: int = 0
