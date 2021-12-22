# Based on
# QUADRATIC ASSIGNMENT AS A GENERAL DATA ANALYSIS STRATEGY By L. HUBERT and J.SCHULTZ
# This method perhaps is more interesting when we want to compare graphs for
# which no node correspondence is known (UKC)


import networkx as nx
import numpy as np
from python_files.Utility import ss_dir_path, ar_dir_path
import matplotlib.pyplot as plt
from tqdm import tqdm
import distances


# Permute rows and columns (in a similar way) of a matrix
# according to a permutation generated uniformly at random.
def random_permute(mat: np.matrix):
    p = np.random.permutation(range(mat.shape[0]))
    return mat[:, p][p, :]


# Begin monte carlo simulations.
# Return all similarity scores in a list.
def monte_carlo(mat1, mat2, steps):
    res = []
    for i in tqdm(range(steps), desc="monte carlo"):
        meas = distances.num_edges_in_common(mat1, random_permute(mat2))
        res.append(meas)
    return np.array(res)


try:
    s_cities_red: nx.Graph = nx.readwrite.read_gexf(ss_dir_path + 'reduced_sister_cities.gexf')
    routes_red: nx.Graph = nx.readwrite.read_gexf(ar_dir_path + 'reduced_routes.gexf')

    # these adjacency matrices are sparse, to make them dense we call todense()

    A1 = nx.adjacency_matrix(s_cities_red).todense()
    A2 = nx.adjacency_matrix(routes_red).todense()

    # replace all positive weights with 1's
    A2[A2 > 1] = 1

    n = A1.shape[0]
    q1 = s_cities_red.size()
    q2 = routes_red.size()
    print("Sister cities nodes: ", n, " edges: ", q1)
    print("Airline routes  nodes: ", n, " edges: ", q2)

    # np.random.seed(0)  # for reproducibility results

    current_res = distances.num_edges_in_common(A1, A2)
    print("Similarity measure: ", current_res)

    results = monte_carlo(A1, A2, 20000)
    p_value = (results >= current_res).sum() / results.size

    # this expected value can be found in the paper
    expected_value = 4 * q1 * q2 / n / (n - 1)

    print("P value: ", p_value)
    print("Expected value: ", expected_value)
    plt.hist(results, bins=100)
    plt.xlabel('Similarity measure')
    plt.grid(True)
    plt.show()
except FileNotFoundError:
    exit("No gexf files found! Run GraphMerge first!")
