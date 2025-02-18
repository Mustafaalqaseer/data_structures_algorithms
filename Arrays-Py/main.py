from LL.LinkedList import LinkedList

def nthToLast(ll,n):
    pointer1 = ll.head
    pointer2 = ll.head
    if pointer1 is None:
        return None
    for _ in range(n):
        pointer2 = pointer2.next

    while pointer2:
        pointer1 = pointer1.next
        pointer2 = pointer2.next

    return pointer1

def partition(ll,x):
    curr = ll.head
    ll.tail = ll.head


def sumLists(ll1,ll2):
    curr1 = ll1.head
    curr2 = ll2.head
    final_ll= LinkedList()
    carry = 0
    while curr1 or curr2:
        result = carry
        if curr1:
            result+=curr1.value
            curr1 = curr1.next

        if curr2:
            result+=curr2.value
            curr2 = curr2.next

        final_ll.add(int(result%10))
        carry = result /10

    return final_ll








l1 = LinkedList()
l1.add(7)
l1.add(1)
l1.add(6)

l2 = LinkedList()
l2.add(5)
l2.add(9)
l2.add(2)
print(l1)
print(len(l1))



