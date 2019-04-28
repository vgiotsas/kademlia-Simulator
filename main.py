import random
import hashlib
from node import Node
from coordinator import Coordinator
"""
s="192.168.10.190"
c="ygiuguguiguiguiguigiugiugiugiguggiugiguiguiguguggiggiugiugiugiuguigiugiuguigiugiu"
hashcodes=hashlib.md5((s).encode('utf-8')).hexdigest()
hashcodec=hashlib.md5((c).encode('utf-8')).hexdigest()
print(bin(int(hashcodes,16)))
print(bin(int(hashcodec,16)))
bi = bin(int(hashcodes,16) ^ int(hashcodec,16))
print('{0:08b}'.format(int(hashcodes,16) ^ int(hashcodec,16)))
"""
#print(random.getrandbits(1))
c = Coordinator(5,5)
ip = c.createIp()
port = c.createPort()
c._Coordinator__createNode()
print(c.nodeList)
#scelgo il bootstrap a random da nodelist
bootstrap = c.nodeList[random.randint(0, len(c.nodeList) - 1)]
newNode = c.notNetworkNode[random.randint(0, len(c.notNetworkNode) - 1)]

bootstrap['node'].insertNode(newNode['id'])
newNode['node'].insertNode(bootstrap['id'])
print(bootstrap['node']._routingTable)
print(newNode['node']._routingTable)

randomId = newNode['node'].createRandomId()
for i in randomId:
    pass