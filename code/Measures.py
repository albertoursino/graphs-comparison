import networkx as nx
import numpy as np
from Utility import ss_dir_path, ar_dir_path
import matplotlib.pyplot as plt
from tqdm import tqdm


def same_edge_set_measure(mat1: np.matrix, mat2: np.matrix):
    return np.sum(np.multiply(mat1, mat2))


def random_permute(mat: np.matrix):
    p = np.random.permutation(range(mat.shape[0]))
    return mat[:, p][p, :]


def monte_carlo(mat1, mat2, steps):
    res = []
    for i in tqdm(range(steps), desc="monte carlo"):
        meas = same_edge_set_measure(mat1, random_permute(mat2))
        res.append(meas)
    return np.array(res)


try:
    s_cities_red: nx.Graph = nx.readwrite.read_gexf(ss_dir_path + 'reduced_sister_cities.gexf')
    routes_red: nx.Graph = nx.readwrite.read_gexf(ar_dir_path + 'reduced_routes.gexf')

    A1 = nx.adjacency_matrix(s_cities_red).todense()
    A2 = nx.adjacency_matrix(routes_red).todense()
    A2[A2 > 1] = 1
    n = A1.shape[0]
    q1 = s_cities_red.size()
    q2 = routes_red.size()
    print("Sister cities nodes: ", n, " edges: ", q1)
    print("Airline routes  nodes: ", n, " edges: ", q2)

    # np.random.seed(0)  # for reproducibility results
    current_res = same_edge_set_measure(A1, A2)
    print("Similarity measure: ", current_res)

    results = monte_carlo(A1, A2, 20000)
    p_value = (results >= current_res).sum() / results.size
    expected_value = 4*q1*q2/n/(n-1)
    print("P value: ", p_value)
    print("Expected value: ", expected_value)
    plt.hist(results, bins=100)
    plt.xlabel('Similarity measure')
    plt.grid(True)
    plt.show()
except FileNotFoundError:
    exit("No gexf files found! Run GraphMerge first!")



