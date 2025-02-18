from logging import exception

from numpy.ma.core import append


class Node:
      def __init__(self,val,next = None):
          self.val = val
          self.next = next


class CSLinkedList:
     def __init__(self):
         self.tail = None
         self.head = None
         self.length = 0


     def append(self,val):
        new_node = Node(val)
        if self.length == 0:
            self.tail = self.head = new_node
            new_node.next = new_node
        else:
            new_node.next = self.head
            self.tail.next = new_node
            self.tail = new_node
        self.length+=1


     def __str__(self):
         result = ""
         curr = self.head

         while curr:
             result+= str(curr.val)
             curr = curr.next

             if curr == self.head:
                 break
             result += '-->'

         return result


     def prepend(self,val):
         new_node = Node(val)

         if self.length == 0:
             self.tail = self.head = new_node
             new_node.next = new_node
         else:

            new_node.next = self.head
            self.tail.next = new_node
            self.head = new_node

         self.length+=1

     def insert(self,index,val):
         if index<0 or index > self.length:
             return None

         new_node = Node(val)

         if index == 0:
             if self.length == 0:
                 self.head = self.tail = new_node
                 new_node.next = new_node
             else:
                new_node.next = self.head
                self.head = new_node
                self.tail.next = new_node
         elif index == self.length:
             self.append(val)
         else:

             curr = self.head

             for _ in range (index-1):  # index = 2 - 1
                curr = curr.next

             new_node.next = curr.next
             curr.next = new_node
         self.length+=1

     def traversal(self):
         curr = self.head
         while curr:
             print(curr.val)
             curr = curr.next
             if curr == self.head:
                 break



     def search(self,val):
         curr = self.head

         while curr:
             if curr.val == val:
                 return True
             curr = curr.next
             if curr == self.head:
                 return False

     def get(self ,index):
         curr = self.head
         if index < 0 or index>=self.length:
             return None

         for _ in range(index):
             curr = curr.next

         return curr

     def set(self,val,index):
         temp = self.get(index)
         if temp:
             temp.val = val
             return True
         return False

     def pop_first(self):
         if self.length == 0:
             return None

         curr = self.head

         if self.length == 1:
             self.head = self.tail = None
         else:
             self.head = self.head.next
             self.tail.next = self.head
             curr.next = None

         self.length-=1

         return curr

     def pop(self):
         if self.length == 0:
             return None

         result = self.tail

         if self.length==1:
             self.tail = self.head = None
             return result


         curr = self.head

         for _ in range(self.length-2):
            curr = curr.next

         curr.next = self.head
         self.tail.next = None

         self.tail = curr
         self.length-=1
         return result

     def remove(self,val):

         current = self.head
         while current:
             if current.next.val == val:
                 current.next = current.next.next
                 popp_node = current.next
                 break
             current = current.next
                                                                 # 1 -->2 -->3 -->4 -->5

             if current == self.head:
                 return exception("value not in Singly_linked_list")


         popp_node.next = None


         self.length -=1

     def delete_all(self):
         self.tail.next = None
         self.tail = self.head = None
         self.length = 0





my_cs = CSLinkedList()

my_cs.append(13)
my_cs.append(15)
my_cs.pop()

print(my_cs)





