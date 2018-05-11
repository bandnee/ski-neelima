
def Sum3(A,k):
    r_sum = 0
    res = []
    for i in range(len(A)-3):
        if (A[i] < k ):
            r_sum = k-A[i]
        l= i+1
        r= len(A)-1
        while (l<r ):
            print("Coming here")
            if A[l] + A[r] > r_sum:
                r=r-1
            elif A[l] + A[r] < r_sum:
                l=l+1
            else:
                res.append([A[i],A[l],A[r]])
                r = r-1
                l = l+1
    print (res)

in_list = [1,2,3,4,5,6,1]

k = 8
Sum3(in_list,k)