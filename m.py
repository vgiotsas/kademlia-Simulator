import random
import math
import hashlib
import csv
#TODO remove se non serve
from node import Node
from coordinator import Coordinator
from nxGraph import NxGra
from graph import Graph

c = Coordinator(5,5)
ng = NxGra()
g = Graph()

c.main()
ng.main()
g.inDegreeBarplot()
g.outDegreeBarplot()