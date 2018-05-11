# Complete the function below.


def printAllPaths(root):
    path = ""
    return (paps_r(root, path))


# First i did this, but the extra elif's are  not required
def pap(root, path):
    if root == None:
        return
    if (root.left == None and root.right == None):
        path = path + str(root.val) + " "
        print
        path
        return
    elif (root.left == None):
        path = path + str(root.val) + " "
        pap(root.right, path)
    elif (root.right == None):
        path = path + str(root.val) + " "
        pap(root.left, path)
    else:
        path = path + str(root.val) + " "
        pap(root.left, path)
        pap(root.right, path)
    return


def paps_r(root, path):
    if root == None:
        return
    elif (root.left == None and root.right == None):
        path = path + str(root.val) + " "
        print
        path
        return
    else:
        path = path + str(root.val) + " "
        pap(root.left, path)
        pap(root.right, path)
        return

