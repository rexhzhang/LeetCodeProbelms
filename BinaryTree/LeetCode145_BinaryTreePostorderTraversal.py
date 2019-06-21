"""
Given a binary tree, return the postorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [3,2,1]
Follow up: Recursive solution is trivial, could you do it iteratively?
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        """
        后续遍历是先左子树，再右子树再到父结点，倒过来看就是先父结点，再右子树再左子树。
        是前序遍历改变左右子树访问顺序。 再将输出的结果倒序输出一遍就是后序遍历
        """
        if not root:
            return []
        
        stack = [root]
        post_order = []
        
        while stack:
            node = stack.pop()
            post_order.append(node.val)
            if node.left:
                stack.append(node.left)
            
            if node.right:
                stack.append(node.right)
            
        return post_order[::-1]
                