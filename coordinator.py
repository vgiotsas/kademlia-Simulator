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


#TODO Da mettere in utility

    def createIp(self):
        return socket.inet_ntoa(struct.pack('>I', random.randint(1, 0xffffffff)))
    
    def createPort(self):
        port = random.randint(0, 49151)
        return str(port)
    
    def createId(self, ip, port):
        return hash(ip + port)

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
        ip = self.createIp()
        port = self.createPort()
        id = self.createId(ip, port)
        self.nodeNumber = n
        self.bitsNumber = m
        no = Node(ip, port, id, m)
        self.nodeList.append({'id': no.getNodeId(), 'node': no})
        #self.nodeList.append(node(ip, port, id))

    def __createNode(self):
        nodeHashSet = set() #se nel set salvo ip+porta non c'è bisogno di istanziare classe, gli id coincidono
        for i in range(1, self.nodeNumber):
            ip = self.createIp()
            port = self.createPort()
            id = self.extractKBits(self.createId(ip,port), self.bitsNumber)
            if id not in nodeHashSet:
                node = Node(ip, port, id, self.bitsNumber)
                #self.nodeList.append(node(ip, port, id))
                #self.nodeList.append({'id': node.getNodeId(), 'node': node})
                self.notNetworkNode.append({'id': node.getNodeId(), 'node': node})
                nodeHashSet.add(id)