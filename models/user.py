from init import db
from sqlalchemy import CheckConstraint

class User(db.Model):
    __tablename__ = "users"
    __table_args__ = (
        CheckConstraint("length(phone_number) = 10", name='check_phone_number_length'), # comma needed to make it a tuple
    )
    user_id = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.String(20), nullable = False)
    last_name = db.Column(db.String(30), nullable = False)
    email = db.Column(db.String(100), nullable = False, unique = True)
    phone_number = db.Column(db.String(10), nullable = False, unique = True)

    # one user can have many bookings
    bookings = db.relationship("Booking", back_populates = "user", cascade = "all, delete-orphan")