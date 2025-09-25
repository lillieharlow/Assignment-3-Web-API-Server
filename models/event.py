from init import db

class Event(db.Model):
    # Event model represents event table.
    __tablename__ = "events"

    event_id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100), nullable = False, unique = True)
    description = db.Column(db.Text)
    
    # ========== Foreign Key ==========
    organiser_id = db.Column(
        db.Integer,
        db.ForeignKey("organisers.organiser_id", ondelete = "SET NULL"),
        nullable = True
        )
    # singular attribute because an event has one and only one organiser
    organiser = db.relationship("Organiser", back_populates = "events")

    # plural attribute because an event can have many shows
    shows = db.relationship("Show", back_populates = "event", cascade = "all, delete-orphan")