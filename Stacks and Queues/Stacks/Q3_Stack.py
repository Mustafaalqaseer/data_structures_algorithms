class PlateStack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.stacks = []

    def __str__(self):
        return str(self.stacks)


    def push(self,item):
        if len(self.stacks) > 0 and len(self.stacks[-1]) < self.capacity:
            self.stacks[-1].append(item)
        else:
            self.stacks.append([item])

    def pop(self):
        pass





plateStack = PlateStack(2)

plateStack.push(1)
plateStack.push(2)
plateStack.push(3)
print(plateStack)