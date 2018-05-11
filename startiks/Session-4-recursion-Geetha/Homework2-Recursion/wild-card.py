
WILD_CHAR = '?'

def wild(in_str):
    str_arr = list(in_str)
    wild_card(str_arr, 0)

def wild_card(str_arr, ind):
    if ind == len(str_arr) :
        finalstr = ''.join(str_arr)
        print(finalstr)
        return
    if str_arr[ind] == WILD_CHAR :
        str_arr[ind] = '0'
        wild_card(str_arr,ind+1)
        str_arr[ind] = '1'
        wild_card(str_arr,ind+1)
        str_arr[ind] = WILD_CHAR
    else:
        wild_card(str_arr,ind+1)
    return



wild("1???")