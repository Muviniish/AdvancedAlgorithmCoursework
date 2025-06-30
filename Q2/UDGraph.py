class UDGraph:
    def __init__(self):
        self.graph = {}

    def addVertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex]=[]

    def addEdge(self, from_vertex, to_vertex):
        self.graph[from_vertex].append(to_vertex)
        
    def remove_edge(self, from_vertex, to_vertex):
        if from_vertex in self.graph:
            if to_vertex in self.graph[from_vertex]:
                self.graph[from_vertex].remove(to_vertex)
            else:
                raise ValueError("Edge does not exists")
            
    def get_vertices(self):
        return list(self.graph.keys())
        
    def listOutgoingAdjacentVertex(self, vertex):
        return self.graph[vertex]
    
    def listIncomingAdjacentVertex(self, target_vertex):
        incoming = []
        for from_node, to_node in self.graph.items():
            if target_vertex in to_node:
                incoming.append(from_node)
        return incoming
    