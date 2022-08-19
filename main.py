from node import Node
from coordinator import Coordinator
from nxGraph import NxGra
from graph import Graph
from utility import removeFile, findFile



def main():
    n = input("Enter the number of nodes ")
    m = input("Enter the number of bits")
    c = Coordinator(int(n),int(m)) #instantiates the coordinator class
    ng = NxGra() #instantiates the class nxGraph
    g = Graph() #instantiates the class graph
    c.main() 
    ng.mainGraph()
    ng.snapshotGraph()
    g.inDegreeBarplot()
    g.outDegreeBarplot()
    g.clusteringBarplot(ng.getClusteringCoeff())



if __name__ == "__main__":
    main()
