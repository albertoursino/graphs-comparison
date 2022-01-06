# ------> You need to install the proper package "pip install python-louvain"
import community as community_louvain
import networkx as nx
from networkx import edge_betweenness_centrality as ebg
from networkx.algorithms.community import girvan_newman
from networkx.algorithms.community import greedy_modularity_communities
from python_files.Utility import sc_dir_path, ar_dir_path


def most_central_edge(graph):
    # Searching for the edge with highest betweenness centrality
    centrality = ebg(graph, weight = "weight")
    return max(centrality, key = centrality.get)


def gn_clustering(graph):
    """
    Detection of communities using Girvan–Newman method; the algorithm proceeds removing each time the
    edge with highest betweenness centrality.
    :param graph: the graph subject to clustering.
    :return: list where each element is a tuple containing lists representing the partitions of the vertices
             in communities. Being k the number of communities obtained in a partition, the returned list
             has an element for each possible value of k.
    """
    partitions = girvan_newman(graph, most_valuable_edge = most_central_edge)
    list = []
    for communities in partitions:
        t = tuple(sorted(c) for c in communities)
        list.append(t)
        print(t)
    return list


def gmc_clustering(graph):
    """
    Detection of communities using Clauset-Newman-Moore greedy modularity maximization. The algorithm
    progressively joins pairs of communities that most increase modularity (until no such pair exists).
    :param graph: the graph subject to clustering.
    :return: list where each element is a set representing a cluster of vertices.
    """
    c = greedy_modularity_communities(graph)
    return c


def louvain_clustering(graph):
    """
    Detection of communities using the Louvain method (https://github.com/taynaud/python-louvain).
    :param graph: the graph subject to clustering.
    :return: dictionary in which each key is a vertex and the correspondent value is a numerical label
             of the cluster to which the vertex belongs.
    """
    partition = community_louvain.best_partition(graph)
    return partition


s_cities = nx.readwrite.read_gexf(
    sc_dir_path + 'reduced_sister_cities.gexf')
routes = nx.readwrite.read_gexf(
    ar_dir_path + 'reduced_routes.gexf')

#sc_GNcommunities = gn_clustering(s_cities)
#ar_GNcommunities = gn_clustering(routes)

#sc_GMCcommunities = gmc_clustering(s_cities)
#ar_GMCcommunities = gmc_clustering(routes)

#sc_LOUVAINcommunities = louvain_clustering(s_cities)
#ar_LOUVAINcommunities = louvain_clustering(routes)