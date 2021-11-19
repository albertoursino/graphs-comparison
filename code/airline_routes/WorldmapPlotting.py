import cartopy.crs as ccrs
import matplotlib.pyplot as plt
import networkx as nx
from tqdm import tqdm

import Utility


def main():
    # All the nodes will be stored in "cities", all the edges in "edges" and in positions the coordinates
    # associated to each city.
    cities = []
    edges = []
    positions = {}
    routes = Utility.read_routes()
    # It iterates only the first 150 routes in order to avoid entries with "N/D" values
    for entry in tqdm(routes[0:150], desc="Creating airline routes graph"):
        cities.append(entry[4])
        cities.append(entry[9])
        edges.append((entry[4], entry[9]))
        positions[entry[4]] = (float(entry[6]), float(entry[5]))
        positions[entry[9]] = (float(entry[11]), float(entry[10]))

    G = nx.Graph()
    G.add_nodes_from(cities)
    for edge in tqdm(edges, desc="Weighting edges"):
        # Each edge will be weighted based on how many times the edge shows up.
        if G.has_edge(edge[0], edge[1]):
            G[edge[0]][edge[1]]['weight'] += 1
        else:
            G.add_edge(edge[0], edge[1], weight=1)

    ax = plt.axes(projection=ccrs.PlateCarree())
    ax.stock_img()
    nx.draw_networkx_nodes(G, positions, node_size=2, nodelist=cities)
    nx.draw_networkx_edges(G, positions, edgelist=edges)
    plt.show()

    # TODO: the graph needs to be restyled, because now it's painful to watch
    # TODO: we need to decide how to manage the pathological entries of routes_complete.csv


if __name__ == "__main__":
    main()
