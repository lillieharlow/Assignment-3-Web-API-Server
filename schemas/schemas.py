from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow import fields

from models.user import User
from models.organiser import Organiser
from models.venue import Venue
from models.event import Event
from models.show import Show

# ========== User Schema ==========
class UserSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_instance = True

user_schema = UserSchema()
users_schema = UserSchema(many = True)

# ========== Organiser Schema ==========
class OrganiserSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Organiser
        load_instance = True

    events = fields.List(fields.Nested("EventSchema", exclude = ("organiser", "organiser_id")))

organiser_schema = OrganiserSchema()
organisers_schema = OrganiserSchema(many = True)

# ========== Venue Schema ==========
class VenueSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Venue
        load_instance = True
    
    shows = fields.List(fields.Nested("ShowSchema", exclude = ("venue", "show_id")))

venue_schema = VenueSchema()
venues_schema = VenueSchema(many = True)

# ========== Event Schema ==========
class EventSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Event
        load_instance = True
        include_fk = True
        fields = (
            "event_id",
            "title",
            "description",
            "organiser_id"
            )
    
    shows = fields.List(fields.Nested("ShowSchema", exclude = ("show_id", "event")))

    organiser = fields.Nested("OrganiserSchema", dump_only = True, only = ("full_name"))

event_schema = EventSchema()
events_schema = EventSchema(many = True)

# ========== Show Schema ==========
class ShowSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Show
        load_instance = True
        include_fk = True
        fields = (
            "show_id",
            "duration",
            "date_time",
            "event_id",
            "venue_id"
        )
    
    event = fields.Nested("EventSchema", dump_only = True, only = ("title"))
    venue = fields.Nested("VenueSchema", dump_only = True, only = ("name"))

show_schema = ShowSchema()
shows_schema = ShowSchema(many = True)