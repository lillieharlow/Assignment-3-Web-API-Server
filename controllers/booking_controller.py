from flask import Blueprint, jsonify, request
from sqlalchemy.exc import IntegrityError
from psycopg2 import errors

from init import db
from models.booking import Booking
from schemas.schemas import booking_schema, bookings_schema

bookings_bp = Blueprint("bookings", __name__, url_prefix = "/bookings")



# Note: Make function to show CANCELLED on bookings if the show is deleted.

"""def delete_show_and_cancel_bookings(show_id):
    show = session.query(Show).get(show_id)
    if show:
        for booking in show.bookings:
            booking.booking_status = BookingStatus.CANCELLED
        session.commit()
        session.delete(show)
        session.commit()"""