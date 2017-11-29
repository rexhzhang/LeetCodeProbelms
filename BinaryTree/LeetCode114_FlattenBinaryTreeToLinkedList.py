"""
Given a binary tree, flatten it to a linked list in-place.

For example,
Given

         1
        / \
       2   5
      / \   \
     3   4   6
The flattened tree should look like:
   1
    \
     2
      \
       3
        \
         4
          \
           5
            \
             6
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if root is None: return None

        def helper(root):
            if root.left is None and root.right is None:
                return root
            elif root.left is None:
                right = helper(root.right)
                return right
            elif root.right is None:
                left = helper(root.left)
                root.right = root.left
                root.left = None
                return left
            else:
                left = helper(root.left)
                right = helper(root.right)
                temp = root.right
                root.right = root.left
                root.left = None
                left.right = temp
                return right

        helper(root)


class SolutionII:
    lastNode = None

    def flatten(self, root):
        # write your code here
        if root is None:
            return

        if self.lastNode != None:
            self.lastNode.left = None
            self.lastNode.right = root

        self.lastNode = root
        right = root.right
        self.flatten(root.left)
        self.flatten(right)
