

#Recurrence Relationship
#Constraint: all positive numbers
#f(i,r) - Returns no of subsets,starting from index 'i'
#        that add up to 'r'
# if r == 0:  1 subsets
# if i ==len(arr) : 0 subsets
# f(i+1,r) if r < arr[i]
#f(i+1,r) + f(i+1,r-arr[i])
# First identify the dimension of the table
# Size of the dimension
#(N+1) * (K+1)


#Recursive Solution
def cnt_subsets_recurse(arr,k):
    i = 0  # start index
    r = k # remaining
    count = []
    #For pass by reference
    count.append(0)
    _cnt_subsets_recurse(arr,i,r,count)
    print(count[0])


def _cnt_subsets_recurse(arr,i,r,count):
    if r == 0:
        count[0] = count[0] + 1
        return
    if i == len(arr):
        return
    #include the arr[i] index and decrement remaining by arr[i]
    _cnt_subsets_recurse(arr,i+1,r-arr[i],count)
    #exclude the arr[i] index and pass the same remaining
    _cnt_subsets_recurse(arr, i+1, r, count)


def count_subsets_dp(arr, k):

    table = [[None] * (k+1) for _ in range(len(arr)+1)]

    for r in range(0,k+1):
        table[len(arr)][r] = 0
    for i in range(0,len(arr)+1):
        table[i][0] = 1

    for i in range((len(arr)-1),-1,-1):
        for r in range(1,k+1):
            print(i,r)
            if r < arr[i]:
                table[i][r] = table[i+1][r]
            else:
                table[i][r] = table[i+1][r] + table[i+1][r-arr[i]]
    print(table[0][k])


arr= [1,3,4,5,6,2]
k=8

#arr = [1,3,4]
#k=4

#cnt_subsets_recurse(arr,k)

count_subsets_dp(arr,k)