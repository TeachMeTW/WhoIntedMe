import pytest


@pytest.mark.parametrize(
    "email,first_name,password",
    [
        ("test1@example.com", "Test1", "password123"),
        ("test2@example.com", "Test2", "password124"),
    ],
)
def test_add_user(test_client, email, password, first_name):
    # Add user
    response = test_client.post(
        "/api/user",
        json={"email": email, "password": password, "first_name": first_name},
    )
    assert response.status_code == 201
