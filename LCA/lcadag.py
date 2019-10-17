##DAG

class Node:

    def __init__(self, val):
        self.val = val
        self.pred = []
        self.succ = []

def LCA(root, x, y):

    if root is None:
        return -1

    if root.val == x.val or root.val == y.val:
        return root.val

    if x == y:
        return x.val;
    lca = []
    i = 0
    while(i<len(x.pred)):
        j = 0
        while(j<len(y.pred)):
            if(x.pred[i].val == y.pred[j].val):
                lca.append(x.pred[i].val)
                j+=1
            else:
                j+=1
        i+=1

    if(lca == []):
        if(x.val > y.val):
            lca.append(dagLCA(root, x.pred[0], y))
        else:
            lca.append(dagLCA(root,x,y,pred[0]))

    return max(lca)

##Attempt 2
class DAG:
    def __init__(self, graph_dict=None):
        if graph_dict == None:
            graph_dict = {}
        self.__graph_dict = graph_dict
