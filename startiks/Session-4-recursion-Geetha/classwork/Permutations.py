def Permutation (str1 ):
    str_l = list(str1)
    permute(str_l,0,0)


def permute(toDo : [bytes], index: int, rec_lvl):
    rec_lvl = rec_lvl+1
    if index >= len(toDo) :
        fstr = '' . join(toDo)
        print(fstr)
        print(",")
        return

    for j in range(index,len(toDo)):
        #swap i with index
        toDo[index],toDo[j] =  toDo[j],toDo[index]
        print("index : rec_lvl  : j ", index,rec_lvl,j)
        permute(toDo,index+1,rec_lvl)
        toDo[index],toDo[j] =  toDo[j],toDo[index]


str1 = "ab"
Permutation(str1)