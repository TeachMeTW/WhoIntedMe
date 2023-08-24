import pytest
from back.database import db
from back.models import User


# Parametrized test for adding and updating lol_username
@pytest.mark.parametrize(
    "userID, status, message",
    [
        (123, 200, "User deleted successfully"),
        (999, 404, "User not found"),
    ],
)
def test_delete_user(test_client, userID, status, message):
    with test_client.application.app_context():
        user = User(id=123)
        db.session.add(user)
        db.session.commit()
        response = test_client.delete(
            f"/api/user/{userID}",
        )
        assert response.status_code == status
        assert response.get_json().get("message") == message
