import requests
import pytest


def test_find_neighbor_200(url_prefix):
    user = requests.post(
        f"{url_prefix}/user",
        json={
            "name": "Mark",
            "coord_x": "61.465245",
            "coord_y": "32.670114"
        },
        headers={"Content-Type": "application/json"}
    )

    user = requests.get(f"{url_prefix}/neighbors/61.465245,34.670114")

    assert user.status_code == 200
    assert user.json() != []



def test_find_neighbor_wrong_params_400(url_prefix):
    user = requests.post(
        f"{url_prefix}/user",
        json={
            "name": "Mark",
            "coord_x": "61.465245",
            "coord_y": "32.670114"
        },
        headers={"Content-Type": "application/json"}
    )

    user = requests.get(f"{url_prefix}/neighbors/61.46524534.670114")

    assert user.status_code == 400


@pytest.mark.parametrize("coords", [
    'abc,34.670114',
    '61.465245,abc',
    '92,34.670114',
    '-92,34.670114',
    '61.465245,182',
    '61.465245,-182',
])
def test_find_neighbor_invalid_coords_422(url_prefix, coords):
    user = requests.post(
        f"{url_prefix}/user",
        json={
            "name": "Mark",
            "coord_x": "61.465245",
            "coord_y": "32.670114"
        },
        headers={"Content-Type": "application/json"}
    )

    user = requests.get(f"{url_prefix}/neighbors/{coords}")

    assert user.status_code == 422


def test_find_neighbor_check_order_200(url_prefix):
    user1 = requests.post(
        f"{url_prefix}/user",
        json={
            "name": "Novgorod",
            "coord_x": "58.538835",
            "coord_y": "31.257455"
        },
        headers={"Content-Type": "application/json"}
    )

    user2 = requests.post(
        f"{url_prefix}/user",
        json={
            "name": "Moscow",
            "coord_x": "55.757333",
            "coord_y": "37.613386"
        },
        headers={"Content-Type": "application/json"}
    )

    user3 = requests.post(
        f"{url_prefix}/user",
        json={
            "name": "SPb1",
            "coord_x": "59.958301",
            "coord_y": "30.302693"
        },
        headers={"Content-Type": "application/json"}
    )

    user4 = requests.post(
        f"{url_prefix}/user",
        json={
            "name": "SPb2",
            "coord_x": "59.961886",
            "coord_y": "30.308335"
        },
        headers={"Content-Type": "application/json"}
    )

    user = requests.get(f"{url_prefix}/neighbors/59.965389,30.311916/?limit=3")

    assert user.status_code == 200
    assert len(user.json()) == 3
    assert user.json()[0]['name'] == 'SPb2'
    assert user.json()[1]['name'] == 'SPb1'
    assert user.json()[2]['name'] == 'Novgorod'
