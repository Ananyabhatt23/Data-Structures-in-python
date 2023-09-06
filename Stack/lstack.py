class Lstack:

    def __init__(self):
        self.data = []
        self.count = 0
        self.size = 4


    def islimStackEmpty(self):
        return self.count == 0
    
    def limStackSize(self):
        return self.size
    
    def limStackPush(self,ele):
        if self.count == self.size:
            print('Error! Stack size is 4')
        else:
            self.data.append(ele)
            self.count += 1

    def limStackPop(self):
        if not self.islimStackEmpty():
            self.count -= 1
            return self.data.pop()
        else:
            return None
    
    def limStackPeek(self):
        if not self.islimStackEmpty():
            return self.data[-1]
        else:
            return None
        
    def printlinStack(self):
        if not self.islimStackEmpty():
            return self.data[0:]
        else:
            return None

