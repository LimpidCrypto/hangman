from enum import Enum
from typing import Dict
from serde import serde, from_dict
from src.models._entities import BaseEntity


@serde
class Model:
    id: str
    name: str
    last_active: float

    def __init__(self, id: str, name: str, last_active: float) -> None:
        self.id = id
        self.name = name
        self.last_active = last_active


class Entity(BaseEntity[Model]):
    def _deserialize(self, data: Dict[str, str]) -> Model:
        return from_dict(Model, data)


class Column(Enum):
    ID = "id"
    NAME = "name"
    LAST_ACTIVE = "last_active"