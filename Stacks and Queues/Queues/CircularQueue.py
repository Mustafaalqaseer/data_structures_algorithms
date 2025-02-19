
class Queue:
    def __init__(self,capacity):
        self.capacity = capacity
        self.items = [None] * capacity
        self.start = -1
        self.back = -1

    def __str__(self):
        values = [ str(element) for element in self.items()]
        return ' '.join(values)
    
    def isFull(self):
        if self.start == 0 and (self.back + 1) == self.capacity:
            return True
        elif (self.back+1) == self.start:
            return True
        return False 
    
    def isEmpty(self):
        if self.back == -1:
            return True
        return False
    
    def enqueue(self,val):
        if self.isFull():
            return "queue is full"
        
        if self.back + 1 == self.size:
            self.back = 0
        else:
            self.back +=1
            if self.start == -1:
                self.start = 0
        self.items[self.back] = val
        return " element is inserted to end of queue"
    
    def dequeue(self):
        if self.isEmpty():
            return "no element in queue"
        else:
            firstElement = self.items[self.start]
            if self.start == self.back:
                self.start = -1
                self.back = -1
            elif self.start == self.capacity:
                self.start = 0
            else:
                self.start +=1
            self.items[self.start] = None
            return firstElement
        
    def peek(self):
        if self.isEmpty():
            return "queue is empty so no peek"
        else:
            return self.items[self.start]
        
    def delete(self):
        self.items = [None] * self.capacity
        self.start = self.back = -1
            

    

    

            

        
    
    



    