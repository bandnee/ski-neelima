class Node :
    def __init__(self):
        self.next = None
        self.val = None
        self.random_node = None


    def printList(self,Node):
        while (Node):
            print("val" , Node.val)
            if Node.next :
                print("node_next_val", Node.next.val)
            if Node.random_node:
                print("node_random_val", Node.random_node.val)
            Node = Node.next

    def getNode(self,node,num):
        while(node):
            if node.val == num :
                return node
            else:
                node = node.next




#second Cut :
def cloneList2(orig_node):

    # Step1: Create a node and insert btwn 1st and 2nd and copy the 1st val to the clone node and so on
    clone = None
    onode_itr = orig_node

    while onode_itr != None :
        onext = onode_itr.next
        onode_itr.next = Node()
        onode_itr.next.val = onode_itr.val
        if clone == None:
            clone = onode_itr.next
        onode_itr.next.next = onext
        onode_itr = onode_itr.next.next


    #Step2: Trace the original's arbit pointer's next and set the clone's arbit pointer
    orig_itr = orig_node
    clone_itr = clone
    while clone_itr != None:
        clone_itr.random_node = orig_itr.random_node.next
        orig_itr = orig_itr.next.next
        if clone_itr.next != None:
            clone_itr = clone_itr.next.next
        else:
            clone_itr = None


    #Step3: Reestablish the original's next pointer and clone's next pointer to their original next's
    orig_itr = orig_node
    clone_itr = clone
    while clone_itr != None:
        if orig_itr.next != None :
            orig_itr.next = orig_itr.next.next
        else :
            orig_itr.next = None
        if clone_itr.next != None:
            clone_itr.next = clone_itr.next.next
        else:
            clone_itr.next = None
        orig_itr = orig_itr.next
        clone_itr = clone_itr.next

    return clone


#Build a doubly linked list with random pointers
a_lnos = [7,9,4,2,1,8,6,5,3]

lnos =   [1,2,3,4,5,6,7,8,9]
head_node = None
prev_node = None
for i in range(len(lnos)):
    node = Node()
    node.val = lnos[i]
    if head_node == None:
        head_node = node
    if prev_node != None:
        prev_node.next = node
    prev_node = node



t_node = head_node
for i in range(len(a_lnos)):
    arbit_node = head_node.getNode(head_node,a_lnos[i])
    t_node.random_node = arbit_node
    t_node = t_node.next

#head_node.printList(head_node)

clone = cloneList2(head_node)

clone.printList(clone)
#head_node.printList(head_node)