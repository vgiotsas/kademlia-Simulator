import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
import csv

def barchart():
    objects = ('Python', 'C++', 'Java', 'Perl', 'Scala', 'Lisp')
    y_pos = np.arange(len(objects))
    performance = [10,8,6,4,2,1]

    plt.bar(y_pos, performance, align='center', alpha=0.5)
    plt.xticks(y_pos, objects)
    plt.ylabel('Usage')
    plt.title('Programming language usage')

    plt.show()
#------------------

def barchartConfronto():
    # data to plot
    n_groups = 4
    means_frank = (90, 55, 40, 65)
    means_guido = (85, 62, 54, 20)

    # create plot
    fig, ax = plt.subplots()
    index = np.arange(n_groups)
    bar_width = 0.35
    opacity = 0.8

    rects1 = plt.bar(index, means_frank, bar_width,
    alpha=opacity,
    color='b',
    label='Frank')

    rects2 = plt.bar(index + bar_width, means_guido, bar_width,
    alpha=opacity,
    color='g',
    label='Guido')

    plt.xlabel('Person')
    plt.ylabel('Scores')
    plt.title('Scores by person')
    plt.xticks(index + bar_width, ('A', 'B', 'C', 'D'))
    plt.legend()

    plt.tight_layout()
    plt.show()

with open('edge.csv', 'r') as f:
    reader = csv.reader(f)
    edge = list(reader)

    ed = set()
    for i in edge:
        tup = ()
        for l in range(0, len(i), 2):
            tup = (int(i[l]), int(i[l+1]))
            ed.add(tup)

    with open('node.csv', 'r') as f:
        reader = csv.reader(f)
        node = list(reader)
    
    inOut = []
    for i in node[0]:
        inOut.append({'id': i, 'in': 0, 'out': 0})
    for i in ed:
        for j in inOut:
            if int(j['id']) == int(i[0]):
                j['out'] += 1
            elif int(j['id']) == int(i[1]):
                j['in'] += 1

    print(inOut)