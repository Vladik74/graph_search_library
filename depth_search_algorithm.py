from collections import deque


graph = {'A': ['M', 'P'],
         'M': ['A', 'N'],
         'N': ['M', 'B'],
         'P': ['A', 'B'],
         'B': ['P', 'N']}


def dsa(start, goal, graph):
    queue = deque([start])
    visited = {}
    visited[start] = None

    while queue:
        current_node = queue.popleft()
        if current_node == goal:
            break

        next_nodes = graph[current_node]
        for next_node in next_nodes:
            if next_node not in visited:
                queue.append(next_node)
                visited[next_node] = current_node
    return visited


start = 'A'
goal = 'B'
current_node = goal
visited = dsa(start, goal, graph)
while current_node != start:
    current_node = visited[current_node]
    print(current_node)
