from init import db

class Venue(db.Model):
    # Venue  model represents venue table.
    __tablename__ = "venues"

    venue_id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(30), nullable = False, unqiue = True)
    location = db.Column(db.String(100), nullable = False)