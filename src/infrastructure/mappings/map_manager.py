from sqlalchemy import MetaData

from src.infrastructure.mappings.list_item_mapper import ListItemMapper
from src.infrastructure.mappings.list_item_status_mapper import ListItemStatusMapper
from src.infrastructure.mappings.to_do_list_mapper import ToDoListMapper


class MapManager:
    _metadata: MetaData = None

    @classmethod
    def map_entities(cls) -> MetaData:
        cls._metadata = MetaData()

        ToDoListMapper(cls._metadata).perform_mapping()
        ListItemMapper(cls._metadata).perform_mapping()
        ListItemStatusMapper(cls._metadata).perform_mapping()

        return cls._metadata
