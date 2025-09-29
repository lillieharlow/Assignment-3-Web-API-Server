from flask import Blueprint, jsonify, request
from sqlalchemy.exc import IntegrityError
from psycopg2 import errors

from init import db
from models.venue import Venue
from schemas.schemas import venue_schema, venues_schema

venues_bp = Blueprint("venues", __name__, url_prefix = "/venues")