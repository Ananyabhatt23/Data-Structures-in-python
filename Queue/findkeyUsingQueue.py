from simpleStack import *;
from simpleQueue import*;

#Program to check if key is present in the given stack using one stack and queue
s1 = Stack()
q1 = simpleQueue()

def findKey(key):
    
    s1.stackPush(10)
    s1.stackPush(20)
    s1.stackPush(30)
    s1.stackPush(40)
    f=0
    while(s1.count>0):
        ele=s1.stackPop()
        q1.enqueue(ele)
        if(key==ele):
            f=1
    copyQueueToStack(s1,q1)
    copyStackToQueue(s1,q1)
    copyQueueToStack(s1,q1)
    return f==1

def copyQueueToStack(s1,q1):
    while(q1.count>0):
        s1.stackPush(q1.dequeue())

def copyStackToQueue(s1,q1):
    while(s1.count>0):
        q1.enqueue(s1.stackPop())

assert(findKey(20)==True)
assert(findKey(200)==False)
