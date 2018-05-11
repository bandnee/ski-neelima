
def  longestSub(sT):

    k = 3
    leftPtr = 0
    longLeftPtr = 0
    longSize = 0
    longRightPtr = 0
    #Hash dict that maintains the key elements
    cDict = {}

    for rightPtr in range(len(sT)):
        print(leftPtr)
        print(rightPtr)
        print(longSize)

        if len(cDict.keys()) <= k :
            if sT[rightPtr] in cDict.keys():
                cDict[sT[rightPtr]] = cDict[sT[rightPtr]] +1
            elif  len(cDict.keys()) < k :
                cDict[sT[rightPtr]] = 1
            else:
                #there are already enough keys in the Dict
                #Save the Longest substring
                #Move the LeftPtr untill Dict becomes 1 less than the
                #'k'
                if longSize < rightPtr - leftPtr:
                    longLeftPtr = leftPtr
                    longSize = rightPtr - leftPtr
                    longRightPtr = longLeftPtr + longSize

                print(sT[longLeftPtr:longRightPtr])
                for j in range(leftPtr,rightPtr):
                    #decrement the key size
                    cDict[sT[leftPtr]] = cDict[sT[leftPtr]]-1
                    if cDict[sT[leftPtr]] == 0 :
                        del cDict[sT[leftPtr]]
                        leftPtr = j+1
                        break
                        #come out of this loop
                cDict[sT[rightPtr]] = 1
            print("From inside:", longSize)
            print(cDict)

    if longSize < rightPtr - leftPtr:
        #If this is true then the last character is also part of the longest string
        longLeftPtr = leftPtr
        longSize = rightPtr - leftPtr
        longRightPtr = longLeftPtr + longSize + 1
        print("Coming in the end length calc")
    print(longSize)
    if(len(cDict.keys())<k):
        return ""
    return(sT[longLeftPtr:longRightPtr])


in_str = "ttttttttef"
print(len(in_str))
out_str = longestSub(in_str)
print(len(out_str))
print(out_str)











