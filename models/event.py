from init import db

class Event(db.Model):
    __tablename__ = "events"

    event_id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100), nullable = False, unique = True)
    description = db.Column(db.Text)
    duration_hours = db.Column(db.Float)
    organiser_id = db.Column(db.Integer, db.ForeignKey("organisers.organiser_id", ondelete = "SET NULL"), nullable = True)
    
    # one event has one and only one organiser
    organiser = db.relationship("Organiser", back_populates = "events")
    # one event can have many shows
    shows = db.relationship("Show", back_populates = "event", cascade = "all, delete-orphan")