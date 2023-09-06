from simpleQueue import *

q1 = simpleQueue()

def rotate():
    q_list = []
    q1.enqueue(10)
    q1.enqueue(20)
    q1.enqueue(30)
    q1.enqueue(40)
    q1.enqueue(50)
    q1.enqueue(60)

    for i in q1.data:
        q_list.append(i)
    for i in range(1,len(q_list)+1):
        q1.enqueue(q_list[-i])
    return q1.data

assert rotate() == ([10, 20, 30, 40, 50, 60, 60, 50, 40, 30, 20, 10])



