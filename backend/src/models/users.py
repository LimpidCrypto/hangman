from src.models.data_store_manager import DataStoreManager, DataList
from typing import List, Optional
from json import JSONDecodeError
from src.models._entities import UserEntity, UserModel
from serde import SerdeError, serde
from uuid import UUID, uuid4
from datetime import datetime


@serde
class NewUserModel:
    name: str

    def __init__(self, name: str):
        self.name = name


def create_user(list_model: NewUserModel) -> UserModel:
    """Creates a new todo list in the data store.

    Args:
        list_model (NewUserModel): The new todo list to create.

    Raises:
        FileNotFoundError: If the data store file is not found.
        JSONDecodeError: If the data store file is not a valid JSON file.
        SerdeError: If the data cannot be serialized.

    Returns:
        UserModel: The created todo list.
    """
    try:
        return UserEntity().create(
            DataStoreManager,
            DataList.LISTS,
            UserModel(id=str(uuid4()), name=list_model.name, last_active=datetime.now().timestamp()),
        )
    except (FileNotFoundError, JSONDecodeError, SerdeError) as error:
        raise error
