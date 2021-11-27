import os
from pathlib import Path
import networkx as nx
from tqdm import tqdm
import csv
import Utility

wd_path = os.path.abspath(os.path.join(Path().resolve(), '..'))


def build_graph():
    # All the nodes will be stored in "cities", all the edges in "edges" and in positions the coordinates
    # associated to each city.
    edges = []
    cities = {}

    file = open(wd_path + "/data/airline_routes_data/routes_complete.csv", encoding="utf-8")
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

    nx.write_gexf(G, '../data/airline_routes_data/routes.gexf')
    return G


def main():
    G = build_graph()
    Utility.plot(G, 'airline_routes_data/complete_routes_plot.png')


if __name__ == "__main__":
    main()
