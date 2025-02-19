
# use a single list to implement three stacks

class MultiStack:
    def __init__(self,stackSize):
        self.numberStacks = 3
        self.custList = [0] * self.stackSize
