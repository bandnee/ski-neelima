from collections import deque


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def add(node, root):
    if root is None:
        raise ValueError('root cannot be None.')

    nodes_found = deque([root])

    while len(nodes_found) > 0:
        current_node = nodes_found.popleft()

        if current_node.left is None:
            current_node.left = node
            break
        if current_node.right is None:
            current_node.right = node
            break

        nodes_found.append(current_node.left)
        nodes_found.append(current_node.right)

def inorder_traversal(root,node_list):
    #Got to the leftmost node untill it hits none
    # add to list
    # go to it's  parent and add to the list
    # go to the root's right  and add right to the list
    if root == None:
        return
    else:
        if (root.left != None):
            inorder_traversal(root.left,node_list)
        node_list.append(root.val)
        if (root.right != None):
            inorder_traversal(root.right,node_list)
        return

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

def mergelists(l1,l2):
    l3 = []
    #Iterate over the lists
    while l1 and l2:
        if l1[0] <= l2[0]:
            l3.append(l1[0])
            del(l1[0])
        else:
            l3.append(l2[0])
            del(l2[0])
    while l1:
        l3.append(l1[0])
        del(l1[0])
    while l2:
        l3.append(l2[0])
        del(l2[0])
    return l3


def constructBST(l1,start,end):
    if start > end :
        return None
    else:
        mid = int(start + end)/2
        root = Node(l1[mid])
        root.left =  constructBST(l1,start,mid-1)
        root.right = constructBST(l1,mid+1,end)
        return root




root1 = Node(8)
vals = [4, 12, 2, 6, 10, 14, 1, 3, 5, 7, 9, 11, 13, 15]

for value in vals:
    add(Node(value), root1)


root2 = Node(28)
vals = [24, 32, 22, 26, 30, 34, 21, 23, 25, 27, 29, 31, 33, 35]

for value in vals:
    add(Node(value), root2)
#l1 = []
#inorder_traversal(root,l1)
#print (l1)

l1 = inorder_traversal_rl(root1)
l2 = inorder_traversal_rl(root2)
print (l1)
print (l2)
l3 = mergelists(l1,l2)
print (l3)