from collections import deque


class Solution:
    def printTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[str]]
        """
        if root is None:
            return []

        result = []
        q = deque()
        q.append(root)

        while len(q) > 0:
            node = q.popleft()
