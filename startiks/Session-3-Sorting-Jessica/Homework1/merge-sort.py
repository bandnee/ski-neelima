A = [ 1,3,4,2,8,9,4,5,7,6]

def mergeSort(A):
    if(len(A)<=1):
        return A
    mid = len(A)//2
    l_list = mergeSort(A[:mid])
    r_list = mergeSort(A[mid:])
    return(merge(l_list,r_list))

def mergeSort1(A,start,end):
    if(start == end-1):
        return [A[start]]
    mid = (start+end)//2
    l_list = mergeSort1(A,start,mid)
    r_list = mergeSort1(A,mid,end)
    return(merge(l_list,r_list))

def merge(l_list,r_list):
    #print(l_list)
    #print(r_list)
    #print ("###########")

    i = 0
    j=0
    flist = []
    while (l_list and  r_list) :
        if l_list[i] < r_list[j] :
            flist.append(l_list[i])
            del l_list[i]
        elif l_list[i] > r_list[j] :
            flist.append(r_list[j])
            del r_list[j]
        else:
            flist.append(l_list[i])
            del l_list[i]
            flist.append(r_list[j])
            del r_list[j]
    while(l_list ) :
        flist.append(l_list[0])
        del l_list[0]

    while (r_list):
        flist.append(r_list[0])
        del r_list[0]
    return flist


A = [1, 3, 4, 2, 8, 9, 4, 5, 7, 6]

print(mergeSort1(A,0,len(A)))
#print(mergeSort(A))
