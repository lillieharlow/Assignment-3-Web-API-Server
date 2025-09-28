import pytest
import os

from main import create_app
from init import db

"""Define pytest fixture called client.
Each test gets a new, empty database and a test client to test endpoints."""
@pytest.fixture
def client():
    os.environ['DATABASE_URI'] = "sqlite:///:memory:"
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    with app.app_context():
        db.create_all()
        yield app.test_client()
        db.session.remove()
        db.drop_all()