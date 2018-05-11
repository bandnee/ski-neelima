

import sys
import os

def hasMatchingParantheses(strExp):
    # Make a dict of valid parans

    dict_parans = {
        '{': '}',
        '[': ']',
        '(': ')'
    }
    paran_stk = []
    strL = len(strExp)
    for i in range(0, strL):
        if strExp[i] in dict_parans.values():
            if not paran_stk:
                return False
            #compare the top-element that is pushed into the stack
            if (dict_parans[paran_stk[len(paran_stk) - 1]] == strExp[i]):
                paran_stk.pop()
            else:
                return False
        elif strExp[i] in dict_parans.keys():
            paran_stk.append(strExp[i])
        else:
            # Don't push the value in  the stack if not in dict-key
            print("Next char")
    # Now check if the stack is empty if not return false
    print(paran_stk)
    if not paran_stk:
        return True
    else:
        return False