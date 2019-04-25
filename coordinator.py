import random
import socket
import struct
from node import node

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

#TODO Da mettere in utility

    def createIp(self):
        #TODO test
        return socket.inet_ntoa(struct.pack('>I', random.randint(1, 0xffffffff)))
    
    def createPort(self):
        #TODO test
        return random.randint(0, 49151)
    
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
        print (int(kBitSubStr,2)) 
        return int(kBitSubStr,2)

#----------
    
    def __init__(self, n, m):
        #devo generare un nuovo nodo
        ip = self.createIp()
        port = self.createPort()
        self.nodeList.append(node(ip, port, id))
        self.nodeNumber = n
        self.bitsNumber = m

    def __createNode(self):
        nodeHashSet = set() #se nel set salvo ip+porta non c'è bisogno di istanziare classe, gli id coincidono
        for i in range(1, self.nodeNumber-1):
            ip = self.createIp()
            port = self.createPort()
            id = self.extractKBits(self.createId(ip,port), self.bitsNumber)
            if id not in nodeHashSet:
                self.nodeList.append(node(ip, port, id))
                nodeHashSet.add(id)