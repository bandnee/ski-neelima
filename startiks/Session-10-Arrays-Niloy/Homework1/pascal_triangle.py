# Enter your code here. Read input from STDIN. Print output to STDOUT

# Go over the range
# for each number/index , we need to make an array of that size
def print_pascal(n):
    prev_arr = [1]
    this_arr = []
    for i in range(2,n+1):
        print(prev_arr)
        for j in range(i):
            if j == 0:
                this_arr.append(prev_arr[j])
            elif j == i-1:
                this_arr.append(prev_arr[j-1])
            else :
                this_arr.append(prev_arr[j-1] + prev_arr[j])
        prev_arr = this_arr
        this_arr = []
    print(prev_arr)


print_pascal(6)