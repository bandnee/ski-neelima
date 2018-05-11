def sets (str1 ):
    result = sets_of_strings(str1)
    print (result)

def sets_of_strings(in_str):
    if len(in_str) == 0:
        return [""]
    result = []
    print (in_str[1:])
    list_of_sets = sets_of_strings(in_str[1:]
    for i in range(len(list_of_sets)):
        #append the one's in the list
        result.append(list_of_sets[i])
        # append the first character with output of the second list
        result.append(in_str[0] + list_of_sets[i])
    return result


str1 = "abcd"
sets(str1)
