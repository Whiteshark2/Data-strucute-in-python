class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__count = 0

    def enqueue(self, data):
        newnode = Node(data)
        if self.__head is None:
            self.__head = newnode
            self.__tail = newnode
        else:
            self.__tail.next = newnode
            self.__tail = newnode
        self.__count +=1

    def dequeue(self):
        if self.__count == 0:
            return -1
        element = self.__head.data
        self.__head = self.__head.next
        self.__count -= 1
        return element

    def front(self):
        if self.__count == 0:
            return -1
        return self.__head.data

    def size(self):
        return self.__count

    def isEmpty(self):
        return self.size() == 0

q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
while q.isEmpty() is False:
    print(q.front())
    q.dequeue()
print(q.isEmpty())