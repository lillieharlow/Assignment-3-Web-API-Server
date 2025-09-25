from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow import fields

from models.user import User

# User Schema: linked to models.user, returns model instance when loading data
class UserSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_instance = True

# Schema instances for single and multiple User objects
user_schema = UserSchema()
users_schema = UserSchema(many = True)

