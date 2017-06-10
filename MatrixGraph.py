class Graph:
    #list of vertices in the graph NI
    vertices = []
    #edge matrix
    edges = []

    def add_vertex(self, vertex):
        # if len(self.vertices_list) == 0:
        #     # self.edges.append(0)
        #     for row in self.edges:
        #         row.append([0])
        if isinstance(vertex, basestring) and vertex not in self.vertices:
            self.edges.append([0] * (len(self.edges)))
            for row in self.edges:
                row.append(0)
            self.vertices.append(vertex)

            return True
        else:
            return False

    #finds the index of the vertex for the matrix
    #replacement for the edge index dictionary
    def find_index(self, vertex):
        for index in range(len(self.vertices)):
            if self.vertices[index] == vertex:
                return index
        return False

    #adds a connection between two vertices in the graph
    def add_edge(self, vertexOne, vertexTwo, weight=1):
        if vertexOne in self.vertices and vertexTwo in self.vertices:
            indexOne = self.find_index(vertexOne)
            indexTwo = self.find_index(vertexTwo)

            self.edges[indexOne][indexTwo] = weight
            self.edges[indexTwo][indexOne] = weight
            return True
        else:
            return False

    def __str__(self):
        string = '  '
        string += ', '.join(map(str, self.vertices))
        #make this string line up correctly

        string2 = '\n'
        counter = 0
        for edgelist in self.edges:
            string2 += self.vertices[counter] + ' '
            for edge in edgelist:
                string2 += edge.__str__() + ' '
            string2 += '\n'
            counter += 1
        return string + string2

    #finds the shortest path between two vertices
    def dijkstra(self, start, end):
        distance = []
        current = start

        #assigning initial distance for the vertices
        for vertex in self.vertices:
            #a distance of -1 means infinity
            distance[vertex] = -1
        distance[start] = 0

        unvisited = set(self.vertices)
        index = self.find_index(current)

        for edgeList in self.edges[index]:
            for edge in edgeList:
                if edge != 0:
                    distance[]








