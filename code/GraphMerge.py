from tqdm import tqdm
import SisterCities
import AirlineRoutes
import Utility
import networkx as nx


def main():
    try:
        s_cities_graph = nx.readwrite.read_gexf('../data/sister_cities_data/sister_cities.gexf')
    except FileNotFoundError:
        s_cities_graph = SisterCities.build_graph()

    try:
        routes_graph = nx.readwrite.read_gexf('../data/airline_routes_data/routes.gexf')
    except FileNotFoundError:
        routes_graph = AirlineRoutes.build_graph()

    remove_uncommon_nodes(s_cities_graph, routes_graph, "sister_cities_data/reduced_sister_cities.gexf")
    print("Sister Cities Graph #nodes:", len(s_cities_graph.nodes), " #edges: ", len(s_cities_graph.edges))
    remove_uncommon_nodes(routes_graph, s_cities_graph, "airline_routes_data/reduced_routes.gexf")
    print("Routes Graph #nodes:", len(routes_graph.nodes), " #edges: ", len(routes_graph.edges))

    # Plotting and saving the reduced graphs
    Utility.save_plot(nx.readwrite.read_gexf('../data/airline_routes_data/reduced_routes.gexf'),
                      "airline_routes_data/reduced_routes_plot.png")
    Utility.save_plot(nx.readwrite.read_gexf('../data/sister_cities_data/reduced_sister_cities.gexf'),
                      "sister_cities_data/reduced_sister_cities_plot.png")


def remove_uncommon_nodes(graph_1, graph_2, file_name_path):
    """
    # TODO
    :param graph_1:
    :param graph_2:
    :param file_name_path:
    :return:
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
    nx.write_gexf(graph_1, '../data/' + file_name_path)
    return graph_1


if __name__ == "__main__":
    main()
