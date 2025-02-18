class Node():
    def __init__(self, val):
        self.val = val
        self.next = self.prev = None

class CircularDoubleLL():
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def prepend(self,val):
        new_node = Node(val)
        if self.length == 0:
            self.head = self.tail = new_node
            self.head.next = new_node
            self.tail.prev = new_node
        else:
            new_node.next = self.head
            new_node.prev = self.tail
            self.head.prev = new_node
            self.head.next = new_node
            self.head = new_node

        self.length+=1

    def append(self,val):
        new_node = Node(val)
        if self.length == 0:
            self.head = self.tail = new_node
            self.head.next = self.tail.prev = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            new_node.next = self.head
            self.tail = new_node
            self.head.prev = self.tail

        self.length+=1

    def __str__(self):
        result = ''
        curr = self.head
        while curr:
            result+=str(curr.val)
            if curr.next == self.head:
                break
            curr = curr.next
            result+="<->"
        return result

    def traverse(self):
        curr =self.head
        while curr:
            print(curr.val)
            curr= curr.next
            if curr == self.head:
                break
    def reverse_traverse(self):
        curr = self.tail
        while curr:
            print(curr.val)
            curr = curr.prev
            if curr == self.tail:
                break

    def search(self,val):
        curr = self.head
        index = 0
        while curr:
            if curr.val == val:
                return index
            curr = curr.next
            index+=1
            if curr == self.head:
                break
        return -1

    def get(self,index):
        curr = None
        if index < self.length//2:
            curr = self.head
            for _ in range(index):
                curr = curr.next
        elif index <= self.length-1:
            curr = self.tail
            for _ in range(self.length-1,index,-1):
                curr = curr.prev

        return curr

    def set(self,val,index):
        curr = self.get(index)
        if curr:
            curr.val = val
            return True
        return False

    def pop(self):
        if self.length ==1:
            self.head.prev = None
            self.tail.next = None
            self.head = self.tail = None
        else:
            pop_node = self.tail
            self.tail = self.tail.prev
            pop_node.next =None
            pop_node.prev = None
            self.head.prev = self.tail
            self.tail.next= None


        self.length-=1

ll = CircularDoubleLL()
ll.append(10)
ll.append(20)
ll.append(30)
ll.append(40)
print(ll.set(100,3))
print(ll)


