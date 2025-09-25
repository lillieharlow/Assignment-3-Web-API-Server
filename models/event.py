from init import db

class Event(db.Model):
    # Event  model represents event table.
    __tablename__ = "events"

    event_id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100), nullable = False, unique = True)
    description = db.Column(db.Text)
    
    organiser_id = db.Column(
        db.Integer,
        db.ForeignKey("organisers.organier_id", ondelete = "SET NULL"),
        nullable = True
        )
    organiser = db.relationship("Organiser", back_populates = "events")