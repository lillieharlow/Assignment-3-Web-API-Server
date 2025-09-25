from init import db
from sqlalchemy import CheckConstraint

class Organiser(db.Model):
    """
    Organiser  model represents organiser table.

    Integrity check:
    Ensure phone number is exactly 10 digits long,
    using length & digit-only pattern check.
    """
    __tablename__ = "organisers"

    organiser_id = db.Column(db.Integer, primary_key = True)
    full_name = db.Column(db.String(50), nullable = False)
    email = db.Column(db.String(100), nullable = False, unique = True)
    phone_number = db.Column(db.String(10), nullable = False, unique = True)

    events = db.relationship("Event", back_populates = "organiser")

    __table_args__ = (
        CheckConstraint(
            "length(phone_number) = 10 AND phone_number GLOB '[0-9]*'",
            name='check_phone_number_length'
            )
    )