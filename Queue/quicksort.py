def quick(list,low,high):
    if low>=high:
        return
    p=partition(list,low,high)
    quick(list,low,p-1)
    quick(list,p+1,high)



def partition(list,low,high):
    pivot = list[low]
    count =0
    for i in range(low,len(list)):
        if list[i]<pivot:
            count+=1
    list[low],list[low+count]=list[low+count],list[low]
    p=low+count
    i=low
    j=high
    while i<j:
        if list[i]<pivot:
            i+=1
        elif list[j]>pivot:
            j-=1
        else:
            list[i],list[j]=list[j],list[i]
            i+=1
            j-=1
    return p


list=[]
n=int(input("Enter the number of list =  "))
for i in range(0,n):
    list.append(int(input()))
quick(list,0,len(list)-1)
print(list)