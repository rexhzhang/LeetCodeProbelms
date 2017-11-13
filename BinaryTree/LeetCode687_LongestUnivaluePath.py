"""

Given a binary tree, find the length of the longest path where each node in the path has the same value. This path
may or may not pass through the root.

Note: The length of path between two nodes is represented by the number of edges between them.

Example 1:

Input:

              5
             / \
            4   5
           / \   \
          1   1   5
Output:

2
Example 2:

Input:

              1
             / \
            4   5
           / \   \
          4   4   5
Output:

2
Note: The given binary tree has not more than 10000 nodes. The height of the tree is not more than 1000.


"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.result = 0

        def helper(node):
            if node is None:
                return None, 0
            left, nodesL = helper(node.left)
            right, nodesR = helper(node.right)
            if left == node.val and right == node.val:
                self.result = max(self.result, nodesL + nodesR + 1 - 1)
                if nodesL >= nodesR:
                    return node.val, nodesL + 1
                else:
                    return node.val, nodesR + 1

            if left == node.val:
                self.result = max(self.result, nodesL + 1 - 1)
                return node.val, nodesL + 1

            if right == node.val:
                self.result = max(self.result, nodesR + 1 - 1)
                return node.val, nodesR + 1

            return node.val, 1

        helper(root)

        return self.result