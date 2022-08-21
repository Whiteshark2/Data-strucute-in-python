def linear(list,x):
    length = len(list)
    for i in range(0,n):
        if list[i] == x:
            print("Found at ",i,"Search Successful")
            return
    print("Search Unsuccessful ")
    return

list = []
n = int(input("Enter the number of element = "))
for i in range(0,n):
    ele = int(input())
    list.append(ele)
x=int(input("Enter the number to be serched = "))
linear(list,x)