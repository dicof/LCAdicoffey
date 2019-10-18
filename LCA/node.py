class Node:
    def __init__(self, val):
        self.val =  val
        self.left = None
        self.right = None
        self.visited = False

# def lowestCommonAncestor(root, x, y):
#
#     path1 = []
#     path2 = []
#
#     if (not findPath(root, path1, x) or not findPath(root, path2, y)):
#         return -1
#
#
#     i = 0
#     while(i < len(path1) and i < len(path2)):
#         if path1[i] != path2[i]:
#             break
#         i += 1
#     return path1[i-1]


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


def lowestCommonAncestor(root, x, y):
    if (root is None):
        return -1
    else:
        if (root.left is None and root.right is None and (x is not y)):
            return -1
    return LCARecursive(root, x, y, [False], [False])


def LCARecursive(root, x, y, path1, path2):
    if (root is None):
        return -1
    if (root.visited is True):
        return -1

    left = LCARecursive(root.left, x, y, path1, path2)
    right = LCARecursive(root.right, x, y, path1, path2)

    if(root.val is x):
        path1[0] = True
        return root.val

    if(root.val is y):
        path2[0] = True
        return root.val

    if(path1[0] is True and path2[0] is True):
        if (left is not -1 and right is not -1):
            return root.val
        elif(left is not -1):
            return left
        else:
            return right

    if (left is not -1):
        return left
    if(right is not -1):
        return right

    return -1
