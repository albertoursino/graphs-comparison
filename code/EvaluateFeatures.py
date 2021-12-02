from Utility import ss_dir_path, ar_dir_path
import networkx as nx

try:
    s_cities = nx.readwrite.read_gexf(ss_dir_path + 'sister_cities.gexf')
    s_cities_red = nx.readwrite.read_gexf(ss_dir_path + 'reduced_sister_cities.gexf')
    routes_graph = nx.readwrite.read_gexf(ar_dir_path + 'routes.gexf')
    routes_red = nx.readwrite.read_gexf(ar_dir_path + 'reduced_routes.gexf')
except FileNotFoundError:
    exit("No gexf files found! Run GraphMerge first!")
