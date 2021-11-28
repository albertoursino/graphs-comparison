import re
import requests
import csv
import os
import unicodedata2
import matplotlib.pyplot as plt
import networkx as nx
import cartopy.crs as ccrs

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


def create_routes_complete():
    # TODO: Function which (re)creates routes_complete.csv from airport.dat and routes.dat
    pass


def read_routes():
    """
    Reads the file "routes_complete.csv"
    :return: matrix with all "routes_complete.csv" entries
    """
    rows = []
    file = open("../data/airline_routes_data/routes_complete.csv", encoding="utf-8")
    csv_reader = csv.reader(file)
    for row in csv_reader:
        rows.append(row)
    return rows


def remove_diacritics(string):
    """
    Substitutes diacritics of the input string with normalized Unicode characters
    :param string: the string to be normalized
    :return: normalized string
    """
    nfkd_form = unicodedata2.normalize('NFKD', string)
    return u"".join([c for c in nfkd_form if not unicodedata2.combining(c)])


def save_plot(graph, save_image_path):
    """
    # TODO
    :param graph:
    :param save_image_path:
    :return:
    """
    positions = {}
    for node, d in graph.nodes(data=True):
        positions[node] = (d['lon'], d['lat'])

    fig = plt.figure()
    ax = fig.add_axes([0, 0, 1, 1], projection=ccrs.PlateCarree())

    os.environ["CARTOPY_USER_BACKGROUNDS"] = "../data"
    ax.background_img(name='ETOPO', resolution='high')

    nx.draw_networkx_nodes(graph, positions, node_size=0.03, nodelist=graph.nodes, node_shape="o", linewidths=0,
                           node_color="black", alpha=0.9)
    nx.draw_networkx_edges(graph, positions, edgelist=graph.edges, width=0.06, edge_color="red")

    plt.savefig('../data/' + save_image_path, format='png', dpi=800)
    plt.show()
