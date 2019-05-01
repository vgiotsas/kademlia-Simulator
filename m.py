from node import Node
from coordinator import Coordinator
from nxGraph import NxGra
from graph import Graph
from utility import removeFile, findFile

print("ciao")
c = Coordinator(5,5) #istanzia la classe coordinator
ng = NxGra() #istanzia la classe nxGraph
g = Graph() #istanzia la classe graph
c.main() 
ng.mainGraph()
ng.snapshotGraph()
g.inDegreeBarplot()
g.outDegreeBarplot()
g.clusteringBarplot(ng.getClusteringCoeff())