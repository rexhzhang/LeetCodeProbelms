"""
Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

For example:
Given the below binary tree and sum = 22,
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1
return
[
   [5,4,11,2],
   [5,8,4,5]
]
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        result = []

        def helper(node, valueList, currentSum):
            if node:
                currentSum = currentSum + node.val
                valueList = valueList + [node.val]
                if node.left is None and node.right is None and currentSum == sum:
                    result.append(valueList)

                helper(node.left, valueList, currentSum)
                helper(node.right, valueList, currentSum)

        helper(root, [], 0)

        return result
