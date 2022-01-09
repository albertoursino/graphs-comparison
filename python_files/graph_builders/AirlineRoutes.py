import networkx as nx
from tqdm import tqdm
import csv

from python_files import Utility
from python_files.Utility import ar_dir_path


def build_graph():
    """
    # This method builds the airline routes graph
    :return: an instance of the graph
    """
    # All the nodes will be stored in "cities", all the edges in "edges" and in positions the coordinates
    # associated to each city.
    edges = []
    cities = {}

    file = open(ar_dir_path + "routes_complete.csv", encoding="utf-8")
    routes = csv.reader(file)
    next(routes)  # skip header
    for entry in tqdm(routes, desc="Creating airline routes graph"):
        source_city = entry[4]
        dest_city = entry[9]
        if source_city != "#N/D" and dest_city != "#N/D":
            if source_city not in cities:
                cities[source_city] = {'lat': float(entry[5]),
                                       'lon': float(entry[6]),
                                       'country': entry[12]}
            if dest_city not in cities:
                cities[dest_city] = {'lat': float(entry[10]),
                                     'lon': float(entry[11]),
                                     'country': entry[13]}

            edges.append((source_city, dest_city))

    G = nx.Graph()

    for node, attr in cities.items():
        G.add_node(node, **attr)

    for edge in tqdm(edges, desc="Weighting edges"):
        # Each edge will be weighted based on how many times the edge shows up.
        if G.has_edge(edge[0], edge[1]):
            G[edge[0]][edge[1]]['weight'] += 1
        else:
            G.add_edge(edge[0], edge[1], weight=1)

    nx.write_gexf(G, ar_dir_path + "routes.gexf")
    return G


def main():
    G = build_graph()
    Utility.save_plot(G, ar_dir_path + 'complete_routes_plot.png', "Airline Routes Graph", len(G.nodes), len(G.edges))


if __name__ == "__main__":
    main()
