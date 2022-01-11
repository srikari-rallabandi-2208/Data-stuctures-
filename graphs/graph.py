
class Graph:
    
    def __init__(self,gDict=None):
        if gDict is None:
            gDict = {}
        self.gDict = gDict
    
    def getVertices(self):
        return list(self.gDict.keys())
    
    def getEdges(self):
        edges = []
        
        for vertex in self.gDict:
            for otherVertex in self.gDict[vertex]:
                if {otherVertex,vertex} not in edges:
                    edges.append({vertex,otherVertex})
        
        return edges
    
    def addVertex(self,vertex):
        if vertex not in self.gDict:
            self.gDict[vertex] = []
            
    def addEdge(self,edge):
        edge = set(edge)
        (vertex,otherVertex) = tuple(edge)
        if vertex not in self.gDict:
            self.gDict[vertex] = [otherVertex]
        else:
            (self.gDict[vertex]).append(otherVertex)
                    
sample = {
    "a" : ["b","c"],
    "b" : ["a","d"],
    "c" : ["a","d"],
    "d" : ["e"],
    "e" : ["d"]
}

g = Graph(sample)

print(g.getVertices())
print(g.getEdges())
g.addVertex("f")
print(g.getVertices())
g.addEdge({"a","e"})
g.addEdge({"a","c"})
print(g.getEdges())

