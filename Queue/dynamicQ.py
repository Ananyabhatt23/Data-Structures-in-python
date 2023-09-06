class dynamicQueue:
    def __init__(self):
        self.data = []
        self.count = 0
        self.size = 2

    def isQEmpty(self):
        return self.count == 0
    
    def getElemCount(self):
        return self.count
    
    def enqueue(self,ele):
        if self.count == self.size:
            print("Queue is filled with "+str(self.size)+" elements "+str(self.data))
            inputval = int(input("Enter how many extras: "))
            self.resize(inputval)
            self.data.append(ele)
            self.count += 1
            return self.count
        else:
            self.data.append(ele)
            self.count+=1
            return self.count

    def resize(self,inputval):
        self.size = self.size + inputval

    def dequeue(self):
        self.count-=1
        return self.data.pop(0)

    def printQ(self):
        return self.data