import re
import requests
import os
import sys
import unicodedata2
import matplotlib.pyplot as plt
import networkx as nx
import cartopy.crs as ccrs

re_coord = re.compile(r'(?P<longitude>-?\d+\.\d+) (?P<latitude>-?\d+\.\d+)')
url = 'https://query.wikidata.org/bigdata/namespace/wdq/sparql'
ar_dir_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "..", "data", "airline_routes_data" + os.sep)
ss_dir_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "..", "data", "sister_cities_data" + os.sep)


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


def normalize(string: str):
    """
    Substitutes diacritics of the input string with normalized Unicode characters
    :param string: the string to be normalized
    :return: normalized string
    """

    nfkd_form = unicodedata2.normalize('NFKD', string.replace("-", " "))
    return u"".join([c for c in nfkd_form if not unicodedata2.combining(c)]).lower()


def save_plot(graph, path):
    """
    # TODO
    :param graph:
    :param path:
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

    plt.savefig(path, format='png', dpi=800)
    plt.show()
