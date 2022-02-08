from tqdm import tqdm
import SisterCities
import AirlineRoutes
from .. import Utility
import networkx as nx
from ..Utility import sc_dir_path, ar_dir_path


def main():
    try:
        s_cities_graph = nx.readwrite.read_gexf(sc_dir_path + 'sister_cities.gexf')
    except FileNotFoundError:
        s_cities_graph = SisterCities.build_graph()

    try:
        routes_graph = nx.readwrite.read_gexf(ar_dir_path + 'routes.gexf')
    except FileNotFoundError:
        routes_graph = AirlineRoutes.build_graph()

    reduced_routes_graph = nx.Graph()
    map_rs = {}

    for s_city, s_attrs in s_cities_graph.copy().nodes(True):
        found = False
        for r_city, r_attrs in routes_graph.nodes(True):
            if (Utility.normalize(s_attrs['label']) == Utility.normalize(r_city)) and \
                    (s_attrs['country'].lower() == r_attrs['country'].lower()):
                reduced_routes_graph.add_node(s_city, **s_attrs)
                map_rs[r_city] = s_city
                found = True
                break
        if not found:
            s_cities_graph.remove_node(s_city)

    # s_cities_graph is now reduced
    # let's build the edges of reduced_routes_graph

    for edge in routes_graph.edges(data=True):
        try:
            node1 = map_rs[edge[0]]
            node2 = map_rs[edge[1]]
        except KeyError:
            continue
        reduced_routes_graph.add_edge(node1, node2, weight=edge[2]['weight'])

    nx.write_gexf(reduced_routes_graph, ar_dir_path + "reduced_routes.gexf")
    nx.write_gexf(s_cities_graph, sc_dir_path + "reduced_sister_cities.gexf")

    # Plotting the reduced graphs
    Utility.save_plot(reduced_routes_graph,
                      ar_dir_path + "reduced_routes_plot.png")
    Utility.save_plot(s_cities_graph,
                      sc_dir_path + "reduced_sister_cities_plot.png")


if __name__ == "__main__":
    main()
