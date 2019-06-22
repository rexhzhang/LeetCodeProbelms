"""
Given a binary tree, find the length of the longest consecutive sequence path.

The path refers to any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The longest consecutive path need to be from parent to child (cannot be the reverse).

Example 1:

Input:

   1
    \
     3
    / \
   2   4
        \
         5

Output: 3

Explanation: Longest consecutive sequence path is 3-4-5, so return 3.
Example 2:

Input:

   2
    \
     3
    / 
   2    
  / 
 1

Output: 2 

Explanation: Longest consecutive sequence path is 2-3, not 3-2-1, so return 2.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def longestConsecutive(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        self.longest = 1
        self.get_longest(root)
        return self.longest
    
    def get_longest(self, root):
        
        if not root:
            return 0, None
        
        if not root.left and not root.right:
            return 1, root.val
        
        left, l_v = self.get_longest(root.left)
        right, r_v = self.get_longest(root.right)
        
        if l_v == root.val + 1 and r_v == root.val + 1:
            self.longest = max(self.longest, left+1, right + 1)
            return max(left, right) +1, root.val
        
        if l_v == root.val + 1:
            self.longest = max(self.longest, left+1)
            return left + 1, root.val
        
        if r_v == root.val + 1:
            self.longest = max(self.longest, right + 1)
            return right + 1, root.val
        
        return 1, root.val
        