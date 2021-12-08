class Node:
    def __init__(self, node):
        self.id = node
        self.neighbours = dict()

    def __str__(self):
        return f"'{self.id}' neighbours:   " \
               f"{[f'{n}, w={self.neighbours[n]}' for n in self.neighbours]}"

    def add_neighbour(self, neighbour, weight=0):
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

    def __str__(self):
        pass

    def add_node(self, node):
        self.nodes_number += 1
        current_node = Node(node)
        self.nodes[node] = current_node
        return current_node

    def get_node(self, node):
        return self.nodes[node] if node in self.nodes else None

    def add_edge(self, from_node, to_node, weight=0):
        if from_node not in self.nodes:
            self.add_node(from_node)
        if to_node not in self.nodes:
            self.add_node(to_node)

        self.nodes[from_node].add_neighbour(to_node, weight)

    def get_nodes(self):
        return self.nodes.keys()


if __name__ == '__main__':

    g = Graph()

    g.add_node('a')
    g.add_node('b')
    g.add_node('c')
    g.add_node('d')
    g.add_node('e')
    g.add_node('f')

    g.add_edge('a', 'b', 7)
    g.add_edge('a', 'c', 9)
    g.add_edge('a', 'f', 14)
    g.add_edge('b', 'c', 10)
    g.add_edge('b', 'd', 15)
    g.add_edge('c', 'd', 11)
    g.add_edge('c', 'f', 2)
    g.add_edge('d', 'e', 6)
    g.add_edge('e', 'f', 9)

    for n in g:
        print(n)
