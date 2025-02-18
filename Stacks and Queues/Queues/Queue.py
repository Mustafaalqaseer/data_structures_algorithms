class Queue:
    def __init__(self):
        self.items = []

    def __str__(self):
        values = [str(x) for x in self.items]
        return ' '.join(values)

    def isEmpty(self):
        if self.items == []:
            return True
        else:
            return False

    def enqueue(self,val):
        self.items.append(val)

    def dequeue(self):
        if self.isEmpty():
            return "queue is empty connot do operation"
        else:
            self.items.pop(0)

    def peek(self):
        if self.isEmpty():
            return "queue is empty/can't peek"
        else:
            return self.items[0]

    def delete(self):
        self.items = None


myQ = Queue()
myQ.enqueue(10)
myQ.enqueue(20)
myQ.enqueue(30)
myQ.dequeue()
myQ.dequeue()
print(myQ)






