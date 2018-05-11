uval = 0
def findSingleValueTrees(node):
    global uval
    if node == None:
        return 0
    findUval(node)
    return (uval)


def findUvalM(node):
    if node == None:
        return (0, True)
    if (node.left == None and node.right == None):
        return (1, True)
    left_subtree_univals = findUvalM(node.left)
    right_subtree_univals = findUvalM(node.right)
    total_subtree_univals = left_subtree_univals[0] + right_subtree_univals[0]
    if node.left != None and node.right != None:
        if ((left_subtree_univals[1] and (node.left.val == node.val)) and
                (right_subtree_univals[1] and (node.right.val == node.val))):
            return (total_subtree_univals + 1, True)
        else:
            return (total_subtree_univals, False)
    elif node.left != None:
        if (left_subtree_univals[1] and (node.left.val == node.val)):
            return (total_subtree_univals + 1, True)
        else:
            return (total_subtree_univals, False)
    else:
        if (right_subtree_univals[1] and (node.right.val == node.val)):
            return (total_subtree_univals + 1, True)
        else:
            return (total_subtree_univals, False)


def findUval(node):
    global uval
    if node.left == None and node.right == None:
        uval += 1
        return True

    if node.left != None:
        if (not findUval(node.left)) or (node.left.val != node.val):
            return False

    if node.right != None:
        if (not findUval(node.right)) or (node.right.val != node.val):
            return False

    if((node.left !=None or (node.left.val != node.val)) or (node.right != None or (node.right.val != node.val))):
            return False

    uval += 1
    return True
