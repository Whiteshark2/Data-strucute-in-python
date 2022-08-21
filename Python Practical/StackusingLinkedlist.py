class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = None
        self.count = 0

    def push(self,element):
        newnode = Node(element)
        newnode.next = self.head
        self.head = newnode
        self.count = self.count +1

    def pop(self):
        if self.isEmpty() is True:
            print("Stack is Empty")
            return
        element = self.head.data
        self.head = self.head.next
        self.count -=1
        return element

    def top(self):
        if self.isEmpty() is True:
            print("Stack is Empty")
            return
        return self.head.data

    def size(self):
        return self.count

    def isEmpty(self):
        return self.count==0

    def printStack(self):
        head = self.head
        while head is not None:
            print(str(head.data)+"->",end=" ")
            head = head.next
        print("None")

s=Stack()
for i in range(0,10):
    s.push(i)
s.printStack()
s.pop()
s.printStack()


