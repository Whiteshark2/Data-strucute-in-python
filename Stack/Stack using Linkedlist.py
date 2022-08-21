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
        data = self.head.data
        self.head = self.head.next
        self.count = self.count -1
        return data

    def top(self):
        if self.isEmpty() is True:
            print("Stack is Empty")
            return
        data = self.head.data
        return data

    def size(self):
        return self.count

    def isEmpty(self):
        return self.size() == 0

    def printll(self):
        head = self.head
        while head is not None:
            print(str(head.data)+"-> ",end="")
            head = head.next
        print("None")




s1 = Stack()
for i in range(1,7):
    s1.push(i)

s1.printll()
s1.pop()
s1.printll()