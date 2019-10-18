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

    #
    # def test_BasicTree(self):
    #     root = node.Node(1)                      #  1
    #     root.left = node.Node(2)                # /   \
    #     root.right = node.Node(3)              # 2     3
    #     root.left.left = node.Node(4)         #/  \   / \
    #     root.left.right = node.Node(5)       #4   5  6  7
    #     root.right.left = node.Node(6)
    #     root.right.right = node.Node(7)
    #     self.assertEqual(2, node.lowestCommonAncestor(root, 4, 5))
    #     self.assertEqual(1, node.lowestCommonAncestor(root, 6, 5))
    #
    # def test_NullTree(self):
    #     root = None
    #     self.assertEqual(-1, node.lowestCommonAncestor(root, 4, 5), 'Empty tree returns -1')
    #     self.assertEqual(-1, node.lowestCommonAncestor(None, 0, 0), 'Empty tree returns -1')
    #
    #
    # def test_InvalidNode(self):
    #     root = node.Node(1)
    #     root.left = node.Node(2)
    #     root.right = node.Node(3)
    #     root.left.left = node.Node(4)
    #     root.left.right = node.Node(5)
    #     root.right.left = node.Node(6)
    #     root.right.right = node.Node(7)
    #     self.assertEqual(-1, node.lowestCommonAncestor(root, 4, 8), "Unfound node returns -1")
    #
    # def test_CommonAncestorIsNode(self):
    #     root = node.Node(1)
    #     root.left = node.Node(2)
    #     root.right = node.Node(3)
    #     root.left.left = node.Node(4)
    #     root.left.right = node.Node(5)
    #     root.right.left = node.Node(6)
    #     root.right.right = node.Node(7)
    #     self.assertEqual(2, node.lowestCommonAncestor(root, 2, 4), "Common Ancestor of 2 & 4 is 2 itself")
    #     self.assertEqual(2, node.lowestCommonAncestor(root, 2, 2), "Common Ancestor of 2 & 2 is 2 itself")
    #     self.assertEqual(2, node.lowestCommonAncestor(root, 4, 2), "Common Ancestor of 4 & 2 is 2 itself")
    #
    # def test_ExtremeInputs(self):
    #     root = node.Node(-1000000000000000)
    #     root.left = node.Node(2.5)
    #     root.right = node.Node(-3.3)
    #     self.assertEqual(-1000000000000000, node.lowestCommonAncestor(root, 2.5, -3.3), "Common ancestor -1000000000000000")
    #     root.left.left = node.Node('seven')
    #     root.left.right = node.Node('crazy')
    #     self.assertEqual(2.5, node.lowestCommonAncestor(root, 'seven', 'crazy'), "Common ancestor 2.5")
    #
    #
    # def test_LeftLeaningTree(self):
    #     # testing a left leaning tree
    #     #
    #     #                         1
    #     #                       /
    #     #                     2
    #     #                   /
    #     #                 3
    #     #               /
    #     #             4
    #     #           /
    #     #         5
    #     #       /
    #     #     6
    #     #   /
    #     # 7
    #     root = node.Node(1)
    #     root.left = node.Node(2)
    #     root.left.left = node.Node(3)
    #     root.left.left.left = node.Node(4)
    #     root.left.left.left.left = node.Node(5)
    #     root.left.left.left.left.left = node.Node(6)
    #     root.left.left.left.left.left.left = node.Node(7)
    #
    #     self.assertEqual(node.lowestCommonAncestor(root, 1, 2), 1, "Should return 1")
    #     self.assertEqual(node.lowestCommonAncestor(root, 7, 2), 2, "Should return 2")
    #     self.assertEqual(node.lowestCommonAncestor(root, 4, 6), 4, "Should return 4")
    #
    # def test_RightLeaningTree(self):
    #     #   testing a right leaning tree
    #     #
    #     #   1
    #     #    \
    #     #     2
    #     #      \
    #     #       3
    #     #        \
    #     #         4
    #     #          \
    #     #           5
    #     #            \
    #     #             6
    #     #              \
    #     #               7
    #     root = node.Node(1)
    #     root.right = node.Node(2)
    #     root.right.right = node.Node(3)
    #     root.right.right.right = node.Node(4)
    #     root.right.right.right.right = node.Node(5)
    #     root.right.right.right.right.right = node.Node(6)
    #     root.right.right.right.right.right.right = node.Node(7)
    #
    #     self.assertEqual(node.lowestCommonAncestor(root, 1, 2), 1, "Should return 1")
    #     self.assertEqual(node.lowestCommonAncestor(root, 7, 2), 2, "Should return 2")
    #     self.assertEqual(node.lowestCommonAncestor(root, 4, 6), 4, "Should return 4")
    #
    # def test_TreeOfOneElement(self):
    #     # create one element tree
    #     # test one element tree
    #     root = node.Node(1)
    #
    #     self.assertEqual(node.lowestCommonAncestor(root, 1, 2), -1, "Should return -1")
    #     self.assertEqual(node.lowestCommonAncestor(root, 1, 1), 1, "Should return 1")
    #     self.assertEqual(node.lowestCommonAncestor(root, 6, 7), -1, "Should return -1")
    #
    #
    #
    # def test_DAG(self):
    #     root = node.Node(1)                      #  1
    #     root.left = node.Node(2)                # /   \
    #     root.right = node.Node(3)              # 2     3
    #     root.left.right = node.Node(4)        # / \  /  \
    #     root.right.left = root.left.right  #       4
    #
    #
    #     self.assertEqual(node.lowestCommonAncestor(root, 4, 3), 3, "Should be 3")
    #
    #

    def test_basicTree(self):
        root = createTree()
        self.assertEqual(2, node.LCA(root, 4, 5))
        self.assertEqual(1, node.LCA(root, 4, 6))



if __name__ == '__main__':
    unittest.main()
