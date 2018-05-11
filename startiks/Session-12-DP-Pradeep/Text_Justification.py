Latex - Donald Knuth

# abc def ghi

words = [""]

badness(i,j) = w - (E(k=i,i) len(words[k]) + (j-i))

F(i) =  Lowest cost of typesetting/justifying
        words[i:] in a paragraph

F(i) = min (F(j+1) + badness(i,j) ) V j= i to len(words)

#Base Case
if i = len(words):
    return 0


2) power N ways  : N choose  ways
    TC = #states * time/state
        = O(n square)




