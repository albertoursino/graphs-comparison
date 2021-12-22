import networkx as nx
from math import sqrt
from python_files.Utility import ss_dir_path, ar_dir_path

import numpy as np
from networkx.linalg.graphmatrix import adjacency_matrix


def deltacon(graph1, graph2):
    """
    Method description here: https://arxiv.org/abs/1304.4657
    :return: a similarity score between graph1 and graph2
    """
    set1 = set(graph1.nodes)
    set2 = set(graph2.nodes)

    graph2.add_nodes_from(set1 - set2)
    graph1.add_nodes_from(set2 - set1)

    I = np.identity(graph1.number_of_nodes())
    A1 = adjacency_matrix(graph1)
    A2 = adjacency_matrix(graph2)

    degrees_graph1 = [val for (node, val) in graph1.degree()]
    degrees_graph2 = [val for (node, val) in graph2.degree()]

    D1 = np.diag(degrees_graph1)
    D2 = np.diag(degrees_graph2)

    epsilon1 = 1 / (1 + D1.max())
    epsilon2 = 1 / (1 + D2.max())

    S1 = pow(I + pow(epsilon1, 2) * D1 - epsilon1 * A1, -1)
    S2 = pow(I + pow(epsilon2, 2) * D2 - epsilon2 * A2, -1)

    d = 0
    for i in range(graph1.number_of_nodes()):
        for j in range(graph1.number_of_nodes()):
            d += pow(sqrt(abs(S1[i, j])) - sqrt(abs(S2[i, j])), 2)
    d = sqrt(d)

    return 1 / (1 + d)


s_cities_red = nx.readwrite.read_gexf(
    ss_dir_path + 'reduced_nations_sister_cities.gexf')
routes_red = nx.readwrite.read_gexf(
    ar_dir_path + 'reduced_nations_routes.gexf')
print("Graph similarity by DeltaCon = ", deltacon(s_cities_red, routes_red))
