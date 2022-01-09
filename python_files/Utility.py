import os
import re

import cartopy.crs as ccrs
import matplotlib.pyplot as plt
import networkx as nx
import requests
import unicodedata2

re_coord = re.compile(r'(?P<longitude>-?\d+\.\d+) (?P<latitude>-?\d+\.\d+)')
url = 'https://query.wikidata.org/bigdata/namespace/wdq/sparql'
ar_dir_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "..", "data", "airline_routes_data" + os.sep)
sc_dir_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "..", "data", "sister_cities_data" + os.sep)


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


def save_plot(graph, path, graph_name="", num_nodes="", num_edges=""):
    """
    This method plots the graph passed as argument and saves the image in the given path.
    :param graph: Graph to plot
    :param path: Path where to store the image
    :param graph_name: Name of the graph (useful for plotting a description)
    :param num_nodes: Number of graph nodes (useful for plotting a description)
    :param num_edges: Number of graph edges (useful for plotting a description)
    """
    positions = {}
    for node, d in graph.nodes(data=True):
        positions[node] = (d['lon'], d['lat'])

    fig = plt.figure()
    ax = fig.add_axes([0, 0, 1, 1], projection=ccrs.PlateCarree())

    os.environ["CARTOPY_USER_BACKGROUNDS"] = os.path.join(os.path.dirname(os.path.realpath(__file__)), "..",
                                                          "data" + os.sep)
    ax.background_img(name='ETOPO', resolution='high')

    nx.draw_networkx_nodes(graph, positions, node_size=0.01, nodelist=graph.nodes, node_shape="o", linewidths=0,
                           node_color="black", alpha=0.9)
    nx.draw_networkx_edges(graph, positions, edgelist=graph.edges, width=0.01, edge_color="red")

    ax.axis('tight')
    ax.axis('off')
    fig.set_size_inches(2.4, 1.35)
    ax.text(0.01, 0.01, str(graph_name) + "\nn° nodes: " + str(num_nodes) + "\nn° edges: " + str(num_edges),
            verticalalignment='bottom', horizontalalignment='left',
            transform=ax.transAxes,
            color='black', fontsize=1.5)
    plt.savefig(path, format='png', dpi=1200)
    plt.show()
