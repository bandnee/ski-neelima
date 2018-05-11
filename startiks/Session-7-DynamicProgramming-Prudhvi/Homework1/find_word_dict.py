
def wb_search(strw, strDict):
    (found,list) = _wb_n(strw,strDict)
    if found:
        print("Printing")
        print(list)


def _wb(s1, strDict):
    if len(s1) == 0:
        return (True, [])
    this_list = []
    for i in range(1, len(s1)+1):
        if s1[0:i] in strDict:
            this_list.append(s1[0:i])
            (found, lwords) = _wb(s1[i:], strDict)
            if found:
                flist = this_list + lwords
                return (True, flist)
            else:
                return (False, [""])

    return (False, [""])

def _wb_n(s1, strDict):
    print("_wb_n: s1: " + s1 + "\n")

    if len(s1) == 0:
        return (True, [[]])

    f_list = []
    for i in range(1, len(s1)+1):
        if s1[0:i] in strDict:
            (found, lwordslists) = _wb_n(s1[i:], strDict)
            if found:
                for wordlist in lwordslists:
                    f_list.append([s1[0:i]] + wordlist)

    return (len(f_list) > 0, f_list)

wb_search("interviewkickstart",["inter","view","kick","start","interview","kickstart"])