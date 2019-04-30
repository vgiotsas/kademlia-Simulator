import math
import time
import random

class Node:
    _active = True
    _ipAddress = None
    _udpPort = None
    _nodeId = None
    _numBit = None
    #TODO riporta a 20
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
        """
        i = 0
        minTimestamp = {'time': -1, 'pos': -1}
        while self._routingTable[h-1][i] is not None:
            if self._routingTable[h-1][i]['time'] > minTimestamp['time']:
                minTimestamp = {'time': self._routingTable[h][i]['time'], 'pos': i}
                #minTimestamp['time'] = self._routingTable[h][i]['time']
                #minTimestamp['pos'] = i
            i += 1

        if i < self._bucketLength and not self.searchEl(self._routingTable[h], id) and id != self._nodeId:
            self._routingTable[h].append({'id': id, 'time': timestamp})
            insert = True
            #self._routingTable[h][i] = {'id': id, 'time': timestamp}
            #self._routingTable[h][i]['id'] = id
            #self._routingTable[h][i]['time'] = timestamp
        elif i == self._bucketLength:
            if minTimestamp['time'] < timestamp and id != self._nodeId:
                i = minTimestamp['pos']
                self._routingTable[h][i]['id'] = id
                self._routingTable[h][i]['time'] = timestamp
                insert = True
        return insert
        """

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

"""
    def findNode(self, id, dim):
        #dim sarebbero i k elementi restituibili da findnode
        #FIXME controllare la dimensione di k
        closestNode = [{'id': 1, 'dist': 10000000000000000}]
        temp = None
        now = -1
        print("l'id è "+str(id))
        h = int(math.log2(id))
        k = h
        move = 0 #mi serve per spostarmi su e giu nella rt
        counterRt = 0
        #finchè closestnode non è pieno, se è pieno controlla che non vengano aggiornati gli elementi
        # (più vicini vengono sostituiti a più lontani)
        #oppure finchè il numero di 
        #FIXME l'errore è out of range su questa riga
        #NOTE Non so so il k-1 è giusto, controllare. perchè il problema probabilmentte è su id
        #while len(closestNode) < dim and closestNode[k]['id'] != temp or counterRt < self._numBit:
        while len(closestNode) < dim and now != temp or counterRt < self._numBit:
            #uso una variabile "temporanea" per tenere l'ultimo elemento in memoria, se qualcosa cambia deve per forza cambiare anche 
            #l'ultimo, dato che ordinando la lista l'ultimo è il più distante
            print("k è "+str(k))
            print(self._routingTable)
            for i in self._routingTable[k]:#conosco il numero di elementi della bucket quindi scorro sugli elementi
                print("ancora non so se è vuoto")
                print(i)
                if i is not None:
                    print("qui non è vuoto")
                    rtId = i['id']#prendo l'id in posizione i
                    distance = self.distance(id, rtId)#prendo la distanza in posizione i
                    print("la distanza è "+ str(distance))
                    if len(closestNode)  < dim and distance > 0:#se la lunghezza di closestnode è minore della lunghezza che deve essere restituita
                        print("inserisci sto coso")
                        closestNode.append({'id': rtId, 'dist': distance})#aggiungo il nodo (id distanza) alla lista
                    else:#se invece la lista è piena
                        #ordino la lista per la distanza in modo da avere l'ultimo elemento come il più distante
                        closestNode = sorted(closestNode, key=lambda k: k['dist']) 
                        if closestNode[k]['dist'] > distance and distance > 0: #se l'ultimo elemento di closestnode è maggiore di quello attuale allora li scambio
                            #in quanto sto inserendo un nodo più vicino
                            closestNode[k] = {}
                            closestNode[k]['id'] = rtId
                            closestNode[k]['dist'] = distance
            
            #ordino la lista in modo che se ci sono stati cambiamenti viene aggiornato l'ultimo elemento
            closestNode = sorted(closestNode, key=lambda k: k['dist']) 
            #questo serve per non scorrere tutta la bucketlist
            #parto dall'altezza h per poi controllare quello immediatamente sotto e sopra, per coi continuare sopra e sotto
            #finchè non riempo l'array o non vengono 
            temp = closestNode[len(closestNode) - 1]['id']
            if k <= h:
                #Se supero la lnghezza della lista allora incremento move per poi decrementarlo
                if k + move * -1 +1<= self._numBit -1:
                    #k += move
                    move = move * -1 +1
                    print("minore di closest")
                    
                else:
                    move = move * -1 -1
                    #k += move
            else:
                
                if k + move * -1 -1 >= 0:
                    #k += move
                    move = move * -1 -1
                    
                else:
                    print("dovrei trovarmi qui dentro in quanto minore di 0")
                    move = move * -1 +1
                    #k += move
            now = closestNode[len(closestNode) - 1]['id']
            k += move
            counterRt += 1
        return closestNode
"""