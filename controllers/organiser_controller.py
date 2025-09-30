from flask import Blueprint, jsonify, request
from sqlalchemy.exc import IntegrityError, DataError
from psycopg2 import errors
from marshmallow import ValidationError

from init import db
from models.organiser import Organiser
from schemas.schemas import organiser_schema, organisers_schema

organisers_bp = Blueprint("organisers", __name__, url_prefix = "/organisers")

# GET / (get all organisers)
@organisers_bp.route("/", methods = ["GET"])
def get_organisers():
    stmt = db.select(Organiser)
    organisers_list = db.session.scalars(stmt)
    data = organisers_schema.dump(organisers_list)
    if data:
        return jsonify(data), 200
    else:
        return {"message": f"No organisers found. Please add an organiser to get started."}, 404
        
# GET /id (get one organiser by id)
@organisers_bp.route("/<int:organiser_id>", methods = ["GET"])
def get_one_organiser(organiser_id):
    stmt = db.select(Organiser).where(Organiser.organiser_id == organiser_id)
    organiser = db.session.scalar(stmt)
    data = organiser_schema.dump(organiser)
    if data:
        return jsonify(data), 200
    else:
        return {"message": f"Organiser with id: {organiser_id} doesn't exist."}, 404
    
# POST / (create a new organiser)
@organisers_bp.route("/", methods = ["POST"])
def create_a_organiser():
    body_data = request.get_json()
    new_organiser = organiser_schema.load(
        body_data,
        session = db.session
    )
    db.session.add(new_organiser)
    db.session.commit()
    return organiser_schema.dump(new_organiser), 201

# PATCH/PUT /id (update organiser by id)
@organisers_bp.route("/<int:organiser_id>", methods = ["PUT", "PATCH"])
def update_a_organiser(organiser_id):
    stmt = db.select(Organiser).where(Organiser.organiser_id == organiser_id)
    organiser = db.session.scalar(stmt)
    if not organiser:
        return {"message": f"Organiser with {organiser_id} id doesn't exist."}, 404
    try:
        update_organiser = organiser_schema.load(
            request.get_json(),
            instance = organiser,
            session = db.session,
            partial = True
        )
        db.session.commit()
        return organiser_schema.dump(update_organiser), 200
    except ValidationError as e:
        return e.messages, 400
    except IntegrityError as e:
        return {"message": "Integrity error: likely a duplicate entry or invalid Foreign Key."}, 409
    except DataError as e:
        return {"message": "Data error: e.orig.diag.message_primary}."}, 400