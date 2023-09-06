from lstack import *

ls1 = Lstack()

def testLstatckEmpty():
    assert ls1.islimStackEmpty() == True

testLstatckEmpty()

def getElemSize():
    assert ls1.limStackSize() == 4

getElemSize()

def testLstackPush():
    ls1.limStackPush(10)
    ls1.limStackPush(11)
    ls1.limStackPush(12)
    assert ls1.count == 3
    # print(ls1.count,ls1.data)

testLstackPush()

def testpop():
    assert ls1.limStackPop() == 12
testpop()

def testpeek():
    assert ls1.limStackPeek() == 11
testpeek()

def printEle():
    assert ls1.printlinStack() == [10,11] 
printEle()




