"""
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # O(n^2) worst case Time Complexity
        # O(n) stack space
        if not root: return True
        left = self.depth(root.left)
        right = self.depth(root.right)
        return abs(left - right) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)

    def depth(self, root):
        if not root: return 0
        return max(self.depth(root.left), self.depth(root.right)) + 1


    def isBalanced2(self, root):
        def helper(node):
            if node is None: return 0
            L = self.isBalanced2(node.left)
            if L == -1: return -1
            R = self.isBalanced2(node.right)
            if R == -1: return -1
            return max(L, R) + 1 if abs(L-R) <= 1 else -1
        return helper(root) == -1