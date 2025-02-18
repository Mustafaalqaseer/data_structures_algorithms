class Stack:
    def __init__(self, maxSize):
        self.list = []
        self.maxSize =maxSize

    def __str__(self):
        values = [str(x) for x in reversed(self.list)]
        return '\n'.join(values)

    def isEmpty(self):
        if self.list == []:
            return True
        else: return False

    def isFull(self):
        if len(self.list) == self.maxSize:
            return True
        else:
            return False

    def push(self,val):
        if self.isFull():
            return "stack is full"
        else:
            self.list.append(val)

    def peek(self):
        if self.isEmpty():
            return "stack is empty"
        else:
            return self.list[len(self.list)-1]

    def delete(self):
        self.list = None

limStack = Stack(3)

limStack.push(10)
limStack.push(20)
limStack.push(30)
limStack.push(40)
print(limStack)
print(limStack.peek())



