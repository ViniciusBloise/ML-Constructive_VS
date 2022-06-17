import networkx as nx

def from_numpy_matrix(A):
    G = nx.from_numpy_matrix(A)
    return G