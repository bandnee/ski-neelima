


def isPalin( s):
    slen = len(s)
    if slen == 1:
        return True
    slen_half = int(slen/2)
    print("isPalin-start")
    print (s)
    for i in range(0, slen_half):
        if (s[i] != s[slen - 1 - i]):
            return False
    return True



def printPalin(instr, palinstrs, plen):
    strlen = len(instr)
    print (plen)
    print(palinstrs.keys())
    if plen >= strlen:
        return
    else:
        ps = 0
        lstr = len(instr)
        pstr = ""
        while (ps <= lstr):
            pe = ps + plen
            if pe > lstr:
                pe = lstr
            if isPalin(instr[ps:pe]):
                pstr = pstr + instr[ps:pe] + "|"
            else :
                for i in range (ps,pe):
                    pstr = pstr + instr[i] + "|"
            ps = ps + plen
        if pstr in palinstrs.keys():
            palinstrs[pstr] = palinstrs[pstr] + 1
        else :
            palinstrs[pstr] = 1
        plen = plen +1
        printPalin(instr,palinstrs,plen)
        return


#palindict  = {}
#printPalin ("abba",palindict,1)
#print(palindict.keys())

def gpd(s,start):
    if start == len(s):
        return ([""])
    inlist = gpd(s,start+1)
    final_list = []
    for pstr in inlist:
        #print ("coming here")
        if (start !=0):
            final_list.append("|" + s[start] + pstr)
        final_list.append(s[start] + pstr)
    return final_list

def isPalin( s):
    slen = len(s)
    if slen == 1:
        return True
    slen_half = int(slen/2)
    for i in range(0, slen_half):
        if (s[i] != s[slen - 1 - i]):
            return False
    return True

flist = gpd("abba",0)
#print (flist)
for pstr in (flist):
    # get the first substring in the string
    # if all are plaindromes , print itdown vote

    plist = pstr.split("|")
    pcheck = 1
    for word in plist:
        #print (word)
        if not isPalin(word):
            pcheck = 0
            break
    if pcheck == 1 :
        print (pstr)




