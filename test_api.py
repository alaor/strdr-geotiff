import requests
import os


def test_sources_exists():
    assert os.path.isfile("./sources/analytic.tif")


def test_endpoint_vegetation_cover():
    url = 'http://localhost:5000/vegetation-cover'
    resp = requests.get(url)
    assert resp.status_code == 200
    assert resp.json()["area"] == 1267031.25
    assert resp.json()["centroid"]["type"] == "Point"
