"""
Given a binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along
the parent-child connections. The path must contain at least one node and does not need to go through the root.

For example:
Given the below binary tree,

       1
      / \
     2   3
Return 6.
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    maxSum = -float('inf')

    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None: return 0
        self.helper(root)
        return self.maxSum

    def helper(self, root):
        if root is None: return 0
        left = self.helper(root.left)
        right = self.helper(root.right)

        # 选择当前节点作为终店，查看sum是否比最大值还大
        self.maxSum = max(left + right + root.val, self.maxSum)

        # 继续向上返回call stack,
        sumOfThisPath = root.val + max(left, right)
        # 如果 > 0 返回上层继续计算 maxSum，如果<0 返回 0， 表示不记入开始节点
        if sumOfThisPath > 0:
            return sumOfThisPath
        else:
            return 0


# 2019-06-20 Redo


class Solution2(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.max_sum = -float('inf')
        
        self.search_maxPathSum(root)
        
        return self.max_sum
    
    def search_maxPathSum(self, node):
        
        if not node:
            return 0
        
        left = self.search_maxPathSum(node.left)
        right = self.search_maxPathSum(node.right)
        
        self.max_sum = max(left + right + node.val, self.max_sum)

        return max(left + node.val, right + node.val, node.val, 0)