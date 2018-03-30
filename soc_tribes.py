from graph import Graph

def loadEdges(path):
    tuples = []
    try:
        with open(path, 'r') as f:
            for line in f:
                if not line.__contains__('%'):
                    node = line.rstrip().split(' ', 2)
                    tuples.append(tuple(node[:-1]) if len(node) > 2 else tuple([node.pop(), node.pop() if node else None]))
        return tuples
    except IOError:
        print("Error: file does not exist")
    return 0

def output(graph):
    for node, connections in graph:
        if node is not None:
            print ("Node %s has degree of %i" % (node, sum(1 for _ in filter(None.__ne__, connections))))


edges = loadEdges('./soc-tribes.edges')
if edges:
    network = Graph(edges)
    output(network._graph.items())
else:
    print("No nodes found")
