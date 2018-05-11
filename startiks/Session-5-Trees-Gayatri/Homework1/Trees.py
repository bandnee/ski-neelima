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

    inorder_traversal(root.left,node_list)
    node_list.append(root.val)
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
