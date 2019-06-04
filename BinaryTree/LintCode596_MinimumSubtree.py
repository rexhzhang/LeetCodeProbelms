"""
Description
Given a binary tree, find the subtree with minimum sum. Return the root of the subtree.

Example
Example 1:

Input:
{1,-5,2,1,2,-4,-5}
Output:1
Explanation:
The tree is look like this:
     1
   /   \
 -5     2
 / \   /  \
0   2 -4  -5 
The sum of whole tree is minimum, so return the root.
Example 2:

Input:
{1}
Output:1
Explanation:
The tree is look like this:
   1
There is one and only one subtree in the tree. So we return 1.
"""

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the root of binary tree
    @return: the root of the minimum subtree
    """
    def findSubtree(self, root):
        # write your code here
        self.subtree = None
        self.minSum = float('inf')
        self.findSubtreeSum(root)
        
        return self.subtree
        
    
    def findSubtreeSum(self, node):
        
        if node is None:
            return 0
        
        left = self.findSubtreeSum(node.left)
        right = self.findSubtreeSum(node.right)
        curSum = node.val + left + right
        
        if curSum < self.minSum:
            self.subtree = node
            self.minSum = curSum
        
        return curSum