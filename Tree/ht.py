def quicksort(list,si,ei):
    if si>=ei:
        return
    piv = partition(list,si,ei)
    quicksort(list,si,piv-1)
    quicksort(list,piv+1,ei)

def partition(list,si,ei):
    pivot = list[si]
    c = 0
    for i in range(si,ei+1):
        if list[i] < pivot:
            c= c+1
    list[si],list[si+c] = list[si+c],list[si]
    pivindex = si+c
    i = si
    j = ei
    while i < j:
        if list[i] <pivot:
            i = i+1
        elif list[j] >=pivot:
            j = j-1
        else:
            list[i],list[j] = list[j],list[i]
            i = i+1
            j = j-1
    return pivindex






list =[6,10,9,8,1,3,5,4,2]
partition(list,0,len(list)-1)
print(list)