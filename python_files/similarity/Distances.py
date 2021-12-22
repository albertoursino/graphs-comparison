import numpy as np


# Given two graphs by their adjacency matrices,
# return the number of edges in common (in case all entries are 0's and 1's).
def num_edges_in_common(mat1: np.matrix, mat2: np.matrix):
    return np.sum(np.multiply(mat1, mat2))
