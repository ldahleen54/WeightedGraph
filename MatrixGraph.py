#a class for a vertex object
#it is more consistent with the list graph format but can probably be ignored for just using a string for the vertex name

class Graph:
    #set of vertices added to the graph
    vertices = {}
    #edge matrix
    edges = []
    #indices for the edges to find it in the matrix
    edge_indices = {}

    def add_vertex(self, vertex):
        # if isinstance(vertex, Vertex) and vertex.name not in self.vertices:
        #     self.vertices[vertex.name] = vertex
        #     for row in self.edges:
        #         row.append(0)
        #     self.edges.append([0] * (len(self.edge_indices)))
        #     self.edge_indices[vertex.name] = len(self.edge_indices)
        #     return True
        if len(self.vertices) == 0:
            # self.edges.append(0)
            for row in self.edges:
                row.append([0])
        if isinstance(vertex, basestring) and vertex not in self.vertices:
            self.vertices[vertex] = vertex

            self.edges.append([0] * (len(self.edge_indices)))
            for row in self.edges:
                row.append(0)

            self.edge_indices[vertex] = len(self.edge_indices)
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

    def __str__(self):


        string = ''
        string = self.edge_indices.values().__str__()

        string2 = '\n'
        for edgelist in self.edges:
            for edge in edgelist:
                string2 += edge.__str__()
            string2 += '\n'
        return string + string2


