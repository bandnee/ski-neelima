# Complete the function below.
# Write the

def find_all_well_formed_brackets(n):
    flist = fbrackets(n)

    # Convert to a set and back into a list.
    fset = set(flist)
    result = list(fset)
    return result


def fbrackets(n):
    if n == 1:
        return (["()"])
    else:
        in_list = fbrackets(n - 1)
        flist = []
        for i in in_list:
            flist.append("()" + i)
            flist.append("(" + i + ")")
            flist.append(i + "()")
        return flist

i = 2n
# includes valid and invalid strings
#oc:open count
#cc: close count
def fbrackets_all(arr,n,oc,cc):
    if n == len(arr):
        return([""])
    else:
        in_list = fbrackets_all(n-1)
        flist = []
        for i in in_list:
            flist.append("(" + i)
            flist.append(")" + i)

result = find_all_well_formed_brackets(3)
print(result)