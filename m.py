from node import Node
from coordinator import Coordinator
from nxGraph import NxGra
from graph import Graph
from utility import removeFile, findFile



def main():
    n = input("Inserisci il numero di nodi ")
    m = input("inserisci il numero di bit")
    print("ciao")
    c = Coordinator(int(n),int(m)) #istanzia la classe coordinator
    ng = NxGra() #istanzia la classe nxGraph
    g = Graph() #istanzia la classe graph
    c.main() 
    ng.mainGraph()
    ng.snapshotGraph()
    g.inDegreeBarplot()
    g.outDegreeBarplot()
    g.clusteringBarplot(ng.getClusteringCoeff())



if __name__ == "__main__":
    main()