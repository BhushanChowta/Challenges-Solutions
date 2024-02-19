#110
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def height(node):
            if node is None:
                return 0
            
            leftH=height(node.left)
            rightH=height(node.right)

            if leftH == -1 or rightH == -1 or abs(leftH-rightH) > 1:
                return -1
            
            return 1+max(leftH,rightH)

        return height(root)!=-1
    