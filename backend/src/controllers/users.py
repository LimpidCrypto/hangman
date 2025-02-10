
# from datetime import datetime
# import random
# from uuid import UUID
# from flask import Blueprint, request
# from src.models._entities import UserEntity
# from src.models.data_store_manager import DataStoreManager
# from src.models.users import NewUserModel, create_user
# from zufallsworte import zufallswoerter, anzahl_buchstaben
# from werkzeug.exceptions import InternalServerError


# USERS_CONTROLLER = Blueprint("users", __name__)

# @USERS_CONTROLLER.route("/users", methods=["POST"])
# @USERS_CONTROLLER.errorhandler(InternalServerError)
# def create_users():
#     try:
#         data = request.json
#         usernames = data["usernames"]
#         new_users = []
#         for username in usernames:
#             new_user_model = NewUserModel(name=username)
#             created_user = create_user(new_user_model)
#             new_users.append(created_user)

#         return {"users": new_users}, 201
#     except Exception as error:
#         raise InternalServerError from error
