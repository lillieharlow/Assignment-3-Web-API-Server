import enum
from sqlalchemy.types import Enum
from sqlalchemy.orm import Session
from init import db

# Define set values for booking_status column of booking table.
class BookingStatus(enum.Enum):
    CONFIRMED = "Confirmed"
    CANCELLED = "Cancelled"
    IN_PROGRESS = "In Progress"
    PENDING = "Pending"

# 

class Booking(db.Model):
    # Booking model represents booking table.
    __tablename__ = "bookings"

    booking_id = db.Column(db.Integer, primary_key = True)
    booking_date = db.Column(db.DateTime, nullable = False)
    booking_status = db.Column(Enum(BookingStatus), nullable = False)

    # ========== Foreign Key 1 ==========
    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.user_id", ondelete = "CASCADE"),
        nullable = False
    )
    # singular attribute because one booking has one and only one user
    user = db.relationship("User", back_populates = "bookings")

    # ========== Foreign Key 2 ==========
    show_id = db.Column(
        db.Integer,
        db.ForeignKey("shows.show_id"),
        nullable = True
    )
    # singular attribute because one booking is for one and only one show
    show = db.relationship("Show", back_populates = "bookings")