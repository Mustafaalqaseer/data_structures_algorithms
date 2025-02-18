class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None


class Stack:
    def __init__(self):
        self.linkedlist = LinkedList()

    def isEmpty(self):
       if self.linkedlist.head is None:
           return True
       else: return False

    def delete(self):
        self.linkedlist.head = None

    def push(self,val):
        new_node = Node(val)
        new_node.next = self.linkedlist.head
        self.linkedlist.head = new_node

    def pop(self):
        if self.isEmpty() is None:
            return "cannot pop from an empty linkedlist"
        else:
            popped_node_value = self.linkedlist.head.val
            self.linkedlist.head = self.linkedlist.head.next
        return popped_node_value

    def peek(self):
        if self.isEmpty() is None:
            return " empty linked list"
        else:
            return self.linkedlist.head.val






