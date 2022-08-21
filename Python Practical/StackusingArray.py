class Stack:
    def __init__(self):
        self.array = []

    def push(self,element):
        self.array.append(element)

    def pop(self):
        if self.size() ==0:
            print("Stack is Empty")
            return
        return self.array.pop()

    def top(self):
        if self.size() == 0:
            print("Stack is Empty")
            return
        return self.array[-1]

    def size(self):
        return len(self.array)

    def isEmpty(self):
        return len(self.array) ==0

s = Stack()
s.push(1)
s.push(2)
s.push(3)
while s.isEmpty() is False:
    print(s.pop())