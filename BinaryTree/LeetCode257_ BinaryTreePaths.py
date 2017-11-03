"""
Given a binary tree, return all root-to-leaf paths.

For example, given the following binary tree:

   1
 /   \
2     3
 \
  5
All root-to-leaf paths are:

["1->2->5", "1->3"]
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        answer = []

        def helper(node, path):
            if node:
                if node.left is None and node.right is None: answer.append(path + str(node.val))
                if node.left:
                    helper(node.left, path + str(node.val) + "->")
                if node.right:
                    helper(node.right, path + str(node.val) + "->")

        helper(root, "")
        return answer