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
    return

def length(head):
    count = 0
    while head is not None:
        count = count +1
        head = head.next
    return count
def appendelastN(head,pos):
    count = 1
    curr = head
    while count < length(head)-pos:
        count = count+1
        curr = curr.next
    h2 = curr.next
    curr.next = None
    tail = h2
    while tail.next is not None:
        tail = tail.next

    tail.next = head
    return h2

def delete(head,i):
    if head is None:
        return head
    if i == 0:
        head = head.next
        return head
    smallhead = delete(head.next,i-1)
    head.next = smallhead
    return head


def insertion(head,i,data):
    if i <0:
        return head
    if i == 0:
        newnode = Node(data)
        newnode.next = head
        head = newnode
        return head
    if head is None:
        return None
    smallhead = insertion(head.next, i-1, data)
    head.next = smallhead
    return head

def reverse(head):
    if head is None or head.next is None:
        return head
    smallhead = reverse(head.next)
    curr = smallhead
    while curr.next is not None:
        curr = curr.next
    curr.next = head
    head.next = None
    return smallhead






head = takeinput()
printll(head)
#head = appendelastN(head,1)
#printll(head)
#head = delete(head,3)
#printll(head)
#head = insertion(head, 2, 34)
#printll(head)
head = reverse(head)
printll(head)