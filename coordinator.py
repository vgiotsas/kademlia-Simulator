from node import node

class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


#Python3
class Coordinator(metaclass=Singleton):
    nodeNumber = None
    nodeList = []

#TODO Da mettere in utility

    def __createIp(self):
        #TODO random ip
        return 0
    
    def __createPort(self):
        #TODO random port
        return 0
    
    def __createId(self, ip, port):
        return hash(ip + port)

#----------
    
    def __init__(self, n):
        #devo generare un nuovo nodo
        ip = self.createIp()
        port = self.createPort()
        self.nodeList.append(node(ip, port, id))
        self.nodeNumber = n

    def __createNode(self):
        nodeHashSet = set() #se nel set salvo ip+porta non c'è bisogno di istanziare classe, gli id coincidono
        for i in range(1, self.nodeNumber-1):
            ip = self.__createIp()
            port = self.__createPort()
            id = self.__createId(ip,port)
            if id not in nodeHashSet:
                self.nodeList.append(node(ip, port, id))
                nodeHashSet.add(id)

    
