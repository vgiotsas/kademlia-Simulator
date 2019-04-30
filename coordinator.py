import random
import socket
import struct
from node import Node

class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class Coordinator(metaclass=Singleton):
    nodeNumber = None
    bitsNumber = None
    nodeList = []
    notNetworkNode = []
    nodeHashSet = set() #se nel set salvo ip+porta non c'è bisogno di istanziare classe, gli id coincidono


#TODO Da mettere in utility

    def createIp(self):
        return socket.inet_ntoa(struct.pack('>I', random.randint(1, 0xffffffff)))
    
    def createPort(self):
        port = random.randint(0, 49151)
        return str(port)
    
    def createId(self, ip, port):
        id = self.extractKBits(int(hash(ip + port)), self.bitsNumber)
        if id == 0:
            id = id + 1
        if id < 0 : 
            id *= -1
        return id

    def extractKBits(self, num, k, p = 0):
        binary = bin(num) 
    
        # remove first two characters 
        binary = binary[2:] 
        end = len(binary) - p 
        start = end - k + 1
        # extract k  bit sub-string 
        kBitSubStr = binary[start : end+1] 
        # convert extracted sub-string into decimal again
        return int(kBitSubStr,2)

#----------
    
    def __init__(self, n, m):
        #devo generare un nuovo nodo
        self.nodeNumber = n
        self.bitsNumber = m
        ip = self.createIp()
        port = self.createPort()
        id = self.createId(ip, port)
        self.nodeHashSet.add(id)
        no = Node(ip, port, id, m)
        self.nodeList.append({'id': no.getNodeId(), 'node': no})
        #self.nodeList.append(node(ip, port, id))

    def __createNode(self):
        #for i in range(1, self.nodeNumber):
        while len(self.nodeHashSet) < self.nodeNumber:
            ip = self.createIp()
            port = self.createPort()
            #id = self.extractKBits(self.createId(ip,port), self.bitsNumber)
            id = self.createId(ip,port)
            if id not in self.nodeHashSet:
                node = Node(ip, port, id, self.bitsNumber)
                #self.nodeList.append(node(ip, port, id))
                #self.nodeList.append({'id': node.getNodeId(), 'node': node})
                self.notNetworkNode.append({'id': node.getNodeId(), 'node': node})
                self.nodeHashSet.add(id)

    def main(self):
        dimensionOfReturn = 50
        self.__createNode()
        while len(self.notNetworkNode) > 0:
            randBts = random.randint(0, len(self.nodeList) - 1)
            bootstrap = self.nodeList[randBts]
            randNn = random.randint(0, len(self.notNetworkNode) - 1)
            newNode = self.notNetworkNode[randNn]

            self.nodeList.append(self.notNetworkNode[randNn])
            del self.notNetworkNode[randNn]

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
                    if not kNode:
                        prev = 0
                    else:
                        prev = kNode[len(kNode)-1]['id']
                    kNode = kNode + bootstrap['node'].findNode(i)
                    #faccio find node sugli altri 2
                    for j in range(counter-3, counter):
                        for n in self.nodeList:
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

        for i in self.nodeList:
            print(i['id'])
            print(i['node']._routingTable)
            print("--------------")
