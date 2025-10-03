import enum

from datetime import date
from sqlalchemy.types import Enum

from init import db

# Define set values for booking_status column of booking table.
class BookingStatus(enum.Enum):
    CONFIRMED = "Confirmed"
    CANCELLED = "Cancelled"
    IN_PROGRESS = "In Progress"
    PENDING = "Pending"

class Booking(db.Model):
    __tablename__ = "bookings"
    __table_args__ = (
        db.UniqueConstraint("user_id", "show_id", name = "booking_unique_user_show"),
    )

    booking_id = db.Column(db.Integer, primary_key = True)
    booking_date = db.Column(db.Date, default = date.today, nullable = False)
    booking_status = db.Column(Enum(BookingStatus), nullable = False, default = BookingStatus.PENDING)
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"), nullable = False)
    show_id = db.Column(db.Integer, db.ForeignKey("shows.show_id"), nullable = False)

    # one booking has one and only one user
    user = db.relationship("User", back_populates = "bookings")
    # one booking is for one and only one show
    show = db.relationship("Show", back_populates = "bookings")