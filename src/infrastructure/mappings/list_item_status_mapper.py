from sqlalchemy import MetaData, Table, Column, String, DateTime, Integer
from sqlalchemy.orm import mapper

from src.infrastructure.entities.list_item_status import ListItemStatus


class ListItemStatusMapper:
    def __init__(self, metadata: MetaData):
        self._metadata = metadata

    def perform_mapping(self) -> Table:
        list_item_status_mapping = Table('list_item_statuses', self._metadata,
                                         Column('id', Integer, primary_key=True),
                                         Column('created_date', DateTime, nullable=False),
                                         Column('modified_date', DateTime),
                                         Column('status', String(30), nullable=False))

        mapper(ListItemStatus, list_item_status_mapping)

        return list_item_status_mapping
