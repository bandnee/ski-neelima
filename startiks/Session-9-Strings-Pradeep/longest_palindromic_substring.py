

def long_palin_string(word):
    #Go over each letter and consider that to be the center of the word
    #that being the center collect the longest Palin .
    longest = ""
    #check for odd lengthed palindrome
    for pindex in range(len(word)) :
        ps = pindex - 1
        pe = pindex + 1
        palin = word[pindex]
        while(ps>=0 and pe<len(word)):
            if word[ps] == word[pe] :
                palin = word[ps] + palin + word[pe]
                ps = ps - 1
                pe = pe + 1
            else:
                break
        if len(longest) < len(palin) :
            longest = palin

    #check for even lengthed palindrome
    for pindex in range(len(word)-1):
        if word[pindex] == word[pindex+1]:
            ps = pindex - 1
            pe = pindex + 2
            palin = word[pindex] + word[pindex+1]
            while (ps >= 0 and pe < len(word)):
                if word[ps] == word[pe]:
                    palin = word[ps] + palin + word[pe]
                    ps = ps - 1
                    pe = pe + 1
                else:
                    break
            if len(longest) < len(palin):
                longest = palin
        '''else :
            # odd string palin, we already got it from previous loop
            print("Already Processed")
        '''

    return(longest)


w = "carracecar"
print(long_palin_string(w))
