class Stack:

    def __init__(self):
        self.count = 0
        self.data = []

    def isstackEmpty(self):
        return self.count == 0
    
    def StackLength(self):
        return self.count
    
    def stackPush(self,ele):
        self.data.append(ele)
        self.count += 1
    
    def stackPop(self):
        if not self.isstackEmpty():
            self.count -= 1
            return self.data.pop()
        else:
            return None
        
    def stackPeek(self):
        if not self.isstackEmpty():
            return self.data[-1]
        else:
            return None
    
    def printElements(self):
        if not self.isstackEmpty():
            return self.data[0:]
        else:
            return None