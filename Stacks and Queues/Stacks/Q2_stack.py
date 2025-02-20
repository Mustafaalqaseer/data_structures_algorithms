# design a stack that has a get min method in O(1)


class Node:
    def __init__(self,val = None, next = None):
        self.val = val
        self.next = next


class Stack:
    def __init__(self):
        self.top = self.minNode = None

    def min(self):
        if not self.minNode.val:
            return None
        return self.minNode.val
    
    def push(self,item):
        if self.minNode and (self.minNode.val < item):
            self.minNode = Node(val = self.minNode.val, next = self.minNode)
        else:
            self.minNode = Node(val = item, next = self.minNode) 
        self.top = Node(val = item, next=self.top)

    def pop(self):
        if self.top == None:
            return "stack is empty"
        else:
            self.minNode = self.minNode.next
            popped_node = self.top.val
            self.top = self.top.next
        return popped_node



    



