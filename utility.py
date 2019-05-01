import random
import socket
import struct
import csv

def createIp():
    return socket.inet_ntoa(struct.pack('>I', random.randint(1, 0xffffffff)))

def createPort():
    port = random.randint(0, 49151)
    return str(port)

def createId(ip, port, bitsNumber):
    id = extractKBits(int(hash(ip + port)), bitsNumber)
    if id == 0:
        id = id + 1
    if id < 0 : 
        id *= -1
    return id

def extractKBits(num, k, p = 0):
    binary = bin(num) 
    # remove first two characters 
    binary = binary[2:] 
    end = len(binary) - p 
    start = end - k + 1
    # extract k  bit sub-string 
    kBitSubStr = binary[start : end+1] 
    # convert extracted sub-string into decimal again
    return int(kBitSubStr,2)

def writeEdgeCsv(nodeList):
    with open('edge.csv', mode='w') as node_file:
        node_writer = csv.writer(node_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for i in nodeList:
            if i is not None:
                for n in i['node']._routingTable:
                    listNodeEdge = []
                    for k in n:
                        if k is not None:
                            listNodeEdge.append(i['id'])
                            listNodeEdge.append(k['id'])
                            node_writer.writerow(listNodeEdge)


def writeNodeCsv(nodeList):
    with open('node.csv', mode='w') as node_file:
        node_writer = csv.writer(node_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        new_list = [i["id"] for i in nodeList]
        node_writer.writerow(new_list)