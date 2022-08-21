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


def merge(head1, head2):
    final = None
    tail = None
    if head1.data < head2.data:
        final = head1
        tail = head1
        head1 = head1.next
    else:
        final = head2
        tail = head2
        head2 = head2.next

    while head1 is not None and head2 is not None:
        if head1.data < head2.data:
            tail.next = head1
            tail = tail.next
            head1 = head1.next
        else:
            tail.next = head2
            tail = tail.next
            head2 = head2.next
    if head1 is not None:
        tail.next = head1
    if head2 is not None:
        tail.next = head2
    return final



def printll(head):
    while head is not None:
        print(str(head.data)+"-> ", end = "")
        head = head.next
    print("None")


head1 = takeinput()
printll(head1)
head2 = takeinput()
printll(head2)

head3 = merge(head1,head2)
printll(head3)