# Given a string


def print_neuronyms(word):
    wlen = len(word)
    max_neuro_size = wlen-2
    if max_neuro_size <= 0 :
        print("No Neuronyms")
    else:
        for cmn in range(max_neuro_size,0,-1):
            neuro_set = set([])
            cr=max_neuro_size-cmn
            for j in range(0,cr+1):
                neuro_word = word[:j+1] + str(cmn) + word[cmn+1+j:]
                neuro_set.add(neuro_word)
            print(neuro_set)


w = "muppalaneni"
print_neuronyms(w)



