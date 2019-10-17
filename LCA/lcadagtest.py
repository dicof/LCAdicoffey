#Test file for lcadag
import unittest
import lcadag


class test_lcadag(unittest.TestCase):



    def test_basicTree(self):
        root = lcadag.Node(1)
        r2 = lcadag.Node(2)
        r3 = lcadag.Node(3)
        r4 = lcadag.Node(4)                               #              ----1-----
        r5 = lcadag.Node(5)                                         #  /   /   \   \
        r6 = lcadag.Node(6)                                        # 2    /    3   \
        root.succ = [r2,r3,r4,r5]                               #   \ /      /\  \
        r2.succ = [r4]                                      #        4------- \  /
        r2.pred = [root]                                    #        \---------5
        r3.succ = [r4, r5]
        r3.pred = [root]
        r4.succ = [r5]
        r4.pred = [r2,r3,root]
        r5.pred = [r3,r4,root]
        r6.pred = [r4]
        self.assertEqual(lcadag.LCA(root,r2, r3), 1, "Should be 1")
        self.assertEqual(lcadag.LCA(root,r1, r5), 1, "Should be 1")
        self.assertEqual(lcadag.LCA(root,r4, r3), 3, "Should be 3")
        self.assertEqual(lcadag.LCA(root,r5, r2), 2, "Should be 2")


    # def test_nullTree(self):
    #
    # def test_invalidNode(self):
    #
    # def test_LCAisNode(self):

if __name__ == '__main__':
    unittest.main()
