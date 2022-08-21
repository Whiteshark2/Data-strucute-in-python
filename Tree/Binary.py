"""def Binary(list,x):
    l = len(list)
    low = 0
    high = l-1
    while low  <= high:
        mid = (low+high)//2
        if list[mid] == x:
            print("found at ",mid)
            return
        elif mid <x:
            low = mid+1
        else:
            high = mid-1
    print("Not found ")
    return"""

def binary1(list,x,si,ei):
    if ei > si:
        return -1
    mid = (ei+si)//2
    if list[mid]==x:
        return mid
    elif list[mid]<x:
        return binary1(list,x,mid+1,ei)
    else:
        return binary1(list,x,si,mid-1)




list = []
n = int(input("Enter the number of element = "))
for i in range(0,n):
    ele = int(input())
    list.append(ele)
x=int(input("Enter the number to be serched = "))
result = binary1(list,x,0,len(list)-1)
if result == -1:
    print("Not found")
else:
    print("found at ",result)
