"""
Given a binary tree, count the number of uni-value subtrees.

A Uni-value subtree means all nodes of the subtree have the same value.

For example:
Given binary tree,
              5
             / \
            1   5
           / \   \
          5   5   5
return 4.

"""


# Definition for a binary tree node.
# class TreeNode(object):

#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def countUnivalSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        # class TreeNode(object):
        #     def __init__(self, x):
        #         self.val = x
        #         self.left = None
        #         self.right = None

        class Solution(object):
            def countUnivalSubtrees(self, root):
                """
                :type root: TreeNode
                :rtype: int
                """
                self.answer = 0

                def helper(node):
                    if node is None: return None, True
                    leftReturn, statusL = helper(node.left)
                    rightReturn, statusR = helper(node.right)

                    if (leftReturn == node.val or leftReturn == None) and (
                            rightReturn == node.val or rightReturn == None) and statusL and statusR:
                        self.answer += 1
                        return node.val, True

                    return node.val, False

                helper(root)

                return self.answer

"""
[5,1,5,5,5,null,5]
return 4
"""