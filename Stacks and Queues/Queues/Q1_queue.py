class Stack():
    def __init__(self):
        self.list = []
    
    def __len__(self):
        return len(self.list)
    
    def push(self,item):
        self.list.append(item) 

    def pop(self):
        if len(self.list) == 0:
            return None
        else:
            return self.list.pop()
        
class QueueViaStacks:
    def __init__(self):
        self.inStack = Stack()
        self.outStack = Stack()

    def enqueue(self,item):
        self.inStack.push(item)
    
    def dequeue(self):
        while len(self.inStack):
            self.outStack.push(self.inStack.pop())
        result = self.outStack.pop()

        while len(self.outStack):
            self.inStack.push(self.outStack.pop())
        
        return result 





