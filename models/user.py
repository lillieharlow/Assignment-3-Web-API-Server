from init import db
from sqlalchemy import CheckConstraint

class User(db.Model):
    """
    User  model represents user table.

    Integrity check:
    Ensure phone number is exactly 10 digits long,
    using length & digit-only pattern check.
    """
    __tablename__ = "users"

    user_id = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.String(20), nullable = False)
    last_name = db.Column(db.String(30), nullable = False)
    email = db.Column(db.String(100), nullable = False, unique = True)
    phone_number = db.Column(db.String(10), nullable = False, unique = True)

    __table_args__ = (
        CheckConstraint(
            "length(phone_number) = 10 AND phone_number GLOB '[0-9]*'",
            name='check_phone_number_length'
            ),
    )