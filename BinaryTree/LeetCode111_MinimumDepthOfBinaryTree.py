"""
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.


"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    # DFS
    # DFS traverses all the nodes even for a highly unbalanced tree
    def minDepthDFS(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        if not root.left: return self.minDepth(root.right) + 1
        if not root.right: return self.minDepth(root.left) + 1
        return min(self.minDepth(root.right),self.minDepth(root.left)) + 1

    # for a highly unbalanced tree, we can perform BFS, when we find a leaf node, we immediately stop BFS
    # BFS
    def minDepthBFS(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        queue = [root]
        depth = 1
        while queue:
            new_q = []
            for node in queue:
                if node.left is None and node.right is None:
                    return depth
                if node.left:
                    new_q.append(node.left)
                if node.right:
                    new_q.append(node.right)
            queue = new_q
            depth += 1
