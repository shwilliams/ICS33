import random
from goody         import irange
from priorityqueue import PriorityQueue
from performance   import Performance


def setup(N):
    global pq
    alist = [i for i in range(N)]
    random.shuffle(alist)
    pq = PriorityQueue(alist)


def code(N):
    global pq
    for i in range(N):
        pq.remove()

        
for i in range(0,8):
    size = 10000*2**i
    p = Performance(lambda : code(10000), lambda:setup(size),5,'\n\nPriority Queue of size ' + str(size))
    p.evaluate()
    p.analyze()

        

        
