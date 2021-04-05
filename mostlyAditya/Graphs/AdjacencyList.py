class Node:
    def __init__(self,vertex):
        self.vertex=vertex
        self.next=None

class Graph:
    def __init__(self,numVertex):
        self.vertices=numVertex
        self.Graph=[None]*numVertex
    
    def add_edge(self,src,dest):
        node=Node(src)
        node.next=self.Graph[dest]
        self.Graph[dest]=node

        node=Node(dest)
        node.next=self.Graph[src]
        self.Graph[src]=node

    def printGraph(self):
        for x in range(self.vertices):
            print(f"The Adjacency list {x}\n{x}",end="")
            temp=self.Graph[x]
            while temp:
                print(f"-->{temp.vertex}",end="")
                temp=temp.next
            print()
graph = Graph(5)
graph.add_edge(0, 1)
graph.add_edge(0, 4)
graph.add_edge(1, 2)
graph.add_edge(1, 3)
graph.add_edge(1, 4)
graph.add_edge(2, 3)
graph.add_edge(3, 4)
graph.printGraph()            