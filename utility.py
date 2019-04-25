def createIp(self):
    #TODO random ip
    return 0

def createPort(self):
    #TODO random port
    return 0

def createId(self, ip, port):
    return hash(ip + port)

def extractKBits(self, num, k, p = 0):
    binary = bin(num) 

    # remove first two characters 
    binary = binary[2:] 
    end = len(binary) - p 
    start = end - k + 1
    # extract k  bit sub-string 
    kBitSubStr = binary[start : end+1] 
    # convert extracted sub-string into decimal again 
    print (int(kBitSubStr,2)) 
    return int(kBitSubStr,2)