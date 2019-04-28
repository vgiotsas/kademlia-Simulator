import math
import time
import random

class Node:
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

    def __init__(self, ipAddr, udpP, idNode, numBit):
        self._ipAddress = ipAddr
        self._udpPort = udpP
        self._nodeId = idNode
        self._numBit = numBit

        #inizializzo la rt
        self._routingTable = [None] * numBit
        for i in range(self._numBit):
            self._routingTable[i] = [None] * self._bucketLength


    def __createId(self, ip, port):
        return hash(ip + port)
    
    
    def getNodeId(self):
        return self._nodeId


    def insertNode(self, id):
        timestamp = time.time()
        #FIXME l'hash genera anche interi negativi, farli restituire solo positivi ed eliminare i doppioni
        h = int(math.log2(id))
        i = 0
        minTimestamp = {'time': -1, 'pos': -1}
        while self._routingTable[h][i] is not None:
            if self._routingTable[h][i]['time'] > minTimestamp:
                minTimestamp['time'] = self._routingTable[h][i]['time']
                minTimestamp['pos'] = i
            i += 1

        if i < self._bucketLength:
            self._routingTable[h][i] = {}
            self._routingTable[h][i]['id'] = id
            self._routingTable[h][i]['time'] = timestamp
        else:
            if minTimestamp['time'] < timestamp:
                i = minTimestamp['pos']
                self._routingTable[h][i]['id'] = id
                self._routingTable[h][i]['time'] = timestamp


    def findNode(self, id, dim):
        closestNode = []
        temp = None
        h = int(math.log2(id))
        k = h
        move = 0 #mi serve per spostarmi su e giu nella rt
        counterRt = 0
        #finchè closestnode non è pieno, se è pieno controlla che non vengano aggiornati gli elementi
        # (più vicini vengono sostituiti a più lontani)
        #oppure finchè il numerro di 
        while len(closestNode) < dim and closestNode[k]['id'] != temp or counterRt < self._numBit:
            #uso una variabile "temporanea" per tenere l'ultimo elemento in memoria, se qualcosa cambia deve per forza cambiare anche 
            #l'ultimo, dato che ordinando la lista l'ultimo è il più distante
            temp = closestNode[k]['id']
            for i in range(self._bucketLength):#conosco il numero di elementi della bucket quindi scorro sugli elementi
                rtId = self._routingTable[k][i]['id']#prendo l'id in posizione i
                distance = self.distance(id, rtId)#prendo la distanza in posizione i
                if len(closestNode)  < dim:#se la lunghezza di closestnode è minore della lunghezza che deve essere restituita
                    closestNode.append({'id': rtId, 'dist': distance})#aggiungo il nodo (id distanza) alla lista
                else:#se invece la lista è piena
                    #ordino la lista per la distanza in modo da avere l'ultimo elemento come il più distante
                    closestNode = sorted(closestNode, key=lambda k: k['dist']) 
                    if closestNode[k]['dist'] > distance: #se l'ultimo elemento di closestnode è maggiore di quello attuale allora li scambio
                        #in quanto sto inserendo un nodo più vicino
                        closestNode[k]['id'] = rtId
                        closestNode[k]['dist'] = distance
            
            #ordino la lista in modo che se ci sono stati cambiamenti viene aggiornato l'ultimo elemento
            closestNode = sorted(closestNode, key=lambda k: k['dist']) 

            #questo serve per non scorrere tutta la bucketlist
            #parto dall'altezza h per poi controllare quello immediatamente sotto e sopra, per coi continuare sopra e sotto
            #finchè non riempo l'array o non vengono 
            if k <= h:
                move = move * -1 +1
                #Se supero la lnghezza della lista allora incremento move per poi decrementarlo
                if k+move <= self._numBit:
                    k += move
                else:
                    move = move * -1 -1
                    k += move
            else:
                move = move * -1 -1
                if k + move >= 0:
                    k += move
                else:
                    move = move * -1 +1
                    k += move

            counterRt += 1
        return closestNode


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
            randomId.append(random.getrandbits(pow(2, i)))
        return randomId
