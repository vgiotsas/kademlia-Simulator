import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
import csv

class Graph:

    with open('edge.csv', 'r') as f:
        reader = csv.reader(f)
        edge = list(reader)

        ed = set()
        for i in edge:
            tup = ()
            for l in range(0, len(i), 2):
                tup = (int(i[l]), int(i[l+1]))
                ed.add(tup)

        with open('node.csv', 'r') as f:
            reader = csv.reader(f)
            node = list(reader)
        
        inOut = []
        for i in node[0]:
            inOut.append({'id': i, 'in': 0, 'out': 0})
        for i in ed:
            for j in inOut:
                if int(j['id']) == int(i[0]):
                    j['out'] += 1
                elif int(j['id']) == int(i[1]):
                    j['in'] += 1

        print(inOut)

        node = []
        inDe = []
        outDe = []
        for j in inOut:
            node.append(j['id'])
            inDe.append(j['in'])
            outDe.append(j['out'])

        def inDegreeBarplot(self):
            y_pos = np.arange(len(self.node))
            plt.bar(y_pos, self.inDe, align='center', alpha=0.5)
            plt.xticks(y_pos, self.node)
            plt.ylabel('in-degree')
            plt.xlabel('Node')
            
            plt.savefig('inDegree.jpg')
            plt.show()


        def outDegreeBarplot(self):
            y_pos = np.arange(len(self.node))
            plt.bar(y_pos, self.outDe, align='center', alpha=0.5)
            plt.xticks(y_pos, self.node)
            plt.ylabel('out-degree')
            plt.xlabel('Node')

            #plt.show()
            plt.savefig('outDegree.jpg')
            plt.show()

        def clusteringBarplot(self, dict):
            val = []
            node = []
            print(type(dict))
            for key, value in dict.items():
                val.append(value)
                node.append(key)
            y_pos = np.arange(len(val))
            plt.bar(y_pos, val, align='center', alpha=0.5)
            plt.xticks(y_pos, node)
            plt.ylabel('clustering coeff')
            plt.xlabel('Node')
            plt.savefig('clustCoeff.jpg')
            plt.show()
