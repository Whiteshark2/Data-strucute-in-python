class Node:
    def __init__(self, data):
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


def reverse(head):  #O(n^2)
    if head is None or head.next is None:
        return head
    smallhead = reverse(head.next)
    curr = smallhead
    while curr.next is not None:
        curr = curr.next
    curr.next = head
    head.next = None
    return smallhead

#O(n)
def reverse1(head):
    if head is None or head.next is None:
        return head, head
    smallhead,smalltail = reverse1(head.next)
    smalltail.next = head
    head.next = None
    return smallhead,head

#Best Case

def reverse2(head):
    if head is None or head.next is None:
        return head
    smallhead = reverse2(head.next)
    tail = head.next
    tail.next = head
    head.next = None
    return smallhead

#Iterative approach O(n)
def reverse3(head):
    prev = None
    curr = head
    while curr is not None:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    return prev

def printll(head):
    while head is not None:
        print(str(head.data)+ "->", end="")
        head = head.next
    print("None")


head = takeinput()
printll(head)
head = reverse(head)
printll(head)
head,tail = reverse1(head)
printll(head)
head = reverse2(head)
printll(head)
head = reverse3(head)
printll(head)
