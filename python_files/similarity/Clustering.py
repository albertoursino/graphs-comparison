# ------> You need to install the proper package with "pip install python-louvain"
import community as community_louvain
import networkx as nx
from networkx import edge_betweenness_centrality as ebg
from networkx.algorithms.community import girvan_newman
from networkx.algorithms.community import greedy_modularity_communities
from sklearn.metrics.cluster import adjusted_rand_score
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
    #TODO: return the clustering in a dictionary form, where each key is a node of the graph and the
    #      relative value is a numerical label of the cluster to which it has been assigned.
    return list


def gmc_clustering(graph):
    """
    Detection of communities using Clauset-Newman-Moore greedy modularity maximization. The algorithm
    progressively joins pairs of communities that most increase modularity (until no such pair exists).
    :param graph: the graph subject to clustering.
    :return: list where each element is a set representing a cluster of vertices.
    """
    c = greedy_modularity_communities(graph)
    #TODO: return the clustering in a dictionary form, where each key is a node of the graph and the
    #      relative value is a numerical label of the cluster to which it has been assigned.
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


def compare_clusters(dict1, dict2):
    """
    Comparison of two clusterings using Rand index (RI) (adjusted for chance).
    :param dict1: Dictionary expressing the clustering of a set of objects: each object is the key, while each value
                  is the label of the relative cluster.
    :param dict2: analogous as above.
    :return: returns the adjusted random index score (between -1 and +1): ARI = (RI_1 - RI_2) / (max(RI) - RI_2)
    """
    list1 = []
    list2 = []
    for key in sorted(dict1):
        list1.append(dict1[key])
    for key in sorted(dict2):
        list2.append(dict2[key])
    # The adjusted Rand index is thus ensured to have a value close to 0.0 for random labeling independently
    # of the number of clusters and samples and exactly 1.0 when the clusterings are identical (up to a permutation)
    return adjusted_rand_score(list1, list2)


s_cities = nx.readwrite.read_gexf(
    sc_dir_path + 'reduced_sister_cities.gexf')
routes = nx.readwrite.read_gexf(
    ar_dir_path + 'reduced_routes.gexf')

#sc_GNcommunities = gn_clustering(s_cities)
#ar_GNcommunities = gn_clustering(routes)

#sc_GMCcommunities = gmc_clustering(s_cities)
#ar_GMCcommunities = gmc_clustering(routes)

sc_LOUVAINcommunities = louvain_clustering(s_cities)
ar_LOUVAINcommunities = louvain_clustering(routes)
print(compare_clusters(sc_LOUVAINcommunities, ar_LOUVAINcommunities))