class simpleQueue:
    def __init__(self):
        self.data = []
        self.count = 0

    def getElem(self):
        return self.count
    
    def isQEmpty(self):
        return self.count == 0
    
    def enqueue(self,ele):
        self.data.append(ele)
        self.count+=1

    def dequeue(self):
        if not self.isQEmpty():
            self.count-=1
            return self.data.pop(0)
        else:
            return None
    
    def peekEle(self):
        if not self.isQEmpty():
            return self.data[0]
        
    def printElem(self):
        if not self.isQEmpty():
            return self.data


        