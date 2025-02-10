# from src.models.data_store_manager import DataStoreManager, DataList
# from typing import List, Optional, Union
# from json import JSONDecodeError
# from src.models._entities import UserColumn, UserEntity, UserModel
# from serde import SerdeError, serde
# from uuid import UUID, uuid4
# from datetime import datetime
# from werkzeug.exceptions import InternalServerError

# INACTIVE_USER_THRESHOLD = 60 * 60 # 1 hour

# @serde
# class NewUserModel:
#     name: str

#     def __init__(self, name: str):
#         self.name = name


# def create_user(list_model: NewUserModel) -> UserModel:
#     """Creates a new todo list in the data store.

#     Args:
#         list_model (NewUserModel): The new todo list to create.

#     Raises:
#         FileNotFoundError: If the data store file is not found.
#         JSONDecodeError: If the data store file is not a valid JSON file.
#         SerdeError: If the data cannot be serialized.

#     Returns:
#         UserModel: The created todo list.
#     """
#     try:
#         _remove_inactive_users()

#         return UserEntity().create(
#             DataStoreManager,
#             DataList.USERS,
#             UserModel(id=str(uuid4()), name=list_model.name, last_active=datetime.now().timestamp()),
#         )
#     except (FileNotFoundError, JSONDecodeError, SerdeError) as error:
#         raise error


# def update_user_activity(user: UUID):
#     """Updates the last active timestamp of a user.

#     Args:
#         user (UUID): The user to update.

#     Raises:
#         InternalServerError: If the user cannot be updated.
#     """
#     try:
#         entity = UserEntity()

#         entity.where(UserColumn.ID, user)

#         user: Optional[UserModel] = entity.one(DataStoreManager)

#         if user is None:
#             return
#         user.last_active = datetime.now().timestamp()

#         entity.update(DataStoreManager, user)
#     except Exception as error:
#         raise InternalServerError from error

# def _remove_inactive_users():
#     """Removes users that have been inactive for a certain period of time.

#     Raises:
#         InternalServerError: If the users cannot be removed.
#     """
#     try:
#         users = UserEntity().all(DataStoreManager)
#         for user in users:
#             if user.last_active < datetime.now().timestamp() - INACTIVE_USER_THRESHOLD:
#                 UserEntity().remove(DataStoreManager, user)
#     except Exception as error:
#         raise InternalServerError from error

