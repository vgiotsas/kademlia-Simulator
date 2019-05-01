import networkx as nx
import csv
import matplotlib.pyplot as plt
from utility import openCsv, findFile

class NxGra:

    clustCoeff = None

    def getClusteringCoeff(self):
        return self.clustCoeff

    def mainGraph(self):
        G = nx.Graph()

        node = openCsv('node.csv')
        """with open('node.csv', 'r') as f:
            reader = csv.reader(f)
            node = list(reader)"""
        edge = openCsv('edge.csv')
        """with open('edge.csv', 'r') as f:
            reader = csv.reader(f)
            edge = list(reader)"""

        ed = []
        for i in edge:
            tup = ()
            for l in range(0, len(i), 2):
                tup = (int(i[l]), int(i[l+1]))
                ed.append(tup)

        #G.add_nodes_from(node[0])
        G.add_edges_from(ed)
        #G.add_nodes_from([1,2,3,4,5])
        #G.add_edges_from([(1,2), (1,3), (2,4), (4,5)])

        nx.draw_circular(G, with_labels=True)
        
        print("diametro")
        print(nx.diameter(G))

        print("clustering coefficient")
        self.clustCoeff = nx.clustering(G)
        print(self.clustCoeff)

        print("diametro")
        print(nx.diameter(G))

        print("clustering coefficient")
        self.clustCoeff = nx.clustering(G)
        print(self.clustCoeff)
        s = 0
        for key, value in self.clustCoeff.items():
            s += value
        averageClustering = s/len(self.clustCoeff)
        print("average clustering")
        print(averageClustering)

        print("degree")
        deg = nx.degree(G)
        print(deg)
        sum = 0
        for i in deg:
            sum += i[0]
        averageDegree = sum/len(deg)
        print("average degree")
        print(averageDegree)

        plt.savefig('topology.jpg')
        plt.show()

    def snapshotGraph(self):
        G = nx.Graph()

        snapshotFile = findFile('snapshot*', '../kademlia')
        for icsv in snapshotFile:
            edge = openCsv(icsv)
            ed = []
            for i in edge:
                tup = ()
                for l in range(0, len(i), 2):
                    tup = (int(i[l]), int(i[l+1]))
                    ed.append(tup)

            #G.add_nodes_from(node[0])
            G.add_edges_from(ed)
            #G.add_nodes_from([1,2,3,4,5])
            #G.add_edges_from([(1,2), (1,3), (2,4), (4,5)])

            nx.draw_circular(G, with_labels=True)
        

            plt.savefig('topology'+icsv+'.jpg')
            plt.show()

