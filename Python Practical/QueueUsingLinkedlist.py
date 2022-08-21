class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0


    def enqueue(self,data):
        newnode = Node(data)
        if self.head is None:
           self.head = newnode
           self.tail = newnode
        else:
            self.tail.next = newnode
            self.tail=newnode
        self.count = self.count+1

    def dequeue(self):
        if self.count == 0:
            print("Queue is Empty")
            return
        element = self.head.data
        self.head = self.head.next
        self.count = self.count -1
        return element

    def front(self):
        if self.count ==0:
            print("Queue is empty")
            return
        return self.head.data


    def size(self):
        return self.count

    def isEmpty(self):
        return self.size()==0


    def printQueue(self):
        head = self.head
        while head is not None:
            print(str(head.data)+" ->",end=" ")
            head= head.next
        print("None")



q=Queue()
for i in range(0,10):
    q.enqueue(i)
q.printQueue()
q.dequeue()
q.printQueue()



