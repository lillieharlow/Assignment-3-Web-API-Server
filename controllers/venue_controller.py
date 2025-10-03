from flask import Blueprint, jsonify, request
from sqlalchemy.exc import IntegrityError, DataError
from psycopg2 import errorcodes
from marshmallow import ValidationError

from init import db
from models.venue import Venue
from schemas.schemas import venue_schema, venues_schema

venues_bp = Blueprint("venues", __name__, url_prefix = "/venues")

# GET / (get all venues)
@venues_bp.route("/", methods = ["GET"])
def get_venues():
    stmt = db.select(Venue)
    venues_list = db.session.scalars(stmt)
    data = venues_schema.dump(venues_list)
    if data:
        return jsonify(data), 200
    else:
        return {"message": "No venues found. Please add a venue to get started."}, 404

# GET /id (get one venue by id)
@venues_bp.route("/<int:venue_id>", methods = ["GET"])
def get_one_venue(venue_id):
    stmt = db.select(Venue).where(Venue.venue_id == venue_id)
    venue = db.session.scalar(stmt)
    data = venue_schema.dump(venue)
    if data:
        return jsonify(data), 200
    else:
        return {"message": f"Venue with id {venue_id} doesn't exist."}, 404
    
# POST / (create a new venue)
@venues_bp.route("/", methods = ["POST"])
def create_a_venue():
    body_data = request.get_json()
    new_venue = venue_schema.load(
        body_data,
        session = db.session
    )
    db.session.add(new_venue)
    db.session.commit()
    return venue_schema.dump(new_venue), 201
    
# DELETE /id (delete venue by id)
@venues_bp.route("/<int:venue_id>", methods = ["DELETE"])
def delete_a_venue(venue_id):
    stmt = db.select(Venue).where(Venue.venue_id == venue_id)
    venue = db.session.scalar(stmt)
    if venue:
        db.session.delete(venue)
        db.session.commit()
        return {"message": f"Venue with id {venue_id} has been deleted."}, 200
    else:
        return {"message": f"Venue with id {venue_id} doesn't exist."}, 404