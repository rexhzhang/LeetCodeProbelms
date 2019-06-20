"""
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Recursive Solution

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        def isValidBST(self, root):
            """
            :type root: TreeNode
            :rtype: bool
            """

            floor = -float('inf')
            ceiling = float('inf')

            def validateBST(node, floor, ceiling):
                if node is None:
                    return True

                left = validateBST(node.left, floor, node.val)
                right = validateBST(node.right, node.val, ceiling)

                return left and right and node.val > floor and node.val < ceiling

            return validateBST(root, floor, ceiling)



# Iterative Solution
class Solution2:
    def isValidBST(self, root: TreeNode) -> bool:
        
        if not root:
            return True
        
        stack = []
        
        node = root
        
        while node:
            stack.append(node)
            node = node.left
        
        last_node = stack[-1]
        while stack:
            node = stack.pop()
            
            if node.right:
                node = node.right
                while node:
                    stack.append(node)
                    node = node.left
            
            if stack:
                # 此处stack[-1]可能是last_node的右子节点，也可能是last_node的parent，都不应该比last_node小
                
                if stack[-1].val <= last_node.val:
                    return False
        
                last_node = stack[-1]
        
        return True