from simpleQueue import *

obj = simpleQueue()

def testEmptyQ():
    assert obj.isQEmpty() == True
    assert obj.count == 0
testEmptyQ()

def testPutEle():
    obj.enqueue(23)
    obj.enqueue(24)
    obj.enqueue(25)
    assert obj.count == 3
    assert obj.data == [23,24,25]
testPutEle()

def testdelEle():
    assert obj.dequeue() == 23
testdelEle()

def testPeekEle():
    assert obj.peekEle() == 24
testPeekEle()

def testPrintEle():
    assert obj.printElem() == [24,25]
testPrintEle()