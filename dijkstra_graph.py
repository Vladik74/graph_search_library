from collections import defaultdict


class Node:
    def __init__(self, node):
        self.id = node
        self.neighbours = defaultdict(int)

    def __str__(self):
        return f"'{self.id}' neighbours:   " \
               f"{[f'{n}, w={self.neighbours[n]}' for n in self.neighbours]}"

    def add_neighbour(self, neighbour, weight=0): #вычисляет расстояние от текущей до указанной
        self.neighbours[neighbour] = weight

    def get_edges(self):
        return self.neighbours.keys()

    def get_node_weight(self, node):
        return self.neighbours[node]

    def get_id(self):
        return self.id


class Graph:
    def __init__(self):
        self.nodes = dict()
        self.nodes_number = 0

    def __iter__(self):
        return iter(self.nodes.values())

    def __len__(self):
        return len(self.nodes)

    def __str__(self):
        pass

    def add_node(self, node):
        self.nodes_number += 1
        current_node = Node(node)
        self.nodes[node] = current_node
        return current_node

    def add_nodes(self, nodes_list):
        for node in nodes_list:
            self.add_node(node)

    def get_node(self, node):
        return self.nodes[node] if node in self.nodes else None

    def add_edge(self, from_node, to_node, weight=0):
        if from_node not in self.nodes:
            self.add_node(from_node)
        if to_node not in self.nodes:
            self.add_node(to_node)

        self.nodes[from_node].add_neighbour(to_node, weight)

    def add_edges(self, edges_list):
        for edge in edges_list:
            self.add_edge(edge[0], edge[1], edge[2])

    def get_nodes(self):
        return self.nodes.keys()


if __name__ == '__main__':

    g = Graph()

    g.add_nodes([0, 1, 2, 3, 4, 5])
    g.add_edges([(0, 1, 7), (0, 2, 9), (0, 5, 14), (1, 2, 10),
                 (1, 3, 15), (2, 3, 11), (2, 5, 2), (3, 4, 6),
                 (4, 5, 9)])

    # g.add_edge('a', 'b', 7)
    # g.add_edge('a', 'c', 9)
    # g.add_edge('a', 'f', 14)
    # g.add_edge('b', 'c', 10)
    # g.add_edge('b', 'd', 15)
    # g.add_edge('c', 'd', 11)
    # g.add_edge('c', 'f', 2)
    # g.add_edge('d', 'e', 6)
    # g.add_edge('e', 'f', 9)

    for n in g:
        print(n)
    print(g.get_node(1).neighbours[2])
