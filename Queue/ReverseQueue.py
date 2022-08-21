class Queue:
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def enqueue(self,element):
        while len(self.s1) != 0:
            self.s2.append(self.s1.pop())
        self.s1.append(element)
        while len(self.s2) != 0:
            self.s1.append(self.s2.pop())
        return

    def dequeue(self):
        if len(self.s1) == 0:
            return -1
        return self.s1.pop()

    def front(self):
        if len(self.s1) == 0:
            return -1
        return self.s1[-1]

    def size(self):
        return len(self.s1)

    def isEmpty(self):
        return self.size() == 0

    def





q = Queue()
q.enqueue(2)
q.enqueue(3)
q.enqueue(6)

while q.isEmpty() is False:
    print(q.front())
    q.dequeue()

