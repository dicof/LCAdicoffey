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

def vertices(self):
    return list(self.__graph_dict.keys())

def edges(self):
    return self.__graph_dict.__generate_edges()

def add_vertex(self, vertex):
    if vertex not in self.__graph_dict:
        self.__graph_dict[vertex] = []

def add_edge(self, edge):
    if len(edge) != 2:
            return

    vertex1, vertex2 = edge
    if vertex1 in self.__graph_dict and vertex2 in self.__graph_dict:
            self.__graph_dict[vertex1].append(vertex2)
    else:
            self.add_vertex(vertex2)
            self.add_vertex(vertex1)
            self.__graph_dict[vertex1].append(vertex2)

def __generate_edges(self):
        edges = []
        for vertex in self.__graph_dict:
            for neighbour in self.__graph_dict[vertex]:
                s = [vertex, neighbour]
                if s not in edges:
                    edges.append( s )
        return edges

def __str__(self):
        res = "vertices: "
        for k in self.__graph_dict:
            res += str(k) + ", "
        res += "edges: "
        for edge in self.__generate_edges():
            res += str(edge) + " "
        return res
