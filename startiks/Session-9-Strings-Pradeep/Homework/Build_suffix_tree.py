

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
        self._collect_all(self,currentNode,word,wordList)
        return wordList

    def _collect_all(self,Node,word,wList):
        currentNode = Node
        if currentNode.word_ending :
            wList.append("".join(word))
        if currentNode == None:
            return
        for ch in currentNode.children.keys():
            word.append(ch)
            _collect_all(self,currentNode[ch],word,wList)
        word.pop()

