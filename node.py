import math
import time

class node:
    _active = True
    _ipAddress = None
    _udpPort = None
    _nodeId = None
    _numBit = None
    _bucketLength = 20
    _routingTable = [] #lista di liste con altezza che varia in base alla lunghezza dell'identificatore
    #ogni entry della routing table deve avere anche il timestamp del momento in cui il nodo è stato aggiunto
    #ogni nodo potrebbe essere rappresentato come dizionario, id, ip, port, timestamp 
    _storedValue = {}#dizionario per avere accesso diretto
    #non so se deve essere impostato come la routing table, così mi sembra più efficente

    def __init__(self, ipAddr, udpP, id, numBit):
        self._ipAddress = ipAddr
        self._udpPort = udpP
        self._nodeId = id
        self._numBit = numBit

        #inizializzo la rt
        self._routingTable = [None] * numBit
        for i in range(self._numBit):
            self._routingTable[i] = [None] * self._bucketLength


    def __createId(self, ip, port):
        return hash(ip + port)
    
    def getId(self):
        return self._nodeId

    def insertNode(self, id):
        timestamp = time.time()
        h = int(math.log2(id))
        i = 0
        minTimestamp = {'time': -1, 'pos': -1}
        while self._routingTable[h][i] is not None:
            if self._routingTable[h][i]['time'] > minTimestamp:
                minTimestamp['time'] = self._routingTable[h][i]['time']
                minTimestamp['pos'] = i
            i += 1

        if i < self._bucketLength:
            self._routingTable[h][i]['id'] = id
            self._routingTable[h][i]['time'] = timestamp
        else:
            if minTimestamp['time'] < timestamp:
                i = minTimestamp['pos']
                self._routingTable[h][i]['id'] = id
                self._routingTable[h][i]['time'] = timestamp


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

    def findNodeOptimized(self, id, k):
        closestNode = []
        temp = []
        h = int(math.log2(id))
        k = h
        while len(closestNode) < k and closestNode[k]['id'] != temp[k]['id']:
            for i in range(self._bucketLength):
                rtId = self._routingTable[k][i]['id']
                distance = self.distance(id, rtId)
                temp.append({'id': rtId, 'dist': distance})
            #sort
            #newlist = sorted(list_to_be_sorted, key=lambda k: k['name']) 
            if k <= h:
                k = k * -1 +1 
            else:
                k = k * -1 -1



    def distance(self, node1, node2):
        return node1 ^ node2
        
    def store(self, key, value):
        self._storedValue[key] = value 
        print('pair ' + key + ' '+ value + ' inserted')

    def findValue(self, key):
        return self._storedValue[key]
    
    def getNodeState(self):
        return self._active

    def changeState(self):
        self._active = not self._active