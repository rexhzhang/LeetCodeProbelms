"""
Given a binary tree, return the postorder traversal of its nodes' values.

For example:
Given binary tree {1,#,2,3},
   1
    \
     2
    /
   3
return [3,2,1].

Note: Recursive solution is trivial, could you do it iteratively?


"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack, ans = [(root, False)], []

        while stack:

            node, flag = stack.pop()

            if node:

                if flag is True:
                    ans.append(node.val)

                else:
                    stack.append((node, True))
                    stack.append((node.right, False))
                    stack.append((node.left, False))

        return ans

    def postorderTraversal2(self, root):
        postorder = deque([])
        stack = [root]
        if root is None:
            return []

        while stack:
            node = stack.pop()
            postorder.appendleft(node.val)

            if node.left:
                stack.append(node.left)

            if node.right:
                stack.append(node.right)

        return list(postorder)
