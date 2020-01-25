import requests


def test_assert_app_heroku_is_responding():
    url = 'https://alaor-strdr.herokuapp.com'
    resp = requests.get(url)
    assert resp.status_code == 200


def test_endpoint_heroku_vegetation_cover():
    url = 'https://alaor-strdr.herokuapp.com/vegetation-cover'
    resp = requests.get(url)
    assert resp.status_code == 200
    assert resp.json()["area"] == 1267031.25
    assert resp.json()["centroid"]["type"] == "Point"
