
class Graph:
    
    def __init__(self,gDict=None):
        if gDict is None:
            gDict = {}
        self.gDict = gDict
        
    def getVertices(self):
        return self.gDict.keys()
    
    def getEdges(self):
        edges = []
        
        for vertex in self.gDict.keys():
            for otherVertex in self.gDict[vertex]:
                if {vertex,otherVertex} not in edges:
                    edges.append({vertex,otherVertex})
        
        return edges
    
    def addVertex(self,vertex):
        if vertex not in self.getVertices():
            self.gDict[vertex] = []

    def addEdge(self,edge):
        edges = set(edge)
        (vertex,otherVertex) = tuple(edges)
        
        if vertex not in self.gDict:
            self.gDict[vertex] = [otherVertex]
        else:
            (self.gDict[vertex]).append(otherVertex)
    
    def dfs(self,vertex, visited = None):
        
        if visited == None:
            visited = set()    
        visited.add(vertex)
        print(vertex)
        for otherVertex in set(self.gDict[vertex]) - visited:
            self.dfs(otherVertex,visited)

if __name__ == "__main__":
    
    sample = {
        "a" : ["b","c"],
        "b" : ["a","d"],
        "c" : ["a","d"],
        "d" : ["e"],
        "e" : ["d"]
    }
    
    g = Graph(sample)
    
    g.dfs('a')
    

