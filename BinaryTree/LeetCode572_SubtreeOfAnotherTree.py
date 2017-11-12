"""Given two non-empty binary trees s and t, check whether tree t has exactly the same structure and node values with
a subtree of s. A subtree of s is a tree consists of a node in s and all of this node's descendants. The tree s could
also be considered as a subtree of itself.

Example 1:
Given tree s:

     3
    / \
   4   5
  / \
 1   2
Given tree t:
   4
  / \
 1   2
Return true, because t has the same structure and node values with a subtree of s.
Example 2:
Given tree s:

     3
    / \
   4   5
  / \
 1   2
    /
   0
Given tree t:
   4
  / \
 1   2
Return false.
"""


class Solution:
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        def sameTree(p, q):
            if p is None and q is None: return True
            if p is None: return False
            if q is None: return False

            return p.val == q.val and sameTree(p.left, q.left) and sameTree(p.right, q.right)

        self.answer = False

        def helper(s, t):
            if s is None or t is None: return
            if self.answer: return
            if s.val == t.val:
                if sameTree(s, t): self.answer = True

            helper(s.left, t)
            helper(s.right, t)

        helper(s, t)
        return self.answer