class Node:
    def __init__(self,val):
        self.val = val
        self.neighbours = set([])

    def addNbr(self, nbr):
        self.neighbours.add(nbr)

def clone_graph(node):

    cloned = {}
    __clone_graph(node,cloned)

def __clone_graph(node, cloned):

    if node in cloned:
        return cloned[node]
    c = Node(node.val)
    cloned[v] = c
    for nbr in node.neighbours:
        c.addNbr(__clone_graph(nbr,cloned))
    return c


