import networkx as nx
from networkx import is_connected
from tqdm import tqdm

from python_files.Utility import sc_dir_path, ar_dir_path


def extrapolate_country_edges(graph):
    """
    Extrapolates city edges from a graph and create a dictionary in the form
    {('source_node', 'dest_node'): [x], ...} where x is the weight of the edge
    :return: instance of a dictionary and the list of all nations found in the graph
    """
    nations = []
    x = graph.nodes(data='country')
    for instance in x:
        nations.append(instance[1])
    nations = list(dict.fromkeys(nations))

    edges = {}
    weight = 1
    for edge in graph.edges():
        source_node = graph.nodes[edge[0]]
        dest_node = graph.nodes[edge[1]]
        if source_node["country"] != dest_node["country"]:
            edge = (source_node["country"], dest_node["country"])
            if not (edge in edges):
                edges[edge] = [weight]
            else:
                edges[edge][0] += 1
    return edges, nations


def build_nations_graph(edge_dict, nations):
    """
    Takes an edge dictionary in the form {('source_node', 'dest_node'): [x], ...}
    where x is the weight of the edge and builds a graph with it.
    :param edge_dict: instance of a dictionary
    :param nations: list of nations that are the graph nodes
    :return: instance of a graph
    """
    G = nx.Graph()
    for nation in nations:
        G.add_node(nation)
    for instance in tqdm(edge_dict):
        G.add_edge(instance[0], instance[1], weight=edge_dict[instance][0])
    return G


def main():
    # Builds nations graph for sister cities
    r_sc = nx.readwrite.read_gexf(sc_dir_path + 'reduced_sister_cities.gexf')
    edge_dict, nations = extrapolate_country_edges(r_sc)
    G = build_nations_graph(edge_dict, nations)
    print("Country SC graph connected: ", is_connected(G))
    print("N° of nodes in Country SC graph: ", len(G.nodes))
    nx.write_gexf(G, sc_dir_path + 'reduced_nations_sister_cities.gexf')

    # Builds nations graph for airline routes
    r_ar = nx.readwrite.read_gexf(ar_dir_path + 'reduced_routes.gexf')
    edge_dict, nations = extrapolate_country_edges(r_ar)
    G = build_nations_graph(edge_dict, nations)
    print("Country AR graph connected: ", is_connected(G))
    print("N° of nodes in Country AR graph: ", len(G.nodes))
    nx.write_gexf(G, ar_dir_path + 'reduced_nations_routes.gexf')


if __name__ == "__main__":
    main()
