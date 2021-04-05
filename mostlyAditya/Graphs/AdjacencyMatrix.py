class Graph:
    def __init__(self,numVertex):
        self.adjMatrix=[[-1] for x in range(numVertex)]
        self.numVertex=numVertex
        self.vertices={}
        self.verticeslist=[0]*numVertex