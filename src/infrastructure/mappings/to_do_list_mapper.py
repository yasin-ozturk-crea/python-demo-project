from sqlalchemy import MetaData, Table, Column, String, DateTime
from sqlalchemy.orm import mapper

from src.infrastructure.entities.to_do_list import ToDoList


class ToDoListMapper:
    def __init__(self, metadata: MetaData):
        self._metadata = metadata

    def perform_mapping(self) -> Table:
        to_do_list_mapping = Table('to_do_lists', self._metadata,
                                   Column('id', String(36), primary_key=True),
                                   Column('created_date', DateTime, nullable=False),
                                   Column('modified_date', DateTime),
                                   Column('name', String(30), nullable=False, index=True))

        mapper(ToDoList, to_do_list_mapping)

        return to_do_list_mapping
