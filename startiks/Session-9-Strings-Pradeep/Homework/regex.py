

class TrieNode:
    def __init__(self,val):
        self.val = val
        self.children = {}
        self.word_ending = None

#Time Complexity is O(N*M) with M
class Trie:
    def __init__(self):
        self.rootNode = TrieNode(" ")

    def addword(self,w1):
        currentNode = self.rootNode
        for ch in w1:
            if ch not in currentNode.children.keys():
                #char is not  present, create a newNode
                currentNode.children[ch] = TrieNode(ch)
            currentNode = currentNode.children[ch]
        currentNode.word_ending = True

    def searchword(self,w1):
        currentNode = self.rootNode
        for ch in w1:
            if ch not in currentNode.children.keys():
                #char is not  present, return False
                return False
            currentNode = currentNode.children[ch]
        return(currentNode.word_ending)

    def searchPrefix(self,prefix):
        currentNode = self.rootNode
        for ch in len(prefix):
            if ch not in currentNode.children.keys():
                #Prefix is not present , return [""]
                return []
            currentNode = currentNode.children[ch]
        word = list(prefix)
        wordList = []
        self._collect_all(currentNode,word,wordList)
        return wordList

    def _collect_all(self,Node,word,wList):
        currentNode = Node
        if currentNode.word_ending :
            wList.append("".join(word))
        if currentNode == None:
            return
        for ch in currentNode.children.keys():
            word.append(ch)
            self._collect_all(currentNode[ch],word,wList)
            word.pop()

    def searchPattern(self,pattern):
        # Go to the indxof the
        indx = 0
        output=set([])
        word = []
        node = self.rootNode
        self._searchPattern(node,word,indx,pattern,output)
        return(output)

    def _searchPattern(self,node,word,indx,pattern,output):
        if indx == len(pattern):
            if node.word_ending :
                print(output)
                output.add("".join(word))
            return
        if node.children.keys() == 0:
            if node.word_ending :
                output.add("".join(word))
                print(output)
            return
        if pattern[indx] != '.' and pattern[indx] !=  '*' :
            for ch in node.children.keys():
                if ch == pattern[indx]:
                    print ("appending letter" , ch)
                    word.append(ch)
                    self._searchPattern(node.children[ch],word,indx+1,pattern,output)
                    word.pop()
        elif pattern[indx] == '.':
            for ch in node.children.keys():
                print("appending dot", ch)
                word.append(ch)
                self._searchPattern(node.children[ch], word, indx + 1, pattern,output)
                wdot = word.pop()
                print("popped dot", wdot)
        else:
            for ch in node.children.keys():
                print("appending * 2", ch)

                if indx >= len(pattern) and  (ch == pattern[indx+1]):
                    word.append(ch)
                    self._searchPattern(node.children[ch], word, indx+1, pattern, output)
                    word.pop()
                else:
                    word.append(ch)
                    self._searchPattern(node.children[ch], word, indx, pattern, output)
                    word.pop()



#list = ['pass',"paat", "pam","jan","pans","paan","pns","pens"]
list = ["pans","pns","pens","pnt",'pass',"paat", "pam","jan","paan","pts"]
list = ["pen"]
t = Trie()
for word in list:
    t.addword(word)
print(t.searchPattern("p.*"))