# TDD for API endpoints on user.py:

# GET /users
# Expected response: 200 OK and a list
def test_get_users(client):
    response = client.get('/users/')
    assert response.status_code == 200
    data = response.get_json()
    assert data == []

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

"""# PATCH/PUT /users/<user_id>
# Expected response: 200 OK, JSON response
def test_update_user_success(client):
    user_id = 1
    update_data = {
        "first_name": "Test",
        "last_name": "User",
    }
    response = client.patch(f'/users/{user_id}', json = update_data)
    assert response.status_code == 200"""
    