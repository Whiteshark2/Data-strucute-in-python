class Stack:
    def __init__(self):
        self.__data = []
    def push(self, item):
        self.__data.append(item)
    def pop(self):
        if self.isEmpty():
            print("Stack is Empty")
            return
        return self.__data.pop()
    def top(self):
        if self.isEmpty():
            print("Stack is Empty")
            return
        return self.__data[len(self.__data)-1]
    def size(self):
        return len(self.__data)
    def isEmpty(self):
        return self.size == 0

    def isRedundant(self, string):
        s = []
        for char in string:
            if char != ')':
                print(s.push(char))

s = Stack()
s.isRedundant(string)