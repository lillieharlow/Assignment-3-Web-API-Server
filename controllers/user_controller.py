from flask import Blueprint, jsonify, request
from sqlalchemy.exc import IntegrityError, DataError
from psycopg2 import errorcodes

from init import db
from models.user import User
from schemas.schemas import user_schema, users_schema

users_bp = Blueprint("users", __name__, url_prefix = "/users")

# GET / (get all users)
@users_bp.route("/")
def get_users():
    stmt = db.select(User)
    users_list = db.session.scalars(stmt)
    data = users_schema.dump(users_list)
    if data:
        return jsonify(data), 200
    else:
        return {"message": "No users found. Please add a user to get started."}, 404

# GET /id (get one user by id)
@users_bp.route("/<int:user_id>")
def get_one_user(user_id):
    stmt = db.select(User).where(User.user_id == user_id)
    user = db.session.scalar(stmt)
    data = user_schema.dump(user)
    if data:
        return jsonify(data), 200
    else:
        return {"message": f"User with id: {user_id} doesn't exist."}, 404

# POST / (create a new user)
@users_bp.route("/", methods = ["POST"])
def create_a_user():
    body_data = request.get_json()
    new_user = user_schema.load(
        body_data,
        session = db.session
    )
    db.session.add(new_user)
    db.session.commit()
    return user_schema.dump(new_user), 201

# PATCH/PUT /id (update user by id)
@users_bp.route("/<int:user_id>")
def update_a_user(user_id):
    