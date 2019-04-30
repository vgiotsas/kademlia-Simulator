x = [[] for i in range(3)]
print(x)
"""
l = []
a = []
for i in range(0,3):
    a[i].append(l)

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