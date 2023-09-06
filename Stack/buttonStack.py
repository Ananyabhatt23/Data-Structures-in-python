from simpleStack import *
import webbrowser

S1 = Stack()
S1.stackPush('https://www.youtube.com/watch?v=v3ctF5rrWbs')
S1.stackPush('https://www.youtube.com/watch?v=fZLLqapzxRQ')
S1.stackPush('https://www.youtube.com/')


def buttons():
    mainBut = input("Going to youtube?")
    if mainBut == 'Yes':
        webbrowser.open(S1.stackPop())
    
    forwardBut = input("Forward?")
    if forwardBut == 'F':
        webbrowser.open(S1.stackPop())

    backwardBut = input("Forward?")
    if backwardBut == 'F':
        webbrowser.open(S1.stackPop())

buttons()






