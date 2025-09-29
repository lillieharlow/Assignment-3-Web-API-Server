import os

from flask import Flask
from dotenv import load_dotenv

from init import db
from controllers.cli_controller import db_commands
from controllers.user_controller import users_bp
from controllers.organiser_controller import organisers_bp
from controllers.venue_controller import venues_bp
from controllers.event_controller import events_bp
from controllers.show_controller import shows_bp
from controllers.booking_controller import bookings_bp

load_dotenv()

def create_app():
    app = Flask(__name__)
    print("Flask server started.")
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DATABASE_URI")
    app.json.sort_keys = False
    db.init_app(app)
    app.register_blueprint(db_commands)
    app.register_blueprint(users_bp)
    app.register_blueprint(organisers_bp)
    app.register_blueprint(venues_bp)
    app.register_blueprint(events_bp)
    app.register_blueprint(shows_bp)
    app.register_blueprint(bookings_bp)

    return app