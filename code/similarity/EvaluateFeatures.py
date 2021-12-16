from ..Utility import ss_dir_path, ar_dir_path
import networkx as nx
import networkx.algorithms as nx_alg


try:
    s_cities = nx.readwrite.read_gexf(ss_dir_path + 'sister_cities.gexf')
    s_cities_red = nx.readwrite.read_gexf(ss_dir_path + 'reduced_sister_cities.gexf')
    routes = nx.readwrite.read_gexf(ar_dir_path + 'routes.gexf')
    routes_red = nx.readwrite.read_gexf(ar_dir_path + 'reduced_routes.gexf')

    # SISTER CITIES

    percent_k = 100  # percent sample size of nodes considered for the computation of centrality
    btw_centrality = nx_alg.betweenness_centrality(s_cities_red, percent_k//100 * s_cities_red.number_of_nodes())
    cls_centrality = nx_alg.closeness_centrality(s_cities_red)
    clustering_co = nx_alg.average_clustering(s_cities_red)

    print("SISTER CITIES REDUCED:")
    print("--> Betweenness centrality: ", btw_centrality)
    print("--> Closeness centrality: ", cls_centrality)
    print("--> Clustering centrality: ", clustering_co)

    # ROUTES

    percent_k = 100  # percent sample size of nodes considered for the computation of centrality
    btw_centrality = nx_alg.betweenness_centrality(routes_red, percent_k//100 * routes_red.number_of_nodes())
    cls_centrality = nx_alg.closeness_centrality(routes_red)
    clustering_co = nx_alg.average_clustering(routes_red)

    print("ROUTES REDUCED:")
    print("--> Betweenness centrality: ", btw_centrality)
    print("--> Closeness centrality: ", cls_centrality)
    print("--> Clustering centrality: ", clustering_co)

except FileNotFoundError:
    exit("No gexf files found! Run GraphMerge first!")


