from graph import Graph


def min_distance(graph, dist, min_dist_list):
    min_dist = float('inf')
    min_index = -1
    for v in range(len(graph)):
        if dist[v] < min_dist and min_dist_list[v] == False:
            min_dist = dist[v]
            min_index = v
    return min_index


def dijkstra(graph, end_node):
    dist = [float('inf')] * len(graph)
    dist[end_node] = 0
    min_dist_list = [False] * len(graph)
    for _ in graph:
        u = min_distance(graph, dist, min_dist_list)
        min_dist_list[u] = True
        for v in range(len(graph)):
            node = graph.get_node(u)
            if (node is not None and v in node.neighbours and not min_dist_list[v]
                    and dist[v] > dist[u] + node.neighbours[v]):
                dist[v] = dist[u] + node.neighbours[v]
    return dist


g = Graph()
g.add_nodes([0, 1, 2, 3, 4, 5])
g.add_edges([(0, 1, 7), (0, 2, 9), (0, 5, 14), (1, 2, 10),
             (1, 3, 15), (2, 3, 11), (2, 5, 1), (3, 4, 6),
             (4, 5, 9)])

print(dijkstra(g, 0))
