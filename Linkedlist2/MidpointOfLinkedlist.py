class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


def takeinput():
    list = [int(ele) for ele in input().split()]
    head = None
    for currdata in list:
        if currdata == -1:
            break
        newnode = Node(currdata)
        if head is None:
            head = newnode
        else:
            curr = head
            while curr.next is not None:
                curr = curr.next
            curr.next = newnode
    return head


def midpoint(head):
    slow = head
    fast = head
    while fast.next is not None and fast.next.next is not None:
        slow = slow.next
        fast = fast.next.next
    return slow.data

def printll(head):
    while head is not None:
        print(str(head.data)+"-> ", end = "")
        head = head.next
    print("None")



head = takeinput()
printll(head)
print(midpoint(head))
