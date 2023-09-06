class LinkedList:

    class _Node:
        def __init__(self, ele):
            self.ele = ele
            self.next = None

    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0
    
    def isEmpty(self):
        return self.count == 0
    
    def listCount(self):
        return self.count
    
    def append(self,ele):
        new_node = self._Node(ele)
        if not self.isEmpty():
            new_node.next = self.head
            self.head = new_node
        else:
            self.head = self.tail = new_node
        
        self.count += 1

    def find_max_marks(self):
        if not self.head:
            return None

        max_marks = self.head.ele  # Initialize max_marks with the first node's data
        current = self.head  # Start from the second node

        while current.next != None:
            if current.ele > max_marks:
                max_marks = current.ele
            current = current.next

        return max_marks

# Example usage:
marks_list = LinkedList()
marks_list.append(85)
marks_list.append(90)
marks_list.append(78)

max_marks = marks_list.find_max_marks()
print("Maximum Marks:", max_marks) 