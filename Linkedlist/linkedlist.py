class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def printll(head):
    while head is not None:
        print(str(head.data)+" ->",end=" ")
        head = head.next
    print("None")


def length(head):
    count = 0
    while head is not None:
        count = count +1
        head = head .next
    return count

def printIthNode(head,i):
    pos = 0
    while head is not None:
        if pos == i:
            return head.data
        head = head .next
        pos= pos +1
    return


def take():
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
            tail= newnode
    return head

def insertion(head,data,i):
    if i < 0 or i > length(head):
        return head
    count = 0
    pre = None
    curr = head
    while count < i:
        pre = curr
        curr = curr.next
        count = count +1
    newnode = Node(data)
    if pre is not None:
        pre.next = newnode
        newnode.next = curr
    else:
        newnode.next = curr
        head = newnode
    return head

def insertionR(head,i,data): #Recursive
    if i < 0:
        return head
    if i == 0:
        newnode = Node(data)
        newnode.next = head
        return newnode
    if head is None:
        return None
    smallhead = insertionR(head.next, i-1, data)
    head.next = smallhead
    return head






head = take()
printll(head)
#print(length(head))
#print(printIthNode(head,9))
#head=insertion(head, 13, 0)
#printll(head)
head = insertionR(head,0,34)
printll(head)
