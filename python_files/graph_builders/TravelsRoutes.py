import networkx as nx
import geopy.distance as gpd
from python_files.Utility import ss_dir_path, ar_dir_path, normalize

def is_node_in_graph(node, node_attrs, nodes_list):
    """
    Checks if node can be found inside node_list.
    :param node: The node to search
    :param node_attrs: the dictionary of node's attributes
    :param nodes_list: list of nodes expressed as tuples (name, {attributes})
    :return: True if node is found among the nodes of node_list, False otherwise
    """
    found = False
    for node2 in nodes_list:
        if normalize(node_attrs['label']).lower() == normalize(node2[1]['label']).lower() and \
                normalize(node_attrs['country']).lower() == normalize(node2[1]['country']).lower():
            found = True
            break
    return found

def build_travels_graph(air_routes_graph, sister_cities_graph):
    ar_nodes = air_routes_graph.nodes.data()
    for city, attrs in sister_cities_graph.copy().nodes(True):
        print("Nuova ITERAZIONE con", attrs['label'])
        if not is_node_in_graph(city, attrs, ar_nodes):
            #Searching for the nearest airport city
            min_dist = float("inf")
            nearest_airport = None
            current_pos = (attrs['lat'], attrs['lon'])  #(latitude, longitude)
            for airport, attrs_airport in air_routes_graph.copy().nodes(True):
                airport_pos = (attrs_airport['lat'], attrs_airport['lon'])
                #Computing distances considering wgs84 model
                dist = gpd.distance(current_pos, airport_pos).km
                if dist < min_dist:
                    min_dist = dist
                    nearest_airport = airport
            air_routes_graph.add_node(city, **attrs)
            air_routes_graph.add_edge(city, nearest_airport, weight = 1)
            print("nodo aggiunto")
    nx.write_gexf(air_routes_graph, ar_dir_path + "travels_routes.gexf")
    #nx.write_gexf(air_routes_graph,
    #              r'C:\Users\MARANGONI\IdeaProjects\ComparisonBetweenNetworks\data\airline_routes_data\travels_routes.gexf')




#sister_cities_graph = nx.readwrite.read_gexf(
#    r'C:\Users\MARANGONI\IdeaProjects\ComparisonBetweenNetworks\data\sister_cities_data\sister_cities.gexf')
#air_routes_graph = nx.readwrite.read_gexf(
#    r'C:\Users\MARANGONI\IdeaProjects\ComparisonBetweenNetworks\data\airline_routes_data\reduced_routes.gexf')
air_routes_graph = nx.readwrite.read_gexf(ar_dir_path + 'reduced_routes.gexf')
sister_cities_graph = nx.readwrite.read_gexf(ss_dir_path + 'sister_cities.gexf')
build_travels_graph(air_routes_graph, sister_cities_graph)
