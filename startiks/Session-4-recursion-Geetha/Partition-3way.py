def Partition(A,start,end):

    low =0
    mid =0
    hi =end

    boundary,j=start
    #Swap with the last element
    swap (A,pivotindex,end)
    while(j< end+1):
        if (A[j] <= A[end] ):
            if(j != boundary):
                swap(A[j],a[boundary])
            boundary = boundary+1
        j = j + 1
    #put the pivot position back in it's position.
    swap(A,boundary,end)
    return(boundary)
