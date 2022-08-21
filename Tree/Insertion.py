def insertion(list):
    length = len(list)
    for i in range(0,length):
        key = list[i]
        j = i-1
        while j>=0 and key < list[j]:
            list[j+1]=list[j]
            j = j-1
        list[j+1]= key



list = []
n = int(input("Enter the number of element = "))
for i in range(0, n):
   ele = int(input())
   list.append(ele)
print("List Before Sorting = ",list)
insertion(list)
print("List After Sorting = ", list)
