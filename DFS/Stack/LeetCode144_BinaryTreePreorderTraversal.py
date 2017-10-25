"""
Given a binary tree, return the preorder traversal of its nodes' values.

For example:
Given binary tree {1,#,2,3},
   1
    \
     2
    /
   3
return [1,2,3].

Note: Recursive solution is trivial, could you do it iteratively?
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversalRecursion(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        preorder = []

        def helper(node):
            if node is None:
                return
            preorder.append(node.val)
            helper(node.left)
            helper(node.right)

        helper(root)
        return preorder

    def preorderTraversalStack(self, root):
        if root is None:
            return []
        preorder = []
        stack = [root]

        while stack:
            node = stack.pop()
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
            preorder.append(node.val)

        return preorder