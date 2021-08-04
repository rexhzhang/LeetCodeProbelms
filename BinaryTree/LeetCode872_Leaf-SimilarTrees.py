"""
Consider all the leaves of a binary tree.  From left to right order, the values of those leaves form a leaf value sequence.



For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).

Two binary trees are considered leaf-similar if their leaf value sequence is the same.

Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.

"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution2:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        s1 = []
        s2 = []
        self._find_leaf_sequence(root1, s1)
        self._find_leaf_sequence(root2, s2)
        
        return s1 == s2
    
        
    def _find_leaf_sequence(self, node, res):
        
        if node:
            
            self._find_leaf_sequence(node.left, res)
            
            
            if not node.left and not node.right:
                res.append(node.val)
            
            self._find_leaf_sequence(node.right, res)