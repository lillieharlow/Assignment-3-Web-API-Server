from main import db
from models.user import User

# TDD for API endpoints on user.py:

# GET /users
# Expected response: 200 OK and a list
def test_get_users(client):
    response = client.get('/users/')
    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data, list) # Test passes when if/else is commented out in user_controller.py (404 throws it off)

# POST /users
# Expected response: 201 OK, JSON response
def test_create_user_success(client):
    new_user = {
        "first_name": "John",
        "last_name": "Smith",
        "email": "john@email.com",
        "phone_number": "0324555444"
    }
    response = client.post('/users/', json = new_user)
    assert response.status_code == 201
    user = response.get_json()
    assert 'user_id' in user
    assert user['email'] == 'john@email.com'

# PATCH/PUT /users/<user_id>
# Expected response: 200 OK, JSON response
def test_update_user_success(client):
    user = User(
        first_name = "Test",
        last_name = "User",
        email = "test@mail.com",
        phone_number = "0123456789"
    )
    db.session.add(user)
    db.session.commit()
    user_id = user.user_id

    update_data = {"first_name": "Passed"}
    response = client.patch(f"/users/{user_id}", json = update_data)
    assert response.status_code == 200
    updated_user = response.get_json()
    assert updated_user["first_name"] == "Passed"