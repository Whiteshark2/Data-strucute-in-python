class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
def takein():
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
    print(head)
    return

def check(head,data):
    count = 0
    curr = head
    while curr is not None:
        if curr.data == data:
            return count
            break
        count = count +1
        curr = curr.next
    return -1

def length(head):
    count = 0
    while head is not None:
        count = count +1
        head = head.next
    return count

def duplicate(head):
    t1 = head
    t2 = head.next
    while t2 is not None:
        if t1.data == t2.data:
            t2 = t2.next
        else:
            t1.next = t2

    return head

def reverse(head):
    if head is None:
        return None
    reverse(head.next)
    print(str(head.data)+"->",end="")
    return


def insertAt(head,data):
    slow = head
    fast = head
    while fast.next is not None and fast.next.next is not None:
        slow = slow.next
        fast = fast.next.next
    curr = head
    prev = None
    newnode = Node(data)
    while curr is not slow:
        prev = curr
        curr = curr.next
    Next = curr.next
    curr.next = newnode
    newnode.next = Next
    return head



head = takein()
printll(head)
#reverse(head)
#print(check(head, 2))
#head = duplicate(head)
#printll(head)
head = insertAt(head,3)
printll(head)