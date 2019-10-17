#Test file for lcadag
import unittest
import lcadag


class test_lcadag(unittest.TestCase):

    root = Node.Node(1)
    r2 = Node.Node(2)
    r3 = Node.Node(3)
    r4 = Node.Node(4)
    r5 = Node.Node(5)
    r6 = Node.Node(6)
    root.succ = [r2,r3,r4,r5]
    r2.succ = [r4]
    r2.pred = [root]
    r3.succ = [r4, r5]
    r3.pred = [root]
    r4.succ = [r5]
    r4.pred = [r2,r3,root]
    r5.pred = [r3,r4,root]
    r6.pred = [r4]

    def test_basicTree(self):

    def test_nullTree(self):

    def test_invalidNode(self):

    def test_LCAisNode(self):

    
