from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, auto_field
from marshmallow import fields, ValidationError, validate, validates

from models.user import User
from models.organiser import Organiser
from models.venue import Venue
from models.event import Event
from models.show import Show
from models.booking import Booking

# ========== User Schema ==========
class UserSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_instance = True
        include_relationships = True
        fields = ("user_id", "first_name", "last_name", "email", "phone_number", "bookings")
    
    bookings = fields.List(fields.Nested("BookingSchema", exclude = ("user", "user_id")))
    
user_schema = UserSchema()
users_schema = UserSchema(many = True)

# ========== Organiser Schema ==========
class OrganiserSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Organiser
        load_instance = True
        incdue_relationships = True
        fields = ("organiser_id", "full_name", "email", "phone_number", "events")

    events = fields.List(fields.Nested("EventSchema", exclude = ("organiser", "organiser_id")))

organiser_schema = OrganiserSchema()
organisers_schema = OrganiserSchema(many = True)

# ========== Venue Schema ==========
class VenueSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Venue
        load_instance = True
        include_relationships = True
        fields = ("venue_id", "name", "location", "shows")
    
    shows = fields.List(fields.Nested("ShowSchema", exclude = ("venue", "show_id")))

venue_schema = VenueSchema()
venues_schema = VenueSchema(many = True)

# ========== Event Schema ==========
class EventSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Event
        load_instance = True
        include_fk = True
        include_relationships = True
        fields = ("event_id", "title", "description", "duration_hours", "organiser_id", "show", "organiser")
    
    shows = fields.List(fields.Nested("ShowSchema", exclude = ("show_id", "event")))
    organiser = fields.Nested("OrganiserSchema", dump_only = True, only = ("full_name",))

event_schema = EventSchema()
events_schema = EventSchema(many = True)

# ========== Show Schema ==========
class ShowSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Show
        load_instance = True
        include_fk = True
        include_relationships = True
        fields = ("show_id", "date_time", "event_id", "venue_id", "bookings", "event", "venue")
    
    bookings = fields.List(fields.Nested("BookingSchema", exclude = ("show", "show_id")))
    event = fields.Nested("EventSchema", dump_only = True, only = ("title",))
    venue = fields.Nested("VenueSchema", dump_only = True, only = ("name", "location"))

show_schema = ShowSchema()
shows_schema = ShowSchema(many = True)

# ========== Booking Schema ==========
class BookingSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Booking
        load_instance = True
        include_fk = True
        include_relationships = True
        fields = ("booking_id", "booking_date", "booking_status","user_id", "show_id", "user", "show")
    
    user = fields.Nested("UserSchema", dump_only = True, only = ("first_name", "last_name"))
    show = fields.Nested("ShowSchema", dump_only = True, only = ("date_time", "event", "venue"))

booking_schema = BookingSchema()
bookings_schema = BookingSchema(many = True)