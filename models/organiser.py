from init import db
from sqlalchemy import CheckConstraint

class Organiser(db.Model):
    __tablename__ = "organisers"
    __table_args__ = (
        CheckConstraint("length(phone_number) = 10", name='check_phone_number_length'), # comma needed to make it a tuple
    )

    organiser_id = db.Column(db.Integer, primary_key = True)
    full_name = db.Column(db.String(50), nullable = False)
    email = db.Column(db.String(100), nullable = False, unique = True)
    phone_number = db.Column(db.String(10), nullable = False, unique = True)

    # one organiser can organise many events
    events = db.relationship("Event", back_populates = "organiser")