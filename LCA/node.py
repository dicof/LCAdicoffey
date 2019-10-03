class Node:
    def __init__(self, val):
        self.val =  val
        self.left = None
        self.right = None

def lowestCommonAncestor(root, x, y):


    path1 = []
    path2 = []

    if (not findPath(root, path1, x) or not findPath(root, path2, y)):
        return -1


    i = 0
    while(i < len(path1) and i < len(path2)):
        if path1[i] != path2[i]:
            break
        i += 1
    return path1[i-1]


def findPath( root, path, k):

    if root is None:
        return False

    path.append(root.val)

    if root.val == k :
        return True

    if ((root.left != None and findPath(root.left, path, k)) or
            (root.right!= None and findPath(root.right, path, k))):
        return True


    path.pop()
    return False
