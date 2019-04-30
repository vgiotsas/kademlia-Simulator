import random
import math
import hashlib
import csv
from node import Node
from coordinator import Coordinator
dimensionOfReturn = 7
c = Coordinator(5,5)
ip = c.createIp()
port = c.createPort()
c._Coordinator__createNode()
#scelgo il bootstrap a random da nodelist
while len(c.notNetworkNode) > 0:
    randBts = random.randint(0, len(c.nodeList) - 1)
    bootstrap = c.nodeList[randBts]
    randNn = random.randint(0, len(c.notNetworkNode) - 1)
    newNode = c.notNetworkNode[randNn]

    c.nodeList.append(c.notNetworkNode[randNn])
    del c.notNetworkNode[randNn]

    print(bootstrap)
    print(newNode)
    kNode = []
    prev = None
    counter = 3
    bootstrap['node'].insertNode(newNode['id'])
    newNode['node'].insertNode(bootstrap['id'])
    randomId = newNode['node'].createRandomId()
    for i in randomId:
        while len(kNode) < dimensionOfReturn:
            print("_______________________")
            print(prev)
            if not kNode:
                prev = 0
            else:
                prev = kNode[len(kNode)-1]['id']
            kNode = kNode + bootstrap['node'].findNode(i)
            #faccio find node sugli altri 2
            for j in range(counter-3, counter):
                for n in c.nodeList:
                    if kNode[j]:
                        if n['id'] == kNode[j]['id']:
                            kNode = kNode + n['node'].findNode(i)
            kNode = sorted(kNode, key=lambda k: k['dist'])
            if kNode[len(kNode) -1] == prev: 
                break
            counter += 3


        if kNode is not None:
            #se fnode <
            for n in kNode:
                newNode['node'].insertNode(n['id'])
        """for list in c.nodeList:
            for k in list['node']._routingTable[int(math.log2(i))]:
                if k is not None:
                    fNode = bootstrap['node'].findNode(k['id'])
                    for n in fNode:
                        newNode['node'].insertNode(n['id'])
        """
"""
for i in c.nodeList:
    for rt in i['node']._routingTable:
        print(rt)
"""
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