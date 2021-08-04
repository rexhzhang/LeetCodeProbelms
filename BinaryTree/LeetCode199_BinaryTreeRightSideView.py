"""Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see
ordered from top to bottom.

For example:
Given the following binary tree,
   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---
You should return [1, 3, 4].
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution:

    def rightSideView(self, root):
        # BFS Solution: using deque
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        q = deque([root])
        rightSideView = []
        while q:
            new_q = deque([])
            while q:
                if len(q) == 1:
                    rightSideView.append(q[0].val)
                node = q.popleft()
                if node.left: new_q.append(node.left)
                if node.right: new_q.append(node.right)

            q = new_q

        return rightSideView

    def rightSideView_DFS(self, root):
        # BFS Solution: using deque
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        