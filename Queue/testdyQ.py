from dynamicQ import *

obj = dynamicQueue()

def testEmpty():
    assert obj.isQEmpty == True
    assert obj.count == 0

def testEnqueue():
    assert obj.enqueue(10) == 1
    assert obj.enqueue(20) == 2
    assert obj.dequeue() == 10
    assert obj.enqueue(30) == 2
    assert obj.enqueue(40) == 3

testEnqueue()

print(obj.printQ())