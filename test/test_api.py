import pytest


def test_people_with_id_1(api, base_url):
    from api.endpoints import People
    people = People(api, base_url)
    response = people.get(1)
    assert response.status_code == 200
    