from urllib.parse import quote
from src.app import activities


def test_unregister_success(client):
    # Arrange
    activity = "Chess Club"
    email = activities[activity]["participants"][0]

    # Act
    resp = client.post(f"/activities/{quote(activity)}/unregister", params={"email": email})

    # Assert
    assert resp.status_code == 200
    assert email not in activities[activity]["participants"]


def test_unregister_not_signed_up(client):
    # Arrange
    activity = "Chess Club"
    email = "not_signed_up@mergington.edu"

    # Act
    resp = client.post(f"/activities/{quote(activity)}/unregister", params={"email": email})

    # Assert
    assert resp.status_code == 400


def test_unregister_nonexistent(client):
    # Arrange
    activity = "Nonexistent Club"
    email = "someone@mergington.edu"

    # Act
    resp = client.post(f"/activities/{quote(activity)}/unregister", params={"email": email})

    # Assert
    assert resp.status_code == 404
