import random

# The place where I got wrong first  is to send the pivotIndex
#
def Partition(A, start, end, pivot):
    i = start
    equal_boundary = start
    gt_begin = end
    while(i < gt_begin):
        if (A[i] < pivot):
            if i != equal_boundary:
                A[i], A[equal_boundary] = A[equal_boundary], A[i]
            i = i + 1
            equal_boundary = equal_boundary + 1
        elif (A[i] == pivot):
            i = i + 1
        elif (A[i] > pivot):
            gt_begin = gt_begin - 1
            A[i], A[gt_begin] = A[gt_begin], A[i]
    return (equal_boundary)


def QuickSort(A, start,end):
    print ("Sorting ", A[start:end])
    if start >= end:
        return
    pivotI = random.randint(start, end-1)
    print ("Pivot" , A[pivotI])
    mid = Partition(A, start,end,A[pivotI])
    QuickSort(A, start, mid)
    QuickSort(A, mid+1, end)
    return


# Partition the first array with a last or first index and decrease or increase.

def sortNutsBolts(N, B):
    start = 0
    nb_size = len(N)
    print ("len of n is", nb_size)
    sortNB(N, B, start, nb_size)


#Main idea is that you call the Partition and Sort twice, but using the other guy's pivot position.
# But sort the same letft and right arrays and you are partiioning twice instead of once in a regular
#quicksort .

def sortNB(N, B, start, nb_size):
    if start >= nb_size:
        return
    # Get the   pivot elements for both nuts and bolts ,
    #based  on
    pivot = N[nb_size - 1]
    # pick a random pivot or the last element as pivot from NUTS for bolts
    #Partition will return the right positin of the bolt .
    pivot_posB = Partition(B, start, nb_size, pivot)

    # IF you simply
    #Use the bolt pivot's bolt position and use that to get the right position for the
    # the same nuts  pivot position.

    pivot_posN = Partition(N, start, nb_size, B[pivot_posB])
    sortNB(N, B, start, pivot_posB)
    sortNB(N, B, pivot_posB+1, nb_size)



#Main idea is that you call the Partition and Sort twice, but using the other guy's pivot position.
# But sort the same letft and right arrays and you are partiioning twice instead of once in a regular
#quicksort .

def sortNB_wo_B(N, B, start, nb_size):
    if start >= nb_size:
        return
    # Get the   pivot elements for both nuts and bolts ,
    #based  on
    pivot = N[nb_size - 1]
    # pick a random pivot or the last element as pivot from NUTS for bolts
    #Partition will return the right positin of the bolt .
    pivot_posB = Partition(B, start, nb_size, pivot)

    # IF you simply
    #Use the bolt pivot's bolt position and use that to get the right position for the
    # the same nuts  pivot position.

    pivot_posN = Partition(N, start, nb_size, B[pivot_posB])
    sortNB_wo_B(N, B, start, pivot_posB)
    sortNB_wo_B(N, B, pivot_posB+1, nb_size)


# Complete the function below.

def groupNumbers(A):
    # Start the odd pointer from the end of the array len(intArr)
    # Start the even_end pointer from the beg of the array
    # Go through each element and check if odd, move the odd pointer
    # by op -1 , swap the elements .
    # If the element is even , move the even ptr
    # repeat the process till even_ptr >= odd_ptr
    even_end = 0
    odd_begin = len(A)
    while (even_end < odd_begin):
        if (A[even_end] % 2 == 0):
            even_end = even_end + 1
        else:
            odd_begin = odd_begin - 1
            A[even_end], A[odd_begin] = A[odd_begin], A[even_end]
    return A



# Enter your code here. Read input from STDIN. Print output to STDOUT
N = [3, 7, 4, 8, 2, 1, 9, 10]
B = [7, 4, 3, 8, 1, 2, 10, 9]


#A = [ 1,3,4,2,8,9,4,5,7,6]
#size = len(A)
#print(A)
#QuickSort(A, 0,len(A))
sortNutsBolts(N, B)
#groupNumbers(N)
print(N)
print(B)
