#Reverse the words in a string
# Complete the function below.
import re
def reverse_ordering_of_words(s):
    oStr = ""
    word_list = re.split(r"(\s+)",s)
    for i in range(len(word_list)-1,-1,-1):
       oStr =  oStr + word_list[i]
    return oStr

    # Reverse the string
    # and then the reverse the string


def move_letters_to_left_side_with_minimizing_memory_writes(s):

    #sample_input : 0a193zbr
    #sample_output : azbr3zbr
    rep_index = -1
    opStr = ""
    chList = list(s)
    for i in range(len(chList)  ):
        if s[i].isdigit():
            rep_index = i
        else:
            opStr = opStr + s[i]
    return opStr


#Print matrix in spiral Order
-Direction == 0,1,2,3,
top,

def print_spiral_order(m):

    T = 0
    B = len(M)
    L = 0
    R = len(M[0])
    direction = 0

    while(T<=B and L<=R):
        if (dir==0):
            for i in range()


    dir = (dir+1) % 4