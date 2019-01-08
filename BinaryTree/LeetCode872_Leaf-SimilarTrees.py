# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    def findLeafNode(self, node, arr):

        if node:
            left = self.findLeafNode(node.left, arr)
            if node.left is None and node.right is None:
                left.append(node.val)
            right = self.findLeafNode(node.right, left)

            return right

        return arr

    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        root1List = []
        root2List = []

        self.findLeafNode(root1, root1List)
        self.findLeafNode(root2, root2List)

        for a, b in zip(root1List, root2List):
            if a != b:
                return False

        return True