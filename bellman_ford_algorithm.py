from collections import defaultdict
from graph import Graph
import datetime


def min_distance(graph, dist, min_dist_list):
    min_dist = float('inf')
    min_index = -1
    for v in range(len(graph)):
        if dist[v] < min_dist and min_dist_list[v] is False:
            min_dist = dist[v]
            min_index = v
    return min_index


# def negative_cycle_check(graph, dist):
#     negative_flag = False
#     for v in range(len(graph)):
#         node_v = graph.get_node(v)
#         for u in range(len(node_v.get_edges())):
#             node_u = graph.get_node(u)
#             if dist[u] != float('inf') and dist[u] + node_u.neighbours[v] < dist[v]:
#                 negative_flag = True
#     return negative_flag


def bellman_ford(graph, start_node):
    dist = [float('inf')] * len(graph)
    dist[start_node] = 0
    min_dist_list = [False] * len(graph)
    for _ in graph:
        u = min_distance(graph, dist, min_dist_list)
        min_dist_list[u] = True
        for v in range(len(graph)-1):
            node = graph.get_node(u)
            if (node is not None and v in node.neighbours and not min_dist_list[v]
                    and dist[v] > dist[u] + node.neighbours[v]):
                dist[v] = dist[u] + node.neighbours[v]
    return dist
    # negative_flag = negative_cycle_check(graph, dist)
    # if negative_flag:
    #     return 'graph contains negative cycle', dist
    # else:
    #     return dist


g4 = Graph()
for i in range(100):
    g4.add_node(i)
    if i < 96:
        g4.add_edge(i, i + 4, i * 2)
    if 2 < i < 50:
        g4.add_edge(i, i + 6, i * 3 + 4)
        g4.add_edge(i - 1, 2 * i + 1, 2 * i + 1)

g1 = Graph()
for i in range(10000):
    g1.add_node(i)
    if i < 9996:
        g1.add_edge(i, i + 4, i * 2)
    if 2 < i < 5000:
        g1.add_edge(i, i + 6, i * 3 + 4)
        g1.add_edge(i - 1, 2 * i + 1, 2 * i + 1)

g2 = Graph()
for i in range(1000):
    g2.add_node(i)
    if i < 996:
        g2.add_edge(i, i + 4, i * 2)
    if 2 < i < 500:
        g2.add_edge(i, i + 6, i * 3 + 4)
        g2.add_edge(i - 1, 2 * i + 1, 2 * i + 1)

g3 = Graph()
for i in range(50000):
    g3.add_node(i)
    if i < 49996:
        g3.add_edge(i, i + 4, i * 2)
    if 2 < i < 25000:
        g3.add_edge(i, i + 6, i * 3 + 4)
        g3.add_edge(i - 1, 2 * i + 1, 2 * i + 1)


# t4 = datetime.datetime.now()
# print(bellman_ford(g4, 0))
# print(datetime.datetime.now() - t4)
# t1 = datetime.datetime.now()
# print(bellman_ford(g1, 0))
# print(datetime.datetime.now() - t1)
t2 = datetime.datetime.now()
print(bellman_ford(g2, 0))
print(datetime.datetime.now() - t2)
# t3 = datetime.datetime.now()
# print(bellman_ford(g3, 0))
# print(datetime.datetime.now() - t3)