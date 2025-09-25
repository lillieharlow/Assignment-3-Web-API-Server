from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow import fields

from models.user import User
from models.organiser import Organiser

# User Schema: linked to models.user, returns model instance when loading data
class UserSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_instance = True

# Schema instances for single and multiple User objects
user_schema = UserSchema()
users_schema = UserSchema(many = True)

# Organiser Schema: linked to models.organiser, returns model instance when loading data
class OrganiserSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Organiser
        load_instance = True

# Schema instances for single and multiple Organiser objects
organiser_schema = OrganiserSchema()
organisers_schema = OrganiserSchema(many = True)