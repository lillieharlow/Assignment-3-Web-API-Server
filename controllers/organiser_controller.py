from flask import Blueprint, jsonify, request
from sqlalchemy.exc import IntegrityError
from psycopg2 import errors

from init import db
from models.organiser import Organiser
from schemas.schemas import organiser_schema, organisers_schema

organisers_bp = Blueprint("organisers", __name__, url_prefix = "/organisers")