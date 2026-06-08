from urllib.parse import quote
from src.app import activities


def test_signup_success(client):
    # Arrange
    activity = "Chess Club"
    email = "newstudent_test@example.com"
    assert email not in activities[activity]["participants"]

    # Act
    resp = client.post(f"/activities/{quote(activity)}/signup", params={"email": email})

    # Assert
    assert resp.status_code == 200
    assert email in activities[activity]["participants"]


def test_signup_duplicate(client):
    # Arrange
    activity = "Chess Club"
    existing = activities[activity]["participants"][0]

    # Act
    resp = client.post(f"/activities/{quote(activity)}/signup", params={"email": existing})

    # Assert
    assert resp.status_code == 400


def test_signup_nonexistent(client):
    # Arrange
    activity = "Nonexistent Club"
    email = "someone@mergington.edu"

    # Act
    resp = client.post(f"/activities/{quote(activity)}/signup", params={"email": email})

    # Assert
    assert resp.status_code == 404
