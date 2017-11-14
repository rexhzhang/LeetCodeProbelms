"""Given a binary tree, find the largest subtree which is a Binary Search Tree (BST), where largest means subtree
with largest number of nodes in it.

Note:
A subtree must include all of its descendants.
Here's an example:
    10
    / \
   5  15
  / \   \
 1   8   7
The Largest BST Subtree in this case is the highlighted one.
The return value is the subtree's size, which is 3.
Follow up:
Can you figure out ways to solve it with O(n) time complexity?
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def largestBSTSubtree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.answer = 0
        if root is None:
            return 0

        def helper(node):
            if node.left is None and node.right is None:
                self.answer = max(self.answer, 1)
                return True, 1, node.val, node.val

            if node.left is None and node.right:
                statusR, numR, rightFloor, rightCeiling = helper(node.right)
                if statusR and node.val < rightFloor:
                    self.answer = max(self.answer, numR + 1)
                    return True, numR + 1, node.val, rightCeiling
                else:
                    return False, 1, node.val, rightCeiling

            elif node.right is None and node.left:
                statusL, numL, leftFloor, leftCeiling = helper(node.left)
                if statusL and node.val > leftCeiling:
                    self.answer = max(self.answer, numL + 1)
                    return True, numL + 1, leftFloor, node.val
                else:
                    return False, 1, leftFloor, node.val
            else:
                statusL, numL, leftFloor, leftCeiling = helper(node.left)
                statusR, numR, rightFloor, rightCeiling = helper(node.right)

                if statusL and statusR and leftCeiling < node.val < rightFloor:
                    self.answer = max(self.answer, numL + numR + 1)
                    return True, numL + numR + 1, leftCeiling, rightFloor
                else:
                    return False, numL + numR + 1, leftCeiling, rightFloor

        helper(root)

        return self.answer
