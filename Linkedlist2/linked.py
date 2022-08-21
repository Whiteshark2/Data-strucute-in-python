class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

def takin():
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
        print(str(head.data)+" ->", end="")
        head = head.next
    print("None")
    return

def insertion(head,data,i):
    if i < 0:
        return head
    if i == 0:
        newnode= Node(data)
        newnode.next = head
        return newnode
    if head is None:
        return None
    smallhead = insertion(head.next, data , i-1)
    head.next = smallhead
    return head

def delete(head,i):
    if head is None:
        return head
    if i == 0:
        head = head.next
        return head
    smallhead = delete(head.next,i-1)
    head.next = smallhead
    return head




head = takin()
printll(head)
#head = insertion(head, 23, 2)
#printll(head)
head = delete(head,3)
printll(head)



