"""

Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]

"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        self.results = []

        if not root:
            return self.results

        # put root on to the queue
        que = [root]

        while que:
            # 两个Queue 互相倒
            next_level_que = []
            self.results.append([node.val for node in que])

            for node in que:
                if node.left:
                    next_level_que.append(node.left)
                if node.right:
                    next_level_que.append(node.right)
            que = next_level_que

        return self.results



