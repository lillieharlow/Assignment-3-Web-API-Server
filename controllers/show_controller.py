from flask import Blueprint, jsonify, request
from sqlalchemy.exc import IntegrityError
from psycopg2 import errors

from init import db
from models.show import Show
from schemas.schemas import show_schema, shows_schema

shows_bp = Blueprint("shows", __name__, url_prefix = "/shows")