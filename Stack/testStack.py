from simpleStack import *
    
s1 = Stack()

def testEmptyStack():
    assert s1.isstackEmpty() == True
    assert s1.StackLength() == 0

testEmptyStack()

def testPush():
    s1.stackPush(12)
    s1.stackPush(13)
    s1.stackPush(14)
    assert s1.isstackEmpty() == False
    assert s1.StackLength() == 3

testPush()

def testPeek():
    assert s1.stackPeek() == 14
    # print(s1.stackPeek())
testPeek()

def testPop():
    assert s1.stackPop() == 14
    # print(s1.stackPop())
testPop()

def testPrintEle():
    assert s1.printElements() == [12, 13]
testPrintEle()