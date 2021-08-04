"""
A binary tree is univalued if every node in the tree has the same value.

Return true if and only if the given tree is univalued.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root.left and root.right:
            left = self.isUnivalTree(root.left)
            right = self.isUnivalTree(root.right)
            return root.val == root.left.val and root.val == root.right.val and left and right

        if root.left:
            left = self.isUnivalTree(root.left)
            return root.val == root.left.val and left

        if root.right:
            right = self.isUnivalTree(root.right)
            return root.val == root.right.val and right

        return True