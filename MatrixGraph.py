#might be better as a library for now will add CLI in the future
#import click
import Queue

class Graph:

    #list of vertices in the graph WIP
    vertices = []
    #edge matrix
    edges = []

    def add_vertex(self, vertex):
        if isinstance(vertex, basestring) and vertex not in self.vertices:
            self.edges.append([0] * (len(self.edges)))
            for row in self.edges:
                row.append(0)
            self.vertices.append(vertex)

            return True
        else:
            return False

    # @click.command()
    # @click.option('--vertex', default=1, help='Number of greetings.')
    # @click.option('--name', prompt='Your name',
    #               help='The person to greet.')
    #finds the index of the vertex for the matrix
    def find_index(self, vertex):
        for index in range(len(self.vertices)):
            if self.vertices[index] == vertex:
                return index
        return True

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

    def get_weight(self, vertexOne, vertexTwo):
        indexOne = self.find_index(vertexOne)
        indexTwo = self.find_index(vertexTwo)
        return self.edges[indexOne][indexTwo]

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

        queue = Queue.PriorityQueue
        distance = {}
        current = start
        unvisited = set(self.vertices)

        currentIndex = self.find_index(current)
        startIndex = self.find_index(start)
        endIndex = self.find_index(end)

        #initialization
        for neighbor in self.vertices:

            distance[neighbor] = -1
        distance[start] = 0

        #end this loop when the destination vertex has been visited
        while end in unvisited:
            # consider neighbors
            for i in range(len(self.edges[currentIndex])):
                weight = self.edges[currentIndex][i]
                if weight != 0:
                    neighbor = self.vertices[i]
                    if distance[neighbor] == -1 or distance[neighbor] > weight:
                        distance[neighbor] = weight
                        queue.__reduce_ex__()

            #needs improvement probably too complicated
            counter = 1
            for item in distance:
                if counter == 1:
                    smallest = item
                    current = item
                elif distance[item] > -1 and item in unvisited and distance[item] < distance[smallest]:
                    current = item
                counter += 1

            # mark current vertex as unvisited
            unvisited.remove(current)





