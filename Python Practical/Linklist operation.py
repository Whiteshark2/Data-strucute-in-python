class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def takeinput():
    list = [int(ele) for ele in  input().split()]
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

def printLL(head):
    curr = head
    while curr is not None:
        print(str(curr.data)+"->",end=" ")
        curr = curr.next
    print("None")



def insertion(head,i,data):
    if i<0:
        return head
    if i==0:
        newnode = Node(data)
        newnode.next = head
        return newnode

    smallhead = insertion(head.next,i-1,data)
    head.next = smallhead
    return head

def deletion(head,i):
    if i<0:
        return head
    if i==0:
        head= head.next
        return head
    smallhead = deletion(head.next,i-1)
    head.next = smallhead
    return head




head = takeinput()
printLL(head)
#head = insertion(head,3,555)
#printLL(head)
head = deletion(head,3)
printLL(head)

