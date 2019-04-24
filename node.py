class node:
    _active = True
    _ipAddress = None
    _udpPort = None
    _nodeId = None
    _routingTable = [] #lista di liste con altezza che varia in base alla lunghezza dell'identificatore
    #ogni entry della routing table deve avere anche il timestamp del momento in cui il nodo è stato aggiunto
    #ogni nodo potrebbe essere rappresentato come dizionario, id, ip, port, timestamp 
    _storedValue = {}#dizionario per avere accesso diretto
    #non so se deve essere impostato come la routing table, così mi sembra più efficente

    def __init__(self, ipAddr, udpP, id):
        self._ipAddress = ipAddr
        self._udpPort = udpP
        self._nodeId = id
        #self._nodeId = self.__createId(ipAddr, udpP)

    def __createId(self, ip, port):
        return hash(ip + port)
    
    def getId(self):
        return self._nodeId

    def findNode(self, id, k):
        #secondo me deve scorrere tutta la routing table per poi restituire i k più vicini
        closestNode = []
        for rt in self._routingTable:
            for buck in rt:
                self.distance(id, buck['id'])
                #inserisco finchè non ho raggiunto k
                #ordino la lista 
                #sostituisco gli elementi presenti con quelli aventi distanza minore
                #in fine restituisco una lista dei k dizionari (nodi) più vicini al nodo passato alla findNode
        #potrei anche controllare nel bucket "giusto" considerando l'id e l'altezza della kbucket poi muovermi +1/-1 rispetto a quella.
        #dovrebbe abbassarsi la complessità

    def distance(self, node1, node2):
        return node1 ^ node2
        
    def store(self, key, value):
        self._storedValue[key] = value 
        print('coppia ' + key + ' '+ value + ' correttamente inserita')

    def findValue(self, key):
        return self._storedValue[key]
    
    def getNodeState(self):
        return self._active

    def changeState(self):
        self._active = not self._active