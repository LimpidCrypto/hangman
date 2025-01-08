
import random
from flask import Blueprint, request
from zufallsworte import zufallswoerter, anzahl_buchstaben
from werkzeug.exceptions import InternalServerError

USERS_CONTROLLER = Blueprint("users", __name__)

@USERS_CONTROLLER.route("/users", methods=["POST"])
@USERS_CONTROLLER.errorhandler(InternalServerError)
def create_users():
    print(request.json)
    return "User created", 200
