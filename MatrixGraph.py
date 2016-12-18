class Vertex:
    def __init__(self, name):
        self.name = name


class Graph:
    vertices = {}
    edges = []
    edge_indices = {}

    def add_vertex(self, vertex):
        if isinstance(vertex, Vertex) and vertex.name not in self.vertices:
            self.vertices[vertex.name] = vertex
            for row in self.edges:
                row.append(0)
            self.edges.append([0] * (len(self.edge_indices)))
            self.edge_indices[vertex.name] = len(self.edge_indices)
            return True
        else:
            return False

    def add_edge(self, vertexOne, vertexTwo, weight=1):
        if vertexOne in self.vertices and vertexTwo in self.vertices:
            self.edges[self.edge_indices[vertexOne]][self.edge_indices[vertexTwo]] = weight
            self.edges[self.edge_indices[vertexTwo]][self.edge_indices[vertexOne]] = weight
            return True
        else:
            return False

    # Prints edges matrix
    def print_graph(self):
        print self.edges[0][1]
        for edge in self.edges:
            print edge
        for edgeIndex in self.edge_indices:
            print self.edge_indices[edgeIndex]


g = Graph()
a = Vertex('A')
g.add_vertex(a)
g.add_vertex(Vertex('B'))
for k in range(ord('A'), ord('K')):
    g.add_vertex(Vertex(chr(k)))





g.print_graph()
