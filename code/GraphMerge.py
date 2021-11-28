from tqdm import tqdm
import SisterCities
import AirlineRoutes
import Utility
import networkx as nx
from Utility import ss_dir_path, ar_dir_path


def main():
    try:
        s_cities_graph = nx.readwrite.read_gexf(ss_dir_path + 'sister_cities.gexf')
    except FileNotFoundError:
        s_cities_graph = SisterCities.build_graph()

    try:
        routes_graph = nx.readwrite.read_gexf(ar_dir_path + 'routes.gexf')
    except FileNotFoundError:
        routes_graph = AirlineRoutes.build_graph()

    remove_uncommon_nodes(s_cities_graph, routes_graph, ss_dir_path + "reduced_sister_cities.gexf")
    remove_uncommon_nodes(routes_graph, s_cities_graph, ar_dir_path + "reduced_routes.gexf")

    # Plotting the reduced graphs
    Utility.save_plot(nx.readwrite.read_gexf(ar_dir_path + 'reduced_routes.gexf'),
                      ar_dir_path + "reduced_routes_plot.png")
    Utility.save_plot(nx.readwrite.read_gexf(ss_dir_path + 'reduced_sister_cities.gexf'),
                      ss_dir_path + "reduced_sister_cities_plot.png")


def remove_uncommon_nodes(graph_1, graph_2, save_path):
    """
    :param graph_1: graph to reduce
    :param graph_2: base graph
    :param save_path: path where to store the reduced graph
    """
    to_remove = []
    for i in tqdm(graph_1.nodes, desc="Removing uncommon nodes"):
        rc = graph_1.nodes[i]
        correspondence = False
        for j in graph_2.nodes:
            sc = graph_2.nodes[j]
            if (Utility.remove_diacritics(rc['label']) == Utility.remove_diacritics(sc['label'])) and \
                    (rc['country'] == sc['country']):
                correspondence = True
        if not correspondence:
            to_remove.append(i)
    graph_1.remove_nodes_from(to_remove)
    nx.write_gexf(graph_1, save_path)
    return graph_1


if __name__ == "__main__":
    main()
