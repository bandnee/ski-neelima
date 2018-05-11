class Node:
    def __init__(self,val):
        self.val = val
        self.neighbours = set([])

    def addNbr(self, nbr):
        self.neighbours.add(nbr)

class Graph:
    def __init__(self):
        self.nodeMap = {}
    def addNode(self,node):
        self.nodeMap[node.val] = node

    def printGraph(self):
        for nodeval in self.nodeMap.keys():
            for nbr in self.nodeMap[nodeval].neighbours:
                print(nodeval, ":", nbr.val)


def pnn(node):
    visited = set([])
    _dfs_pnn(node,visited)

def _dfs_pnn(node, visited):
    if node in visited:
        return
    #print (node.val,":")
    visited.add(node)
    for nbr in node.neighbours:
        print(node.val,":",nbr.val)
        _dfs_pnn(nbr,visited )
    return



def build_other_graph(in_node):
    nMap = Graph()
    __build_adjList(in_node, nMap)
    ntMap = Graph()
    for node in nMap.nodeMap.keys():
        __build_transpose(nMap.nodeMap[node],ntMap)
    ntMap.printGraph()



def __build_transpose(node,ntMap):
    transp_nbrNode = None
    transp_thisNode = None
    if node.val in ntMap.nodeMap.keys():
        transp_nbrNode = ntMap.nodeMap[node.val]
    else:
        transp_nbrNode = Node(node.val)
        ntMap.nodeMap[node.val] = transp_nbrNode

    for nbr_node in node.neighbours:
        if  nbr_node.val in ntMap.nodeMap.keys():
            ntMap.nodeMap[nbr_node.val].addNbr(transp_nbrNode)
        else:
            transp_thisNode = Node(nbr_node.val)
            transp_thisNode.addNbr(transp_nbrNode)
            ntMap.nodeMap[nbr_node.val] = transp_thisNode



def __build_adjList(node, nMap):
    if node.val  in nMap.nodeMap.keys():
        return
    nMap.addNode(node)
    for nbr_node in node.neighbours:
        __build_adjList(nbr_node,nMap)


def build_dfs_graph(node):
    nDictV = {}
    return(__build_dfs_graph(node, nDictV))

def __build_dfs_graph(node, transpDict):
    # given a random node , get it's a

    # Make the neighbour as a key and add the key as a value
    # If the key exists in the Graph, then add this current node as the value of the
    # for the new graph key
    if  node in transpDict.keys():
        return transpDict[node]

    #create the 2nd graph nodes
    nodet = Node(node.val)
    #traverse the first graph, and mark visited
    transpDict[node] = nodet
    for nbr_node in node.neighbours:
        __build_dfs_graph(nbr_node,transpDict).addNbr(nodet)
    return nodet


# Create a fully connected node
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n1.addNbr(n3)
n2.addNbr(n1)
n3.addNbr(n2)

pnn(n1)

tr_node = build_dfs_graph(n1)

pnn(tr_node)


