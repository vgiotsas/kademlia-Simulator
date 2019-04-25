import random
import hashlib
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
print(random.getrandbits(1))