from collections import defaultdict

class Graph(object):
    def __init__(self, connections, directed=False):
        self._graph = defaultdict(set)
        self._directed = directed
        self.add_connections(connections)

    def add_connections(self, connections):
            for node1, node2 in connections:
                self.add(node1, node2)
                
    def add(self, node1, node2 = None):
        self._graph[node1].add(node2)
        if not self._directed:
            self._graph[node2].add(node1)

    def __str__(self):
        return '{}({})'.format(self.__class__.__name__, dict(self._graph))