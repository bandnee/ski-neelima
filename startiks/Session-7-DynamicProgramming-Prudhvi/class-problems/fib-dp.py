def fib_dp(num):
    arr = [0,1]
    for i in range(2,num+1):
        #print(i)
        arr.append(arr[i-1] + arr[i-2])
    return(arr[num])


def fib_recurse(num):
    if num == 0 :
        return 0
    elif num == 1:
        return 1
    return(fib_recurse(num-1) + fib_recurse(num-2))

def fib_memo(num):
    cache ={}
    cache[0] = 0
    cache[1] = 1
    return(_fib_memo(num,cache))

def _fib_memo(num,cache):
    if num in cache.keys():
        return cache[num]
    cache[num] = _fib_memo(num-1,cache) + _fib_memo(num-2,cache)
    return cache[num]

Time Complexity:
T(n) = T(n-1)
#0,1,2,3,4,5,6,7,8
#0,1,1,2,3,5,8,13,21


print(fib_dp(8))

print(fib_memo(8))

print(fib_recurse(8))