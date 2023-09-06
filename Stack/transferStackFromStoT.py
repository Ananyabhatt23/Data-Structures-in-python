from simpleStack import *

S = Stack()
T = Stack()
S_duplicate = []

def transfer():
    S.stackPush(10)
    S.stackPush(20)
    S.stackPush(30)

    for i in S.data:
        S_duplicate.append(i)
        T.stackPush(i)
    print("Stack Elements in S is {}".format(S.data))
    print(f"The elements in T_Stack is {T.data}")

    if(S.data == T.data):
        print("Good, Keep it up :)")

    

    
transfer()





