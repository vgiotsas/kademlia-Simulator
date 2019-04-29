import random
import math
import hashlib
from node import Node
from coordinator import Coordinator

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
    print(bootstrap)
    print(newNode)
    bootstrap['node'].insertNode(newNode['id'])
    newNode['node'].insertNode(bootstrap['id'])
    randomId = newNode['node'].createRandomId()
    for i in randomId:
        insert = None
        #qui siamo in un bucket
        #devo andare avanti finchè non riempo il bucket oppure finchè non mi arrivano più info nuove
        fNode = bootstrap['node'].findNode(i)
        if fNode is not None:
            for n in fNode:
                newNode['node'].insertNode(n['id'])
        h = int(math.log2(bootstrap['id']))

        for i in newNode['node']._routingTable[h]:
            if i is not None:
                for n in c.nodeList:
                    if n['id'] == i['id']:
                        nn = n['node'].findNode(i['id'])
                        if nn is not None:
                            print(nn)
                            for n in nn:
                                newNode['node'].insertNode(n['id'])
                        
    c.nodeList.append(c.notNetworkNode[randNn])
    del c.notNetworkNode[randNn]

for i in c.nodeList:
    print(i['id'])
    print(i['node']._routingTable)
    print("--------------")