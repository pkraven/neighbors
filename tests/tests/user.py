import requests
import pytest


def test_create_user_201(url_prefix):
    user = requests.post(
        f"{url_prefix}/user",
        json={
            "name": "Mark",
            "coord_x": "61.465245",
            "coord_y": "32.670114"
        },
        headers={"Content-Type": "application/json"}
    )

    assert user.status_code == 201
    assert 'application/json' in user.headers['Content-Type']


@pytest.mark.parametrize("body", [
    '{"name": "Mark"}}}',
    ''
])
def test_create_user_wrong_body_400(url_prefix, body):
    user = requests.post(
        f"{url_prefix}/user",
        data=body,
        headers={"Content-Type": "application/json"}
    )

    assert user.status_code == 400


@pytest.mark.parametrize("body", [
    {},
    {
        "coord_x": "61.465245"
    },
    {
        "coord_y": "32.670114"
    },
    {
        "coord_x": "61.465245",
        "coord_y": "32.670114"
    },
    {
        "name": "Mark",
        "coord_x": "61.465245"
    },
    {
        "name": "Mark",
        "coord_y": "32.670114"
    },
    {
        "name": "Mark",
        "coord_x": "abc",
        "coord_y": "32.670114"
    },
    {
        "name": "Mark",
        "coord_x": "61.465245",
        "coord_y": "abc"
    },
    {
        "name": "Mark",
        "coord_x": "92",
        "coord_y": "32.670114"
    },
    {
        "name": "Mark",
        "coord_x": "61.465245",
        "coord_y": "182"
    },
    {
        "name": "Mark",
        "coord_x": "-92",
        "coord_y": "32.670114"
    },
    {
        "name": "Mark",
        "coord_x": "61.465245",
        "coord_y": "-182"
    },
])
def test_create_user_wrong_params_422(url_prefix, body):
    user = requests.post(
        f"{url_prefix}/user",
        json=body,
        headers={"Content-Type": "application/json"}
    )

    assert user.status_code == 422
