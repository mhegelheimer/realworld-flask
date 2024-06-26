from flask import Blueprint, request
from realworld.api.models.users import (
    CreateUserRequest,
    UpdateUserRequest,
    AuthenticateUserRequest,
    SingleUserResponse,
)


users_blueprint = Blueprint(
    "users_endpoints",
    __name__,
)


@users_blueprint.route("/users", methods=["POST"])
def create_user() -> SingleUserResponse:
    # Authorization: Token jwt.token.here
    data = CreateUserRequest.model_validate_json(request.json)
    assert data
    return {
        "user": {
            "email": "user@realworld.io",
            "token": "jwt.token.here",
            "username": "user",
            "bio": "I am a user.",
            "image": None,
        }
    }


@users_blueprint.route("/users/login", methods=["POST"])
def authenticate_user() -> SingleUserResponse:
    request_model = AuthenticateUserRequest()
    request_model.model_validate_json(request.json)
    return {
        "user": {
            "email": "user@realworld.io",
            "token": "jwt.token.here",
            "username": "user",
            "bio": "I am a user.",
            "image": None,
        }
    }


@users_blueprint.route("/user", methods=["GET"])
def get_current_user() -> SingleUserResponse:
    return {
        "user": {
            "email": "user@realworld.io",
            "token": "jwt.token.here",
            "username": "user",
            "bio": "I am a user.",
            "image": None,
        }
    }


@users_blueprint.route("/user", methods=["PUT"])
def update_user() -> SingleUserResponse:
    request_model = UpdateUserRequest()
    request_model.model_validate_json(request.json)
    return {
        "user": {
            "email": "user@realworld.io",
            "token": "jwt.token.here",
            "username": "user",
            "bio": "I am a user.",
            "image": None,
        }
    }
