from python_files.Utility import ss_dir_path, ar_dir_path
import networkx as nx
import networkx.algorithms as nx_alg
import numpy as np
import scipy.stats
import scipy.spatial


# We add two extra features for each node, i.e. the betweeness centrality and the closeness centrality
def net_simile_get_features(graphs: [nx.Graph]):
    f = []
    for graph in graphs:
        bet_centrality = nx.betweenness_centrality(graph)
        clo_centrality = nx.betweenness_centrality(graph)
        size = graph.number_of_nodes()
        features = np.empty((size, 9))
        i = 0
        for node in graph.nodes:
            node_features = net_simile_get_node_features(graph, node)
            features[i, :] = node_features + (bet_centrality[node], clo_centrality[node])
            i = i + 1
        f.append(features)
    return f


#  Standard features from the paper: for each node we collect, in THIS order:
#  0) degree, 1) clustering coefficient, 2) average number of 2 hops neighbors,
#  3) average clustering coefficient for the neighbors of the current node,
#  4) number of edges in the ego network, 5) number of outgoing edges from the ego network,
#  6) number of neighbors in the ego network
def net_simile_get_node_features(graph, node):
    deg = graph.degree[node]
    c_coff = nx.clustering(graph, nodes=node)
    neighbors = list(graph.neighbors(node))
    avg_2hop = 0
    avg_clustering_coff = 0
    edges_ego = 0
    number_out_edges_ego = 0
    neighbors_ego = 0
    if deg > 0:
        avg_2hop = (sum(graph.degree[neigh] for neigh in neighbors) / deg)
        if deg > 1:
            avg_clustering_coff = nx.average_clustering(graph, nodes=neighbors)
        ego_g = nx.ego_graph(graph, node)
        edges_ego = ego_g.number_of_edges()
        outgoing_edges_ego = []
        for node_ego in ego_g.nodes:
            for node_incident_ego in graph.adj[node_ego]:
                if node_incident_ego not in ego_g.nodes:
                    outgoing_edges_ego.append(node_incident_ego)
        number_out_edges_ego = len(outgoing_edges_ego)
        neighbors_ego = len(set(outgoing_edges_ego))
    return deg, c_coff, avg_2hop, avg_clustering_coff, edges_ego, number_out_edges_ego, neighbors_ego


def net_simile_aggregator(feature_matrices):
    number_graphs = len(feature_matrices)
    signatures = []
    for i in range(number_graphs):
        f_matrix = feature_matrices[i]  # matrix graph_nodes x 8
        signature = []
        for j in [0, 1, 2, 3, 4, 5, 6]:  # change this set to select different features
            feat_col = f_matrix[:, j]
            signature_col = (np.median(feat_col), np.mean(feat_col),
                             np.std(feat_col), scipy.stats.skew(feat_col), scipy.stats.kurtosis(feat_col))
            signature += signature_col
        signatures.append(signature)
    return signatures


def net_simile_compare(graphs, normalized_sim=False, dist=scipy.spatial.distance.canberra):
    features = net_simile_get_features(graphs)
    signatures = net_simile_aggregator(features)
    number_graphs = len(graphs)
    similarities = []
    for i in range(number_graphs):
        for j in range(i+1, number_graphs):
            dist = dist(signatures[i], signatures[j])
            similarities.append((i, j, 1/(1+dist) if normalized_sim else 1/dist))
    return similarities


try:
    s_cities = nx.readwrite.read_gexf(ss_dir_path + 'sister_cities.gexf')
    s_cities_red = nx.readwrite.read_gexf(ss_dir_path + 'reduced_sister_cities.gexf')
    routes = nx.readwrite.read_gexf(ar_dir_path + 'routes.gexf')
    routes_red = nx.readwrite.read_gexf(ar_dir_path + 'reduced_routes.gexf')

    # SISTER CITIES

    # percent_k = 100  # percent sample size of nodes considered for the computation of centrality
    # btw_centrality = nx_alg.betweenness_centrality(s_cities_red, percent_k // 100 * s_cities_red.number_of_nodes())
    # cls_centrality = nx_alg.closeness_centrality(s_cities_red)
    # clustering_co = nx_alg.average_clustering(s_cities_red)

    # print("SISTER CITIES REDUCED:")
    # print("--> Betweenness centrality: ", btw_centrality)
    # print("--> Closeness centrality: ", cls_centrality)
    # print("--> Clustering centrality: ", clustering_co)

    # ROUTES

    # percent_k = 100  # percent sample size of nodes considered for the computation of centrality
    # btw_centrality = nx_alg.betweenness_centrality(routes_red, percent_k // 100 * routes_red.number_of_nodes())
    # cls_centrality = nx_alg.closeness_centrality(routes_red)
    # clustering_co = nx_alg.average_clustering(routes_red)

    # print("ROUTES REDUCED:")
    # print("--> Betweenness centrality: ", btw_centrality)
    # print("--> Closeness centrality: ", cls_centrality)
    # print("--> Clustering centrality: ", clustering_co)

    sim = net_simile_compare([s_cities, routes], True, dist=scipy.spatial.distance.cosine)
    print(sim)

except FileNotFoundError:
    exit("No gexf files found! Run GraphMerge first!")