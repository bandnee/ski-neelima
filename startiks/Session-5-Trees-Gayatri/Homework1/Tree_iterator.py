# Enter your code here. Read input from STDIN. Print output to STDOUT
# Keep pushing from root to the last right element.

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class BSTIterator:

    def __init__(self, bst):
        self.itr_stack = []
        if bst == None:
            print("Bad BST ")
            return
        self.stackMax(bst)
        return

    def stackMax(self, node):
        if node == None:
            return
        self.itr_stack.append(node)
        self.stackMax(node.right)

    def next(self):
        this_node = self.itr_stack.pop()
        if this_node.left != None:
            self.stackMax(this_node.left)
        return this_node.val


    def hasNext(self):
        if len(self.itr_stack) == 0:
            return False
        else:
            return True



def constructBST(l1,start,end):
    if start > end :
        return None
    else:
        mid = int((start + end)/2)
        root = Node(l1[mid])
        root.left =  constructBST(l1,start,mid-1)
        root.right = constructBST(l1,mid+1,end)
        return root

l2 = [1,2,3,4,5,6,7,8,9,10]
#l2 = [1,2,3,4,5]
my_bst = constructBST(l2,0,len(l2)-1)
bst_itr = BSTIterator(my_bst)

while bst_itr.hasNext():
    val = bst_itr.next()
    print(val)




