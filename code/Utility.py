import re
import requests
import csv
import os
import pathlib

re_coord = re.compile(r'(?P<longitude>-?\d+\.\d+) (?P<latitude>-?\d+\.\d+)')
url = 'https://query.wikidata.org/bigdata/namespace/wdq/sparql'
wd_path = os.path.abspath(os.path.join(pathlib.Path().resolve(), '..'))


def coord(point):
    match = re.search(re_coord, point)
    if match:
        return float(match.group('longitude')), float(match.group('latitude'))


def request(query):
    return requests.get(url, params={'query': query, 'format': 'json'}).json()


def test_coord():
    assert (-73.94, 40.67) == coord('Point(-73.94 40.67)')


def create_routes_complete():
    # TODO: Function which (re)creates routes_complete.csv from airport.dat and routes.dat
    pass


def read_routes():
    """
    Reads the file "routes_complete.csv"
    :return: matrix with all "routes_complete.csv" entries
    """
    rows = []
    file = open(wd_path + "/data/airline_routes_data/routes_complete.csv", encoding="utf-8")
    csv_reader = csv.reader(file)
    for row in csv_reader:
        rows.append(row)
    return rows
