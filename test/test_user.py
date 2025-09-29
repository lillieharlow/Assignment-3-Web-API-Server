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
        "first_name":
        "last_name":
        "email":
        "phone_number":
        
    }