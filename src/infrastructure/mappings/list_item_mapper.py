from sqlalchemy import MetaData, Table, Column, String, DateTime, Integer, ForeignKey
from sqlalchemy.orm import mapper, relationship

from src.infrastructure.entities.list_item import ListItem
from src.infrastructure.entities.list_item_status import ListItemStatus
from src.infrastructure.entities.to_do_list import ToDoList


class ListItemMapper:
    def __init__(self, metadata: MetaData):
        self._metadata = metadata

    def perform_mapping(self) -> Table:
        list_item_mapping = Table('list_items', self._metadata,
                                  Column('id', String(36), primary_key=True),
                                  Column('created_date', DateTime, nullable=False),
                                  Column('modified_date', DateTime),
                                  Column('list_id', String(36), ForeignKey('to_do_lists.id'), nullable=False),
                                  Column('title', String(30), nullable=False),
                                  Column('description', String(255 * 4)),
                                  Column('status_id', Integer, ForeignKey('list_item_statuses.id'), nullable=False))

        mapper(ListItem, list_item_mapping, properties={
            'to_do_list': relationship(ToDoList, uselist=False),
            'status': relationship(ListItemStatus, uselist=False)
        })

        return list_item_mapping
