from init import db

class Show(db.Model):
    # Show model represents show table.
    __tablename__ = "shows"

    show_id = db.Column(db.Integer, primary_key = True)
    duration_hours = db.Column(db.Float)
    date_time = db.Column(db.DateTime, nullable = False, unique = True)

    # ========== Foreign Key 1 ==========
    event_id = db.Column(
        db.Integer,
        db.ForeignKey("events.event_id", ondelete = "CASCADE"),
        nullable = False
    )
    # singular attribute because a show is one and only one event
    event = db.relationship("Event", back_populates = "shows")

    # ========== Foreign Key 2 ==========
    venue_id = db.Column(
        db.Integer,
        db.ForeignKey("venues.venue_id", ondelete = "SET NULL"),
        nullable = True
    )
    #singular attribute because a show can be at one and only one venue
    venue = db.relationship("Venue", back_populates = "shows")

    # plural attribute because one show can have many bookings
    bookings = db.relationship("Booking", back_populates = "show")