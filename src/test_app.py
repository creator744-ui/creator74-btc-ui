import copy

import pytest
from fastapi import HTTPException

import app


@pytest.fixture(autouse=True)
def reset_activities():
    original = copy.deepcopy(app.activities)
    yield
    app.activities.clear()
    app.activities.update(copy.deepcopy(original))


def test_signup_rejects_duplicate_student(reset_activities):
    activity_name = "Gym Class"
    email = app.activities[activity_name]["participants"][0]

    with pytest.raises(HTTPException) as excinfo:
        app.signup_for_activity(activity_name, email=email)

    assert excinfo.value.status_code == 400
    assert excinfo.value.detail == "Student already signed up"


def test_signup_prevents_overbooking(reset_activities):
    activity_name = "Chess Club"
    activity = app.activities[activity_name]
    activity["participants"] = [
        f"student{i}@mergington.edu" for i in range(activity["max_participants"])
    ]

    with pytest.raises(HTTPException) as excinfo:
        app.signup_for_activity(activity_name, email="newstudent@mergington.edu")

    assert excinfo.value.status_code == 400
    assert excinfo.value.detail == "Activity is full"
