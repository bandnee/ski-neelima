# Complete the function below.
#!/bin/python

import sys
import os

class Node(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def createTree(data):
    def deserialize():
        val = next(vals,None)
        if val == None:
            return None
        if val == '#':
            return None
        node = Node(int(val))
        node.left = deserialize()
        node.right = deserialize()
        return node
    vals = iter(data.split())
    return deserialize()

def isBST(root):
    return (checkBST(root, None, None))

#Wrong one
def checkBST(root, left, right):
    if root == None:
        return True
    # if left node exist that check it has correct data or not
    if (left != None and root.val < left.val):
        return False
    if (right != None and root.val > right.val):
        return False

    return (checkBST(root.left, left, root) and checkBST(root.right, root, right))


# Python program to check if a binary tree is bst or not

INT_MAX = 4294967296
INT_MIN = -4294967296



# Returns true if the given tree is a binary search tree
# (efficient version)
def isBST(node):
    return (isBSTUtil(node, INT_MIN, INT_MAX))


# Retusn true if the given tree is a BST and its values
# >= min and <= max
def isBSTUtil(node, mini, maxi):
    # An empty tree is BST
    if node is None:
        return True

    # False if this node violates min/max constraint
    if node.val < mini or node.val > maxi:
        return False

    # Otherwise check the subtrees recursively
    # tightening the min or max constraint
    if (not isBSTUtil(node.left, mini, node.val - 1)):
        return False
    if ( not isBSTUtil(node.right, node.val + 1, maxi)) :
        return False
    return True
