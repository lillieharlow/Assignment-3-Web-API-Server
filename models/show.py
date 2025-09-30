from init import db
from datetime import datetime

class Show(db.Model):
    __tablename__ = "shows"

    show_id = db.Column(db.Integer, primary_key = True)
    date_time = db.Column(db.DateTime, nullable = False, unique = True)
    event_id = db.Column(db.Integer, db.ForeignKey("events.event_id"), nullable = False)
    venue_id = db.Column(db.Integer, db.ForeignKey("venues.venue_id", ondelete = "SET NULL"), nullable = True)
    
    # one show is one and only one event
    event = db.relationship("Event", back_populates = "shows")
    # one show can be held at one and only one venue
    venue = db.relationship("Venue", back_populates = "shows")
    # one show can have many bookings
    bookings = db.relationship("Booking", back_populates = "show")
