# Evolution for the  problem
# No of ways for the Coin Change to be 'n'
#F(n) = # of ways to make change for $n using D
#F(n) = Sum (F(n-d))
#F(0) = 1


#F(n,i) = # of ways to make change for $n using D[i:]
#F(n,i)  =  F(n-D[i], i ) # use the coin and decrement + F(n, i+1) # don't use the coin and go to the next


#Top-down Recursion 'vs' Bottom-up Recursion

def num_ways_coin_change(n,i,D):
    if n < 0 :
        return 0
    if n == 0:
        return 1
    if i >= len(D):
        return 0:
    if(n,i) in h:
        return h[(n,i)]
        # All the paths as well
    h[(n,i)] = num_ways_coin_change(n-D[i:],i) + num_ways_coin_change(n,i+1)


# Time Complexity = O(n * D)

#Bottom-up Solution

F = [[]] n * D
F[0][i=0 to D] = 1
F[i = 1 to n][len(D)] =0
for i in range(1,n+1):
    for j in range(len(D), -1, -1):
        if i >= D[j]:
           F[i][j] = F[i-D[j]][j] + F[i][j+1]
