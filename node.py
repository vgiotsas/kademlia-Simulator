import math
import time
import random
#TODO nel main inserire che i parametri vengono scelti dall'utente
class Node:
    _active = True
    _ipAddress = None
    _udpPort = None
    _nodeId = None
    _numBit = None
    dimensionOfReturn = 50
    _bucketLength = 10
    _routingTable = None #lista di liste con altezza che varia in base alla lunghezza dell'identificatore
    #ogni entry della routing table deve avere anche il timestamp del momento in cui il nodo è stato aggiunto
    #ogni nodo potrebbe essere rappresentato come dizionario, id, ip, port, timestamp 
    _storedValue = {}#dizionario per avere accesso diretto
    #non so se deve essere impostato come la routing table, così mi sembra più efficente

    def __init__(self, ipAddr, udpP, idNode, numBit):
        self._ipAddress = ipAddr
        self._udpPort = udpP
        self._nodeId = idNode
        self._numBit = numBit

        #inizializzo la rt
        #self._routingTable = [None] * numBit
        self._routingTable = [[] for i in range(numBit)]
            #self._routingTable[i] = [None] * self._bucketLength

    def getNodeId(self):
        return self._nodeId

    def searchEl(self, list, el):
        exist = False
        for i in list:
            if i is not None:
                if i['id'] == el:
                    exist = True
        return exist

    def insertNode(self, id):
        insert = None
        timestamp = time.time()
        h = int(math.log2(id))
        #faccio sempre append poi ordino rispetto al tempo, poi taglio per la lunghezza 
        if not self.searchEl(self._routingTable[h], id) and id != self._nodeId:
            self._routingTable[h].append({'id': id, 'time': timestamp})
            self._routingTable[h] = sorted(self._routingTable[h], key=lambda k: k['time']) 
            self._routingTable[h] = self._routingTable[h][:self._bucketLength]

    def findNode(self, id):
        closestNode = []
        for i in self._routingTable:
            for bucket in i:
                if bucket is not None:
                    rtId = bucket['id']
                    dist = self.distance(id, rtId)
                    closestNode.append({'id': rtId, 'dist': dist})
                    """
                    if len(closestNode) < self.dimensionOfReturn and dist > 0 and rtId != id:
                        closestNode.append({'id': rtId, 'dist': dist})
                    else:
                        if dist > 0 and rtId != id:
                            closestNode = sorted(closestNode, key=lambda k: k['dist']) 
                            if closestNode[self.dimensionOfReturn - 1]['dist'] > dist:
                                closestNode[self.dimensionOfReturn - 1]['id'] = rtId  
                                closestNode[self.dimensionOfReturn - 1]['dist'] = dist  
                    """
        return closestNode[:self.dimensionOfReturn]



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
    
    def createRandomId(self):
        randomId = []
        for i in range(0, self._numBit):
            randomId.append(pow(2, i))
        return randomId