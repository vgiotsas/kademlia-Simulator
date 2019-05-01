import random
import socket
import struct
from node import Node
from utility import writeNodeCsv, writeEdgeCsv, createIp, createId, createPort, writeSnapshotCsv

class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class Coordinator(metaclass=Singleton): #definisco la classe coordinator come singleton
    nodeNumber = None
    bitsNumber = None
    nodeList = []
    notNetworkNode = [] #lista di nodi non ancora entrati nella rete
    nodeHashSet = set() #con questo set faccio in modo di non avere collisione tra gli id

    def __init__(self, n, m):
        self.nodeNumber = n
        self.bitsNumber = m
        ip = createIp()
        port = createPort()
        id = createId(ip, port, m)
        self.nodeHashSet.add(id)
        no = Node(ip, port, id, m) #creo un nuovo nodo e lo aggiungo alla rete, nel primo passaggio sarà il nodo bootstrap
        self.nodeList.append({'id': no.getNodeId(), 'node': no, 'ip': no._ipAddress, 'port': no._udpPort})

    def __createNode(self):
        """
        Creo il numero di nodi richiesto dall'utente
        """
        while len(self.nodeHashSet) < self.nodeNumber:
            ip = createIp()
            port = createPort()
            id = createId(ip,port, self.bitsNumber)
            if id not in self.nodeHashSet: #controllo se l'id è già presente
                node = Node(ip, port, id, self.bitsNumber)
                self.notNetworkNode.append({'id': node.getNodeId(), 'node': node, 'ip': node._ipAddress, 'port': node._udpPort})#inizialmente lo aggiungo alla lista di nodi non ancora nella rete
                self.nodeHashSet.add(id) #lo aggiungo al set così da non poterlo riutilizzare

    def main(self):
        """
        funzione in cui viene effettivamente eseguita la simulazione
        """
        dimensionOfReturn = 50
        #sia c che counterSnapshot sono 2 contatori necessari per creare gli snapshot
        counterSnapshot = 1
        c = 1
        self.__createNode() #
        while len(self.notNetworkNode) > 0: #itero finchè tutti i nodi non siano nella rete
            if c %50 == 0: #ogni n passaggi salvo le informazioni in un csv, che poi utilizzer per i grafici
                writeSnapshotCsv(self.nodeList, counterSnapshot)
                counterSnapshot += 1

            randBts = random.randint(0, len(self.nodeList) - 1) #
            bootstrap = self.nodeList[randBts] #il bootstrap è un nodo preso a random dalla lista dei nodi nella rete
            randNn = random.randint(0, len(self.notNetworkNode) - 1)
            newNode = self.notNetworkNode[randNn] #il nodo entrante è un nodo preso a random dalla lista dei nodi non ancora nella rete
            
            #aggiungo il nodo entrante nella lista dei nodi della rete e lo elimino da quella dei nodi non ancora entrati
            self.nodeList.append(self.notNetworkNode[randNn]) 
            del self.notNetworkNode[randNn]
            
            print(bootstrap)
            print(newNode)
            kNode = []
            prev = None
            counter = 3

            #inserisco il bootstrap node nella routing table del nodo entrante e viceversa
            bootstrap['node'].insertNode(newNode['id'], newNode['ip'], newNode['port']) 
            newNode['node'].insertNode(bootstrap['id'], bootstrap['ip'], bootstrap['port'])

            #creo una serie di id a random, un id per ogni elemento della routing table
            randomId = newNode['node'].createRandomId()
            for i in randomId: #itero per ogni id random
                while len(kNode) < dimensionOfReturn: # finchè la bucket non è piena oppure finchè non vengono restituite informazioni utili
                    if not kNode:
                        prev = 0
                    else:
                        prev = kNode[len(kNode)-1]['id']
                    kNode = kNode + bootstrap['node'].findNode(i) #eseguo la findnode sul bootstrap node
                    #prendo i primi n elementi, di default ne vengono presi 3 e eseguo la findnode con lo stesso id su quei nodi
                    for j in range(counter-3, counter): 
                        for n in self.nodeList:
                            if kNode[j]:
                                if n['id'] == kNode[j]['id']:
                                    kNode = kNode + n['node'].findNode(i)
                    #ordino la lista di k nodi restituita dalla findnode
                    kNode = sorted(kNode, key=lambda k: k['dist'])
                    if kNode[len(kNode) -1] == prev: 
                        break
                    counter += 3
                if kNode is not None:
                    for n in kNode:
                        newNode['node'].insertNode(n['id'], n['ip'], n['port'])#inserisco i k nodi nella routing table
            c += 1

        for i in self.nodeList:
            print(i['id'])
            print(i['node']._routingTable)
            print("--------------")
        
        writeNodeCsv(self.nodeList) #inserisce i nodi nel csv
        writeEdgeCsv(self.nodeList) #inserisce li archi nel csv