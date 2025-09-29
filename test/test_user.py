"""TDD for API endpoints:
    1. Comment out other controller imports and Blueprints in main.py
    3. Write individual tests for HTTP requests (GET, POST, PATCH/PUT, DELETE)
    4. Run test
    5. It fails
    6. Write code to make it pass"""

# GET /users
# Expected response: 200 OK and a list
def test_get_users(client):
    response = client.get('/users/')
    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data, list)

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
    assert 'id' in user
    assert user['email'] == "john@email.com"

# Expected response: Returns an empty list when no users exist
def test_get_users_returns_empty_list(client):
    response = client.get('/users/')
    assert response.status_code == 404
    data = response.get_json()
    assert data == {"message": "No users found. Please add a user to get started."}