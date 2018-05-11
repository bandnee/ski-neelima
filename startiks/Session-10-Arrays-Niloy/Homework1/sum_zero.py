# Complete the function below.

def sumZero(inArr):
    for i in range(len(inArr)):
        (status, subarr) = szero(inArr, i, (len(inArr)-1))
        if status:
            return subarr
    return None


def szero(inArr, si, ei):
    if si == ei:
        if inArr[ei] == 0:
            return (True, [intArr[ei]])
        else:
            return (False, None)
    if sum(intArr[si:ei]) == 0:
        return (True, intArr[si:ei])
    else:
        szero(inArr, si, ei - 1)


def szero_memo(inArr,si,ei):
    if si == ei:
        if inArr[ei] == 0:
            return (True, [intArr[ei]])
        else:
            sdict[si] = inArr[si]
            return (False, None)
        if (not szero(inArr, si+1, ei)):
            if sum(intArr[si,ei-1]) + sdict[si] == 0:
                return (True, intArr[si:ei])
            else:
                return(False,None)


