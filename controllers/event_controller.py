from flask import Blueprint, jsonify, request
from sqlalchemy.exc import IntegrityError, DataError
from psycopg2 import errorcodes
from marshmallow import ValidationError

from init import db
from models.event import Event
from schemas.schemas import event_schema, events_schema

events_bp = Blueprint("events", __name__, url_prefix = "/events")

# GET / (get all events)
@events_bp.route("/", methods = ["GET"])
def get_events():
    stmt = db.select(Event)
    events_list = db.session.scalars(stmt)
    data = events_schema.dump(events_list)
    if data:
        return jsonify(data), 200
    else:
        return {"message": "No events found. Please add a event to get started."}, 404

# GET /id (get one event by id)
@events_bp.route("/<int:event_id>", methods = ["GET"])
def get_one_event(event_id):
    stmt = db.select(Event).where(Event.event_id == event_id)
    event = db.session.scalar(stmt)
    data = event_schema.dump(event)
    if data:
        return jsonify(data), 200
    else:
        return {"message": f"Event with id {event_id} doesn't exist."}, 404

# POST / (create a new event)
@events_bp.route("/", methods = ["POST"])
def create_a_event():
    body_data = request.get_json()
    new_event = event_schema.load(
        body_data,
        session = db.session
    )
    db.session.add(new_event)
    db.session.commit()
    return event_schema.dump(new_event), 201

# PATCH/PUT /id (update event by id)
@events_bp.route("/<int:event_id>", methods = ["PUT", "PATCH"])
def update_a_event(event_id):
    stmt = db.select(Event).where(Event.event_id == event_id)
    event = db.session.scalar(stmt)
    if not event:
        return {"message": f"Event with id {event_id} doesn't exist."}, 404
    try:
        update_event = event_schema.load(
            request.get_json(),
            instance = event,
            session = db.session,
            partial = True
        )
        db.session.commit()
        return event_schema.dump(update_event), 200
    except ValidationError as e:
        return e.messages, 400
    except IntegrityError as e:
        return {"message": "Integrity error: likely a duplicate entry or invalid Foreign Key."}, 409
    except DataError as e:
        return {"message": "Data error: e.orig.diag.message_primary}."}, 400
    
# DELETE /id (delete event by id)
@events_bp.route("/<int:event_id>", methods = ["DELETE"])
def delete_a_event(event_id):
    stmt = db.select(Event).where(Event.event_id == event_id)
    event = db.session.scalar(stmt)
    
    for show in event.shows:   # Join events to bookings via shows
        for booking in show.bookings:   # If an event is cancelled, mark all bookings as CANCELLED
            booking.booking_status = "CANCELLED"

    db.session.commit()
    return {"message": f"Event id {event_id} and their bookings have been cancelled"}, 200