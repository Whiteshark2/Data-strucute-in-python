class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def takeinput():
    list = [int(ele) for ele in input().split()]
    head = None
    tail = None
    for currdata in list:
        if currdata == -1:
            break
        newnode = Node(currdata)
        if head is None:
            head = newnode
            tail = newnode
        else:
            tail.next = newnode
            tail = newnode
    return head

def printll(head):
    while head is not None:
        print(str(head.data)+"->", end="")
        head = head.next
    print("None")


def length(head):
    count = 0
    while head is not None:
        count = count+1
        head = head.next
    return count

def insertion(head,data,x):
    if x<0 or x >length(head):
        return head
    pre = None
    curr = head
    count = 0
    while count < x:
        pre = curr
        curr = curr.next
        count = count +1
    newnode = Node(data)
    if pre is not None:
        pre.next = newnode
    else:
        head = newnode
    newnode.next = curr
    return head

def appendN(head,x):
    count =1
    curr = head
    while count < length(head)-x:
        curr = curr.next
        count = count +1
    curr2 = curr.next
    curr.next = None
    tail = curr2
    while tail.next is not None:
        tail = tail.next
    tail.next = head
    return curr2

def duplicate(head):
    t1 = head
    while t1 is not None and t1.next is not None:
        if t1.data == t1.next.data:
            t1.next = t1.next.next
        else:
            t1 = t1.next
    return head

def insert(head , data):
    if head is None:
        return head
    pre = None
    curr = head
    newnode = Node(data)
    while curr is not None and curr.data <= data:
        pre = curr
        curr = curr.next
    Next = curr.next
    curr.next = newnode
    newnode.next = Next
    return head






head = takeinput()
printll(head)
head = insert(head, 34)
print(head)


