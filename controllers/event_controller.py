from flask import Blueprint, jsonify, request
from sqlalchemy.exc import IntegrityError
from psycopg2 import errors

from init import db
from models.event import Event
from schemas.schemas import event_schema, events_schema

events_bp = Blueprint("events", __name__, url_prefix = "/events")