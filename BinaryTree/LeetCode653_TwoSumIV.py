"""
Given a Binary Search Tree and a target number, return true if there exist two elements in the BST such that their sum is equal to the given target.

Example 1:

Input: 
    5
   / \
  3   6
 / \   \
2   4   7

Target = 9

Output: True
 

Example 2:

Input: 
    5
   / \
  3   6
 / \   \
2   4   7

Target = 28

Output: False
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        # 使用Inorder Traverse Time: O(n), Space O(n)
        
        if not root:
            return False
        
        stack = [root]
        
        values = set()
        
        while stack:
            node = stack.pop()
            
            if k - node.val in values:
                return True
            
            values.add(node.val)
            
            if node.right:
                stack.append(node.right)
            
            if node.left:
                stack.append(node.left)
        
        return False
    
    # 方法二：O(nh) Time Complexity, O(h) Space complexity, h is the height of the BST
    # 用inorder遍历。
    # 遍历过程中根据BST的性质用类似二分的方法查找。
