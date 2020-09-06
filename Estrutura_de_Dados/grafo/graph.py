from collections import defaultdict

class Grafo():
    def __init__(self,edges,digraph=False):
        self.adj = defaultdict(set)
        self.digraph = digraph
        self.add_edges(edges)

    
    def get_vertices(self):
        return list(self.adj.keys)
    

    def get_edges(self):
        return [(k,v) for k in self.adj.keys() for v in self.adj[k]]


    def add_edges(self,edges):
        for k,v in edges:
            self.adj[k].add(v)
            
            if not self.digraph:
                self.adj[v].add(k)
    

    def hasEdges(self,u,v):
        return u in self.adj and v in self.adj[u]


    def __len__(self):
        return len(self.adj)
    

    def __str__(self):
        return '{}({})'.format(self.__class__.__name__, dict(self.adj))