#543
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.dia=0

        def depth(n):
            if not n:
                return 0

            l=depth(n.left) 
            r=depth(n.right) 
            self.dia=max(self.dia,l+r)

            return 1+max(l,r)

        depth(root)

        return self.dia
        