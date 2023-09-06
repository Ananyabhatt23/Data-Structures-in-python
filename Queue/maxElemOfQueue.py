from simpleQueue import *

q1 = simpleQueue()

q1.enqueue(10)
q1.enqueue(20)
q1.enqueue(30)

def findMax():
    maxElem = q1.data[0]
    for i in q1.data:
        if i > maxElem:
            maxElem = i
    return maxElem

assert findMax() == (30)



