def Selection(list):
    length = len(list)
    for i in range(0,length-1):
        min = i
        for j in range(i+1,length):
            if list[j] <list[min]:
                min = j
        list[i],list[min]= list[min],list[i]
    print(list)



list = []
n = int(input("Enter the number of element = "))
for i in range(0, n):
   ele = int(input())
   list.append(ele)
Selection(list)