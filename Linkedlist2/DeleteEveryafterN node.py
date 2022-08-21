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

def printll(head):
    while head is not None:
        print(str(head.data)+"-> ", end= "")
        head = head.next
    print("Null")

def deleteEveryMnode(head,n,m):
    count1 = 1
    count2 = 1
    curr = head
    while head is not None:
        while count1 < n:
            if curr is None:
                break
            count = count+1
            curr = curr.next
        temp = curr.next
        count1 = 1
        while count2 < m:
            if temp is None:
                break
            count2 = count2 +1
            temp = temp.next
        count2 = 1
        curr.next = temp
        curr = temp
    return head


head = takeinput()
printll(head)
head = deleteEveryMnode(head,2,3)
printll(head)
