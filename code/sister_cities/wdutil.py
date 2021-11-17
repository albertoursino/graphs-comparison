import re
import requests


re_coord = re.compile(r'(?P<longitude>-?\d+\.\d+) (?P<latitude>-?\d+\.\d+)')
url = 'https://query.wikidata.org/bigdata/namespace/wdq/sparql'


def coord(point):
    match = re.search(re_coord, point)
    if match:
        return float(match.group('longitude')), float(match.group('latitude'))


def request(query):
    return requests.get(url, params={'query': query, 'format': 'json'}).json()


def test_coord():
    assert (-73.94, 40.67) == coord('Point(-73.94 40.67)')

