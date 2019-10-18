import unittest
import node
import sys

def createTree():
    root = node.Node(1)
    n2 = node.Node(2)
    n3 = node.Node(3)
    n4 = node.Node(4)
    n5 = node.Node(5)
    n6 = node.Node(6)
    n7 = node.Node(7)
    root.addChild(n2)
    root.addChild(n3)
    n2.addChild(n4)
    n2.addChild(n5)
    n3.addChild(n6)
    n3.addChild(n7)
    return root

def createDAG():
    root = node.Node(1)
    n2 = node.Node(2)
    n3 = node.Node(3)
    n4 = node.Node(4)
    n5 = node.Node(5)
    n6 = node.Node(6)
    n7 = node.Node(7)
    n8 = node.Node(8)
    n9 = node.Node(9)
    n10 = node.Node(10)
    n11 = node.Node(11)
    n12 = node.Node(12)
    n13 = node.Node(13)
    n14 = node.Node(14)
    root.addChild(n2)
    root.addChild(n3)
    n2.addChild(n5)
    n2.addChild(n4)
    n3.addChild(n4)
    n3.addChild(n7)
    n4.addChild(n11)
    n4.addChild(n6)
    n5.addChild(n8)
    n6.addChild(n10)
    n6.addChild(n13)
    n7.addChild(n9)
    n8.addChild(n10)
    n9.addChild(n12)
    n10.addChild(n14)
    n11.addChild(n10)
    n13.addChild(n12)
    n13.addChild(n14)
    return root




class test_node(unittest.TestCase):



    def test_NullTree(self):
        root = None
        self.assertEqual(-1, node.LCA(root, 4, 5), 'Empty tree returns -1')
        self.assertEqual(-1, node.LCA(None, 0, 0), 'Empty tree returns -1')


    # def test_InvalidNode(self):
    #     root = node.Node(1)
    #     root.left = node.Node(2)
    #     root.right = node.Node(3)
    #     root.left.left = node.Node(4)
    #     root.left.right = node.Node(5)
    #     root.right.left = node.Node(6)
    #     root.right.right = node.Node(7)
    #     self.assertEqual(-1, node.LCA(root, 4, 8), "Unfound node returns -1")

    def test_CommonAncestorIsNode(self):
        root = createTree()
        self.assertEqual(2, node.LCA(root, 2, 4), "Common Ancestor of 2 & 4 is 2 itself")
        self.assertEqual(2, node.LCA(root, 2, 2), "Common Ancestor of 2 & 2 is 2 itself")
        self.assertEqual(2, node.LCA(root, 4, 2), "Common Ancestor of 4 & 2 is 2 itself")

    def test_ExtremeInputs(self):
        root = node.Node(-1000000000000000)
        n1 = node.Node(2.5)
        n2 = node.Node(-3.3)
        root.addChild(n1)
        root.addChild(n2)
        self.assertEqual(-1000000000000000, node.LCA(root, 2.5, -3.3), "Common ancestor -1000000000000000")
        n3 = node.Node('seven')
        n4 = node.Node('crazy')
        n1.addChild(n3)
        n1.addChild(n4)
        self.assertEqual(2.5, node.LCA(root, 'seven', 'crazy'), "Common ancestor 2.5")


    def test_LeftLeaningTree(self):
        # testing a long single branched tree
        #
        #                         1
        #                       /
        #                     2
        #                   /
        #                 3
        #               /
        #             4
        #           /
        #         5
        #       /
        #     6
        #   /
        # 7
        root = node.Node(1)
        n2 = node.Node(2)
        n3 = node.Node(3)
        n4 = node.Node(4)
        n5 = node.Node(5)
        n6 = node.Node(6)
        n7 = node.Node(7)
        root.addChild(n2)
        n2.addChild(n3)
        n3.addChild(n4)
        n4.addChild(n5)
        n5.addChild(n6)
        n6.addChild(n7)

        self.assertEqual(node.LCA(root, 1, 2), 1, "Should return 1")
        self.assertEqual(node.LCA(root, 7, 2), 2, "Should return 2")
        self.assertEqual(node.LCA(root, 4, 6), 4, "Should return 4")


    def test_TreeOfOneElement(self):
        # create one element tree
        # test one element tree
        root = node.Node(1)

        self.assertEqual(node.LCA(root, 1, 2), -1, "Should return -1")
        self.assertEqual(node.LCA(root, 1, 1), 1, "Should return 1")
        self.assertEqual(node.LCA(root, 6, 7), -1, "Should return -1")





    def test_basicTree(self):
        root = createTree()
        self.assertEqual(2, node.LCA(root, 4, 5))
        self.assertEqual(1, node.LCA(root, 4, 6))

    def test_multipleRoutes(self):
        root = createDAG()
        # lca.findNode(root, 10).printAncestors() these were for debugging
        # lca.findNode(root, 12).printAncestors()
        self.assertEqual(6, node.LCA(root, 10, 12), "Common Ancestor of 10 & 12 is 6")
        self.assertEqual(2, node.LCA(root, 8, 13), "Common Ancestor of 8 & 13 is 2")
        self.assertEqual(3, node.LCA(root, 6, 9), "Common Ancestor of 6 & 9 is 3")

    def test_multipleParentsStructure(self):
        root = node.Node(1)
        n2 = node.Node(2)
        n3 = node.Node(3)
        n4 = node.Node(4)
        n5 = node.Node(5)
        n6 = node.Node(6)
        n7 = node.Node(7)
        n8 = node.Node(8)
        n9 = node.Node(9)
        n10 = node.Node(10)
        n11 = node.Node(11)
        n12 = node.Node(12)
        n13 = node.Node(13)
        n14 = node.Node(14)
        root.addChild(n2)
        root.addChild(n3)
        root.addChild(n4)
        root.addChild(n5)
        root.addChild(n6)
        root.addChild(n7)
        root.addChild(n8)
        root.addChild(n9)
        root.addChild(n10)
        root.addChild(n11)
        root.addChild(n12)
        root.addChild(n13)
        n2.addChild(n14)
        n3.addChild(n14)
        n4.addChild(n14)
        n5.addChild(n14)
        n6.addChild(n14)
        n7.addChild(n14)
        n8.addChild(n14)
        n9.addChild(n14)
        n10.addChild(n14)
        n11.addChild(n14)
        n12.addChild(n14)
        n13.addChild(n14)
        self.assertEqual(11, node.LCA(root, 14, 11), "Common ancestor of 14 and 11 is 11")
        self.assertEqual(11, node.LCA(root, 14, 1), "Common ancestor of 14 and 11 is 11")





if __name__ == '__main__':
    unittest.main()
