import sys
from pathlib import Path
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
from itertools import combinations


def distance(a, b):
    a = np.array(a, dtype=int)
    b = np.array(b, dtype=int)
    c = np.subtract(a, b)
    # print(a, b, c)
    return np.linalg.norm(c)


def star_one(data):
    nodes = [tuple(row) for row in data]
    edges = combinations(nodes, 2)
    w_edges = []
    for a, b in edges:
        c = distance(a, b)
        if c:
            w_edges.append((a, b, c))
    w_edges.sort(key=lambda e: e[-1])
    G = nx.Graph()
    G.add_nodes_from(nodes)
    G.add_weighted_edges_from(w_edges[:1000])
    # for row in w_edges[:10]:
    #     # start = ",".join([str(e) for e in row[0]])
    #     # end = ",".join([str(e) for e in row[1]])
    #     # print(start, end, row[-1])
    c_len = [len(e) for e in nx.connected_components(G)]
    c_len.sort(reverse=True)

    # nx.draw(G)
    # plt.show()
    return np.prod(c_len[:3])


def star_two(data):
    nodes = [tuple(row) for row in data]
    edges = combinations(nodes, 2)
    w_edges = []
    for a, b in edges:
        c = distance(a, b)
        if c:
            w_edges.append((a, b, c))
    w_edges.sort(key=lambda e: e[-1])
    G = nx.Graph()
    G.add_nodes_from(nodes)

    for row in w_edges:
        # start = ",".join([str(e) for e in row[0]])
        # end = ",".join([str(e) for e in row[1]])
        # print(start, end, row[-1])
        G.add_edge(row[0], row[1], weight=row[-1])
        # print(len(list(nx.connected_components(G))))
        if nx.components.is_connected(G):
            return row[0][0] * row[1][0]


def main():
    data = []
    type = sys.argv[2]
    script_name = Path(__file__).name
    day = script_name.replace(".py", "")
    data = np.loadtxt(f"data/{day}_{type}.txt", delimiter=",", dtype=np.uint)

    if sys.argv[1] == "1":
        print(star_one(data))
    if sys.argv[1] == "2":
        print(star_two(data))


if __name__ == "__main__":
    main()
