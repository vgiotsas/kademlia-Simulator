import random
import math
import hashlib
import csv
from node import Node
from coordinator import Coordinator

c = Coordinator(6,5)
ip = c.createIp()
port = c.createPort()
c._Coordinator__createNode()
#scelgo il bootstrap a random da nodelist
while len(c.notNetworkNode) > 0:
    randBts = random.randint(0, len(c.nodeList) - 1)
    bootstrap = c.nodeList[randBts]
    randNn = random.randint(0, len(c.notNetworkNode) - 1)
    newNode = c.notNetworkNode[randNn]
    print(bootstrap)
    print(newNode)
    bootstrap['node'].insertNode(newNode['id'])
    newNode['node'].insertNode(bootstrap['id'])
    randomId = newNode['node'].createRandomId()
    for i in randomId:
        fNode = bootstrap['node'].findNode(i)
        if fNode is not None:
            for n in fNode:
                newNode['node'].insertNode(n['id'])
        h = int(math.log2(bootstrap['id']))
        insert = None

                        
    c.nodeList.append(c.notNetworkNode[randNn])
    del c.notNetworkNode[randNn]

for i in c.nodeList:
    print(i['id'])
    print(i['node']._routingTable)
    print("--------------")


def writeEdgeCsv(nodeList):
    with open('edge.csv', mode='w') as node_file:
        node_writer = csv.writer(node_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for i in c.nodeList:
            if i is not None:
                for n in i['node']._routingTable:
                    listNodeEdge = []
                    for k in n:
                        if k is not None:
                            listNodeEdge.append(i['id'])
                            listNodeEdge.append(k['id'])
                            node_writer.writerow(listNodeEdge)


def writeNodeCsv(nodeList):
    with open('node.csv', mode='w') as node_file:
        node_writer = csv.writer(node_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        new_list = [i["id"] for i in nodeList]
        node_writer.writerow(new_list)

writeNodeCsv(c.nodeList)
writeEdgeCsv(c.nodeList)