def sort-odd_even(A,start,end):
    if start >= end:
        return

def Partition(A,start,end,pivotindex):
    boundary,j=start
    while(j< end+1):
        if (A[j] // 2 == 0 ):
            if(j != boundary):
                swap(A[j],a[boundary])
            boundary = boundary+1
        j = j + 1
    #put the pivot position back in it's position.
    swap(A,boundary,end)
    return(boundary)

