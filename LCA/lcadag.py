##DAG

class Node:

    def __init__(self, val):
        self.val = val
        self.pred = []
        self.succ = []

    def dagLCA(root, x, y):
