import os
import pathlib

import cartopy.crs as ccrs
import matplotlib.pyplot as plt
import networkx as nx
from tqdm import tqdm

import Utility

wd_path = os.path.abspath(os.path.join(os.path.join(pathlib.Path().resolve(), '..'), '..'))
os.environ["CARTOPY_USER_BACKGROUNDS"] = wd_path + r"\data\airline_routes_data"


def main():
    # All the nodes will be stored in "cities", all the edges in "edges" and in positions the coordinates
    # associated to each city.
    cities = []
    edges = []
    positions = {}
    routes = Utility.read_routes()
    for entry in tqdm(routes, desc="Creating airline routes graph"):
        source_city = entry[4]
        dest_city = entry[9]
        if source_city != "#N/D" and dest_city != "#N/D":
            cities.append(source_city)
            cities.append(dest_city)
            edges.append((source_city, dest_city))
            positions[source_city] = (float(entry[6]), float(entry[5]))
            positions[dest_city] = (float(entry[11]), float(entry[10]))

    G = nx.Graph()
    G.add_nodes_from(cities)
    for edge in tqdm(edges, desc="Weighting edges"):
        # Each edge will be weighted based on how many times the edge shows up.
        if G.has_edge(edge[0], edge[1]):
            G[edge[0]][edge[1]]['weight'] += 1
        else:
            G.add_edge(edge[0], edge[1], weight=1, )

    fig = plt.figure()
    ax = fig.add_axes([0, 0, 1, 1], projection=ccrs.PlateCarree())
    ax.background_img(name='BM', resolution='high')

    nx.draw_networkx_nodes(G, positions, node_size=0, nodelist=cities)
    nx.draw_networkx_edges(G, positions, edgelist=edges, width=0.005, edge_color="red")

    plt.savefig(wd_path + r'/data/airline_routes_data/plotted_graph.jpg', dpi=1000)
    plt.show()


if __name__ == "__main__":
    main()
