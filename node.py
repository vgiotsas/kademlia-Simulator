import math
import time
import random
#TODO nel main inserire che i parametri vengono scelti dall'utente
class Node:
    _active = True #true se il nodo è attivo, valore restituito quando viene eseguito il ping al nodo
    _ipAddress = None
    _udpPort = None
    _nodeId = None
    _numBit = None
    dimensionOfReturn = 50
    _bucketLength = 20
    _routingTable = None #lista di liste con altezza che varia in base alla lunghezza dell'identificatore
    #ogni entry della routing table deve avere anche il timestamp del momento in cui il nodo è stato aggiunto
    _storedValue = {}

    def __init__(self, ipAddr, udpP, idNode, numBit):
        """
        Costruttore, prende in input ip, port e numero di bit
        """
        self._ipAddress = ipAddr
        self._udpPort = udpP
        self._nodeId = idNode
        self._numBit = numBit
        #inizializzo la routing table come lista di liste
        self._routingTable = [[] for i in range(numBit)]

    def getNodeId(self):
        """
        Restituisce l'id del nodo
        """
        return self._nodeId

    def searchEl(self, list, el):
        """
        controlla se l'id è già presente nella routing table
        """
        exist = False
        for i in list:
            if i is not None:
                if i['id'] == el:
                    exist = True
        return exist

    def insertNode(self, id, ip, port):
        """
        Inserisce il nodo nella routing table
        """
        timestamp = time.time() #prende il timestamp necessario per ordinare i nodi all'interno della kbucket
        h = int(math.log2(id)) #con il logaritmo trovo a che altezza inserire l'elemento
        if not self.searchEl(self._routingTable[h], id) and id != self._nodeId:
            self._routingTable[h].append({'id': id, 'time': timestamp, 'ip': ip, 'port': port}) #inserisco l'elemento nella bucket
            self._routingTable[h] = sorted(self._routingTable[h], key=lambda k: k['time'])  #ordino gli elementi nella bucket rispetto al tempo
            self._routingTable[h] = self._routingTable[h][:self._bucketLength] #restituisco la bucket di k elementi

    def findNode(self, id):
        """
        Restituisce i K elementi più vicini ad id
        """
        closestNode = [] #lista in cui vengono aggiunti i k nodi
        for i in self._routingTable:
            for bucket in i:
                if bucket is not None:
                    rtId = bucket['id']
                    dist = self.distance(id, rtId) #calcolo la distanza tra l'id e quello trovato nella routing table
                    ip = bucket['ip']
                    port = bucket['port']
                    closestNode.append({'id': rtId, 'dist': dist, 'ip': ip, 'port': port}) 
                    closestNode = sorted(closestNode, key=lambda k: k['dist'])  #ordino gli elementi nella bucket rispetto alla distanza
        return closestNode[:self.dimensionOfReturn]



    def distance(self, node1, node2):
        """
        Restituisce la distanza tra due id
        """
        return node1 ^ node2


    def store(self, key, value):
        """
        Salva una coppia chiave valore
        """
        self._storedValue[key] = value 
        print('pair ' + key + ' '+ value + ' inserted')


    def findValue(self, key):
        """
        restituisce il valore di una certa chiave salvata nel nodo
        """
        return self._storedValue[key]


    def ping(self):
        """
        Restituisce lo stato del nodo, se attivo o no
        """
        return self._active


    def changeState(self):
        """
        modifica lo stato del nodo
        """
        self._active = not self._active
    
    def createRandomId(self):
        randomId = []
        for i in range(0, self._numBit):
            randomId.append(pow(2, i))
        return randomId