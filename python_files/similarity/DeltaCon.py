import networkx as nx
from math import sqrt

import numpy as np
from networkx.linalg.graphmatrix import adjacency_matrix


def deltacon(graph1, graph2):
    """
    Method description here: https://arxiv.org/abs/1304.4657
    :return: a similarity score between graph1 and graph2
    """
    nodes1_list_sorted = sorted(list(graph1.nodes))
    nodes2_list_sorted = sorted(list(graph2.nodes))
    # The two graphs node sets must be the same
    if nodes1_list_sorted != nodes2_list_sorted:
        node_list = list(set(nodes1_list_sorted) | set(nodes2_list_sorted))
    else:
        node_list = nodes1_list_sorted

    I = np.identity(len(node_list))
    A1 = adjacency_matrix(graph1, nodelist=node_list)
    A2 = adjacency_matrix(graph2, nodelist=node_list)

    degrees_graph1 = [val for (node, val) in graph1.degree()]
    degrees_graph2 = [val for (node, val) in graph2.degree()]

    D1 = np.diag(degrees_graph1)
    D2 = np.diag(degrees_graph2)

    epsilon1 = 1 / (1 + D1.max())
    epsilon2 = 1 / (1 + D2.max())

    S1 = pow(I + pow(epsilon1, 2) * D1 - epsilon1 * A1, -1)
    S2 = pow(I + pow(epsilon2, 2) * D2 - epsilon2 * A2, -1)

    d = 0
    for i in range(len(node_list)):
        for j in range(len(node_list)):
            d += pow(sqrt(abs(S1[i, j])) - sqrt(abs(S2[i, j])), 2)
    d = sqrt(d)

    return 1 / (1 + d)


s_cities_red = nx.readwrite.read_gexf(
    r'C:\Users\letto\Desktop\IntellIj Local Files\Learning-from-Network-Project\data\sister_cities_data\reduced_sister_cities.gexf')
routes_red = nx.readwrite.read_gexf(
    r'C:\Users\letto\Desktop\IntellIj Local Files\Learning-from-Network-Project\data\airline_routes_data\reduced_routes.gexf')
print("Graph similarity by DeltaCon = ", deltacon(s_cities_red, routes_red))
