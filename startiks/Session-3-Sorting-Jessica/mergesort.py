def mergesort(A,start,end):
    if len(A)<=1:
        return A
    middle = start+end/2
    L = mergesort(A,start,middle)
    R = mergesort(A,middle+1, end)
    return merge(L,R)

def merge(L,R):
    i=0
    j=0
    if A[start]
