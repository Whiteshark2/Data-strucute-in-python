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

def EvenAfterOdd(head):
    oddhead = None
    oddtail = None
    evenhead = None
    eventail = None
    while head is not None:
      if head.data % 2==1:
          if oddhead is None:
              oddhead = head
              oddtail = head
          else:
              oddtail.next = head
              oddtail = head
      else:
          if evenhead is None:
              evenhead = head
              eventail = head
          else:
              eventail.next = head
              eventail = head
      head = head.next
    if oddhead is None:
        return evenhead
    elif evenhead is None:
        return oddhead
    else:
        oddtail.next = evenhead
        eventail.next = None
        return oddhead



head = takeinput()
printll(head)
head = EvenAfterOdd(head)
printll(head)