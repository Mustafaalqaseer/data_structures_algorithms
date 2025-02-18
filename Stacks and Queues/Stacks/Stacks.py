from logging import exception


class Stack:
    def __init__(self):
        self.list = []


    def __str__(self):
        values = reversed(self.list)
        values = [str(element) for element in values]
        return '\n'.join(values)



    def isEmpty(self):
        if self.list == []:
            return True
        else:
            return False

    def push(self,val):
        self.list.append(val)
        return None

    def peek(self):
        if self.isEmpty():
            return "array is empty"
        else:
            return self.list[len(self.list)-1]

    def pop(self):
        # if len(self.list) <= 0:
        #     return exception("array is empty")

        if self.isEmpty():
            return exception("There is no element in list")
        self.list.pop()
        return None

    def delete(self):
        self.list = None


stack = Stack()



print(stack.pop())
stack.push(93)
stack.push(100)
print(stack)


