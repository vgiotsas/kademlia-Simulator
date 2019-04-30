import networkx as nx
import csv
import matplotlib.pyplot as plt

G = nx.Graph()

with open('node.csv', 'r') as f:
    reader = csv.reader(f)
    node = list(reader)

with open('edge.csv', 'r') as f:
    reader = csv.reader(f)
    edge = list(reader)

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
print(nx.clustering(G))

print("degree")
print(nx.degree(G))


plt.show()
