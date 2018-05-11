

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def BSTtoLL1(root):
    # Do a inorder traversal recursively and insert it into a DLL.
    if root == None:
        return None
    else:
        left = BSTtoLL(root.left)
        right = BSTtoLL(root.right)
        # point the root to itself , if that is the only element
        root.left = root.right = root
        # concatenate the left,root and right  nodes
        ll = concatenate(left, root)
        lr = concatenate(ll, right)
        return lr

def BSTtoLL(root):
    # Do a inorder traversal recursively and insert it into a DLL.\
    prev = None
    head = None
    BSTtoLLInorder(root,prev,head)
    return head

def BSTtoLLInorderWrong(root,prev,head):
    # Do a inorder traversal recursively and insert it into a DLL.
    if root == None:
        return None
    else:
        if prev == None:
            head = root
        else :
            BSTtoLLInorder(root.left,prev,head)
            root.left = prev
            prev.right = root
            prev = root
            BSTtoLLInorder(root.right,prev,head)
    return

class DoubleLinkedList:
    def __init__(self):
        self.head = None

    def append(self, node):
        if self.head == None:
            node.left, node.right = node, node
            self.head = node
        else:
            h = self.head
            t = self.head.left

            node.left, node.right = t, h
            t.right, h.left = node, node

    def appendAll(self, cur_node):
        if self.head == None:
            self.head = cur_node
        else:
            h1 = self.head
            t1 = self.head.left

            h2 = cur_node
            t2 = cur_node.left

            h1.left = t2
            t1.right = h2
            h2.left = t1
            t2.right = h1

    def print(self):
        if self.head == None:
            return

        h = self.head
        print(h.val)
        h=h.right
        while h != self.head:
            print(h.val)
            h = h.right


def BSTtoLLInorderClean(root, dll):
    if root == None:
        return

    BSTtoLLInorderClean(root.left, dll)
    right = root.right
    dll.append(root)
    BSTtoLLInorderClean(right, dll)

def find_path(cur_node,n1val,path):
    if cur_node == None :
        return False
    path.append(cur_node.val)
    if n1val < cur_node.val  :
        find_path(cur_node.left,n1val)
    elif n1val > cur_node.val :
        find_path(cur_node.right, n1val)
    elif n1val == cur_node.val  :
        return True

def LCA(cur_node, n1val,n2val):
    path1 = []
    path2 = []
    lca
    if(find_path(cur_node,n1val) and find_path(cur_node.left,n1val)):
        #find the last common node
        for i in range(path1):
            if path1[i] != path2[i]:
                lca = path1[i-1]
                break
    else:
        lca =  -1
    return lca


    else:
        return -1


def LCA(cur_node, n1val,n2val):
    if cur_node == None:
        return None
    #if cur_node.val == n1val or cur_node.val == n2val
    #lcm is in the previous nodes
    prev_node = cur_node.val
    if cur_node.val > n1val and cur_node.val > n2val:
        lca = LCA(cur_node.left,prev_node,n1val,n2val)
    elif cur_node.val < n1val and cur_node.val < n2val:
        lca = LCA(cur_node.right, prev_node, n1val, n2val)
    elif (n1val > cur_node.val  and n2val < cur_node.val ):
        if (isNode(cur_node.right, n1val) and isNode(cur_node.left, n2val)):
            return cur_node.val
        else:
            return None
    elif(n1val < cur_node.val  and n2val > cur_node.val ):
        if (isNode(cur_node.left, n1val) and isNode(cur_node.right, n2val)):
            return cur_node.val
        else:
            return None
    elif((n1val == cur_node.val and n2val == cur_node.val)):
        return cur_node.val
    elif ((n1val == cur_node.val)):
        if ( n2val > cur_node.val):
            if(isNode(cur_node.right, n2val)) :
                return cur_node.val
            else:
                return None
        else:
            if (isNode(cur_node.left, n2val)):
                return cur_node.val
            else:
                return None
    else:
        return None


def constructBST(l1,start,end):
    if start > end :
        return None
    else:
        mid = int((start + end)/2)
        root = Node(l1[mid])
        root.left =  constructBST(l1,start,mid-1)
        root.right = constructBST(l1,mid+1,end)
        return root

def inorder_traversal_rl(root):
    if root == None:
        return([])
    else:
        fl = []
        if (root.left != None):
            ll = inorder_traversal_rl(root.left)
            fl = fl + ll
        fl.append(root.val)
        if (root.right != None):
            rl = inorder_traversal_rl(root.right)
            fl = fl + rl
        return fl

def printCLL(cll):
    first_element = cll.val
    print(cll.val)
    cll = cll.right
    while (cll.val != first_element):
        print(cll.val)
        cll = cll.right


l1 = [1,2,3,4,5,6,7]
l2 = [1,2,3,4,5,6,7,8,9,10]
my_bst = constructBST(l1,0,len(l1)-1)
linorder = inorder_traversal_rl(my_bst)
print("inorder traversal")
print(linorder)
dll = DoubleLinkedList()
prevNode
LCA(my_bst,)
#BSTtoLLInorderClean(my_bst, dll)
dll.print()



