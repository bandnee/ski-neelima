# No of binary trees that can be formed given 'n' number of nodes
# For 0 node : a 0 node tree can be formed, so o/p is 1
# For 1 node : 1 tree can be formed , so /op is 1
# For 2 node : i at root 1 at l/right , so 2 can be formed
# For 3 : 1, being root : (1,1) + (2,0) + (0,2)  ie: 1 + 2 + 2 = 5
# For 4: 1 being root : (1,2) + (2,1) + (3,0) + (0,3) ie:
# 2 (1 node on left, 2 nodes on right) + 2 (2 nodes on left , 1 node on right )+ (5+5) 2 * f(n-1) = 14
# For 5: 1 being root: (2,2) + (3,1) + (1,3) + (4,0) + (0,4) = 4 + 5 + 5 +14 + 14 = 42
# For 6: 1 being root: (5,0) + (0,5) +  (4,1) + (1,4) + (3,2) + (2,3)  = 42 + 42 + 14 +14 +10 +10

def computeBTs(n):
    if (n == 0):
        return 1
    elif (n==1):
        return 1
    else:
        BT_count = (2 * computeBTs(n-1))
    for i in range (1,n-1):
        l = computeBTs(i)
        j = n-1-i
        r = computeBTs(j)
        BT_count = BT_count + l*r
    return BT_count

def computeBT_memo(n, bt_dict,fbt_cnt):
    print("first ", n)
    if (n == 0):
        bt_dict[0] = 1
        return 1
    elif(n==1):
        bt_dict[1] = 1
        return 1
    else:
        this_cnt = (2 * computeBT_memo(n-1,bt_dict,fbt_cnt))
        fbt_cnt = this_cnt + fbt_cnt
    for i in range(1,n-1):
        print("coming")
        l = bt_dict[i]
        j = n-1-i
        r = bt_dict[j]
        print ("left, right,n", i,j ,n)
        fbt_cnt = fbt_cnt + l*r
    bt_dict[n] = fbt_cnt
    print (bt_dict)
    print("last" , n)
    return(bt_dict[n])


def computeBT_memo2(n, bt_dict,fbt_cnt):
    print("first ", n)
    if (n == 0):
        bt_dict[0] = 1
        return 1
    elif(n==1):
        bt_dict[1] = 1
        return 1
    else:
        '''this_cnt = computeBT_memo2(n-1,bt_dict,fbt_cnt)
        fbt_cnt = this_cnt + fbt_cnt
        '''
        computeBT_memo2(n-1, bt_dict, fbt_cnt)
        for i in range(0,n):
            l = bt_dict[i]
            j = n-1-i
            r = bt_dict[j]
            print ("left, right,n", i,j ,n)
            fbt_cnt = fbt_cnt + l*r
        bt_dict[n] = fbt_cnt
        print (bt_dict)
        print("last" , n)
    return(bt_dict[n])


bt_dict = {}
bt_dict[0] = 1
bt_dict[1] = 1
fbt_cnt = 0


print(computeBT_memo2(5, bt_dict, fbt_cnt))

print(computeBTs(2))

