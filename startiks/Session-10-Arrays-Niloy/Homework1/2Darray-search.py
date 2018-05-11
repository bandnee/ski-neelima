# Enter your code here. Read input from STDIN. Print output to STDOUT

# Do a BST on the column, if it is not found , find the row to be searched
# ie : s_elem >  cur_row[0] and s_elem < next_row[0]
# BST in the candidate row .

def search_2Darray(A1, s1):
    # Get the 0th column
    col_zero = []
    for i in range(len(A1)):
        col_zero.append(A1[i][0])

    # Do a bin search and return the index where the number could be found
    (index, status) = bsearch(col_zero, s1, 0, len(col_zero))
    if status == True :
        return(True)
    else:
        #Do a bin search on the row with the index
        row_arr = []
        for i in range(len(A1[0])):
            row_arr.append(A1[index-1][i])
        (index, status) = bsearch(row_arr, s1, 0, len(row_arr))
        return status



def bsearch(arr, selem, start, end):
    if start >= end:
        return(start,False)
    half = (start + end) // 2
    if selem  == arr[half]:
        return(half,True)
    elif selem < arr[half]:
        return(bsearch(arr,selem,start,half-1))
    else :
        return(bsearch(arr,selem,half+1,end))


Ar = [2,3,4,6,7,8,9,10]

(index,st)= bsearch(Ar, 10, 0 ,len(Ar))

print("status is " ,index, st)