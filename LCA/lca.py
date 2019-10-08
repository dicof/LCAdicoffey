import unittest
import node


class test_node(unittest.TestCase):

    def test_basicTree(self):
        root = node.Node(1)                      #  1
        root.left = node.Node(2)                # /   \
        root.right = node.Node(3)              # 2     3
        root.left.left = node.Node(4)         #/  \   / \
        root.left.right = node.Node(5)       #4   5  6  7
        root.right.left = node.Node(6)
        root.right.right = node.Node(7)
        self.assertEqual(2, node.lowestCommonAncestor(root, 4, 5))
        self.assertEqual(1, node.lowestCommonAncestor(root, 6, 5))

    def test_nullTree(self):
        root = None
        self.assertEqual(-1, node.lowestCommonAncestor(root, 4, 5), 'Empty tree returns -1')
        self.assertEqual(-1, node.lowestCommonAncestor(None, 0, 0), 'Empty tree returns -1')


    def test_InvalidNode(self):
        root = node.Node(1)
        root.left = node.Node(2)
        root.right = node.Node(3)
        root.left.left = node.Node(4)
        root.left.right = node.Node(5)
        root.right.left = node.Node(6)
        root.right.right = node.Node(7)
        self.assertEqual(-1, node.lowestCommonAncestor(root, 4, 8), "Unfound node returns -1")

    def test_commonAncestorIsNode(self):
        root = node.Node(1)
        root.left = node.Node(2)
        root.right = node.Node(3)
        root.left.left = node.Node(4)
        root.left.right = node.Node(5)
        root.right.left = node.Node(6)
        root.right.right = node.Node(7)
        self.assertEqual(2, node.lowestCommonAncestor(root, 2, 4), "Common Ancestor of 2 & 4 is 2 itself")
        self.assertEqual(2, node.lowestCommonAncestor(root, 2, 2), "Common Ancestor of 2 & 2 is 2 itself")
        self.assertEqual(2, node.lowestCommonAncestor(root, 4, 2), "Common Ancestor of 4 & 2 is 2 itself")

    def test_extremeInputs(self):
        root = node.Node(-1000000000000000)
        root.left = node.Node(2.5)
        root.right = node.Node(-3.3)
        self.assertEqual(-1000000000000000, node.lowestCommonAncestor(root, 2.5, -3.3), "Common ancestor -1000000000000000")
        root.left.left = node.Node('seven')
        root.left.right = node.Node('crazy')
        self.assertEqual(2.5, node.lowestCommonAncestor(root, 'seven', 'crazy'), "Common ancestor 2.5")



if __name__ == '__main__':
    unittest.main()
