class Node:
    def __init__(self, val):
        self.val =  val
        #self.left = None
        #self.right = None
        #self.visited = False
        self.children = []
        self.parents = []
        self.maxDepth = 0

    def addChild(self, n):
        self.children.append(n)
        n.ancestors.extend(self.ancestors)
        n.ancestors.append(self)
        if n.maxDepth < self.maxDepth + 1:
            n.maxDepth = self.maxDepth + 1

    def printAncestors(self):
        print("Ancestors of ", self.val)
        for x in self.ancestors:
            print("Parent = ", x.val, ", Depth = ", x.maxDepth, "\n")



def LCA(root, x, y):
    if root == None:
        return -1

    xN = findNode(root, x)
    yN = findNode(root, y)

    if xN == yN:
        return xN.val

    if xN == None or yN == None:
        return -1

    deepestAncestorDepth = -1
    deepestAncestor = None 








def findNode(node, val):
    if node.val == val:
        return node
    elif len(node.children) != 0:
        for x in node.children:
            n = findNode(x,val)
            if n != None:
                return n
    else:
        return None
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
