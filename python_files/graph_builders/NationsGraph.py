import networkx as nx
import os
from python_files.Utility import sc_dir_path, ar_dir_path

def extrapolate_country_edges(graph):
    """
    Extrapolates city edges from a graph and create a dictionary in the form
    {('source_node', 'dest_node'): [x], ...} where x is the weight of the edge
    :return: instance of a dictionary
    """
    edges = {}
    weight = 1
    for instance in graph.edges():
        source_node = graph.nodes[instance[0]]
        dest_node = graph.nodes[instance[1]]
        edge = (source_node["country"], dest_node["country"])
        if not (edge in edges):
            edges[edge] = [weight]
        else:
            edges[edge][0] += 1
    return edges


def build_nations_graph(edge_dict):
    """
    Takes an edge dictionary in the form {('source_node', 'dest_node'): [x], ...}
    where x is the weight of the edge and builds a graph with it.
    :param edge_dict: instance of a dictionary
    :return: instance of a graph
    """
    G = nx.Graph()
    for instance in edge_dict:
        G.add_edge(instance[0], instance[1], weight=edge_dict[instance][0])
    return G


def main():
    # Builds nations graph for sister cities
    edge_dict = extrapolate_country_edges(
        nx.readwrite.read_gexf(sc_dir_path + 'reduced_sister_cities.gexf'))
    G = build_nations_graph(edge_dict)
    nx.write_gexf(G, sc_dir_path + 'reduced_nations_sister_cities.gexf')

    # Builds nations graph for airline routes
    edge_dict = extrapolate_country_edges(
        nx.readwrite.read_gexf(ar_dir_path + 'reduced_routes.gexf'))
    G = build_nations_graph(edge_dict)
    nx.write_gexf(G, ar_dir_path + 'reduced_nations_routes.gexf')


if __name__ == "__main__":
    main()