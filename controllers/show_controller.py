from flask import Blueprint, jsonify, request
from sqlalchemy.exc import IntegrityError
from psycopg2 import errors

from init import db
from models.show import Show
from schemas.schemas import show_schema, shows_schema

shows_bp = Blueprint("shows", __name__, url_prefix = "/shows")

"""@app.route('/show/<int:id>')
def get_show(id):
    show = Show.query.get(id)
    return jsonify({
        "show_id": show.show_id,
        # Format datetime to string exactly as requested here
        "date_time": show.date_time.strftime("%-d-%-m-%Y | %-I:%M %p"),
        "event_id": show.event_id,
        "venue_id": show.venue_id
    })"""