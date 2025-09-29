from init import db

class Venue(db.Model):
    __tablename__ = "venues"

    venue_id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(30), nullable = False, unique = True)
    location = db.Column(db.String(100), nullable = False)

    # one venue can have many shows
    shows = db.relationship("Show", back_populates = "venue")