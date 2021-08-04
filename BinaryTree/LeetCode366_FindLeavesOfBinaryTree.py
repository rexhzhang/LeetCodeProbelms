"""
Given a binary tree, collect a tree's nodes as if you were doing this: Collect and remove all leaves, repeat until the tree is empty.



Example:

Input: [1,2,3,4,5]

          1
         / \
        2   3
       / \
      4   5

Output: [[4,5,3],[2],[1]]


Explanation:

1. Removing the leaves [4,5,3] would result in this tree:

          1
         /
        2


2. Now removing the leaf [2] would result in this tree:

          1


3. Now removing the leaf [1] would result in the empty tree:

          []
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    def helper(self, node, array):

        if node:
            left, L_flag = self.helper(node.left, array)
            if node.left is None and node.right is None:
                left.append(node.val)
                current_flag = True
            else:
                current_flag = False

            right, R_flag = self.helper(node.right, left)

            if L_flag:
                node.left = None
            if R_flag:
                node.right = None

            return right, current_flag

        return array, False

    def findLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        if root is None:
            return []

        answer = []

        while root.left or root.right:
            leaves, _ = self.helper(root, [])
            answer.append(leaves)

        answer.append([root.val])
        return answer