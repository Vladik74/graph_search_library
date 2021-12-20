from heapq import *

graph = {'0': [(2, '2'), (3, '4')],
         '2': [(2, '0'), (2, '3')],
         '3': [(2, '2'), (2, '1')],
         '4': [(3, '0'), (4, '1')],
         '1': [(4, '4'), (2, '3')]}


def heuristic(a, b):
    return abs(int(a[0]) - int(b[0])) + abs(int(a[1]) - int(b[1]))


def a_algorithm(start, goal, graph):
    queue = []
    heappush(queue, (0, start))
    cost_visited = {start: 0}
    visited = {start: None}

    while queue:
        cur_cost, cur_node = heappop(queue)
        if cur_node == goal:
            break

        next_nodes = graph[cur_node]
        for next_node in next_nodes:
            neigh_cost, neigh_node = next_node
            new_cost = cost_visited[cur_node] + neigh_cost

            if neigh_node not in cost_visited or new_cost < cost_visited[neigh_node]:
                priority = new_cost + heuristic(neigh_node, goal)
                heappush(queue, (priority, neigh_node))
                cost_visited[neigh_node] = new_cost
                visited[neigh_node] = cur_node
    return visited


start = '0'
goal = '1'
cur_node = goal
visited = a_algorithm(start, goal, graph)
while cur_node != start:
    cur_node = visited[cur_node]
    print(cur_node)
