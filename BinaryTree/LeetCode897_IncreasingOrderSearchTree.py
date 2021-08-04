"""
Given a tree, rearrange the tree in in-order so that the leftmost node in the tree is now the root of the tree, and every node has no left child and only 1 right child.

Example 1:
Input: [5,3,6,2,4,null,8,1,null,null,null,7,9]

       5
      / \
    3    6
   / \    \
  2   4    8
 /        / \
1        7   9

Output: [1,null,2,null,3,null,4,null,5,null,6,null,7,null,8,null,9]

 1
  \
   2
    \
     3
      \
       4
        \
         5
          \
           6
            \
             7
              \
               8
                \
                 9
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:

        # 考点：中序遍历 + Dummy Node

        d = TreeNode(0)
        cur = d

        if not root:
            return None
        
        stack = []
        node = root
        while node:
            stack.append(node)
            node = node.left
        
        while stack:
            node = stack.pop()
            cur.right = node
            cur = cur.right
            node.left = None

            if node.right:
                node = node.right
                while node:
                    stack.append(node)
                    node = node.left
            
        return d.right




