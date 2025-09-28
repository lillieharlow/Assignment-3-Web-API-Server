from flask import Blueprint, jsonify, request
from sqlalchemy.exc import IntegrityError
from psycopg2 import errors

from init import db
from models.user import User
from schemas.schemas import user_schema, users_schema

users_bp = Blueprint("users", __name__, url_prefix = "/users")

# Define routes for user operations
# GET /
@users_bp.route("/")
def get_users():
    stmt = db.select(User)
    users_list = db.session.scalars(stmt)
    data = users_schema.dump(users_list)
    if data:
        return jsonify(data), 200
    else:
        return {"message": "No users found. Please add a user to get started."}, 404