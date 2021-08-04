"""
In a binary tree, the root node is at depth 0, and children of each depth k node are at depth k+1.

Two nodes of a binary tree are cousins if they have the same depth, but have different parents.

We are given the root of a binary tree with unique values, and the values x and y of two different nodes in the tree.

Return true if and only if the nodes corresponding to the values x and y are cousins.

 

Example 1:


Input: root = [1,2,3,4], x = 4, y = 3
Output: false
Example 2:


Input: root = [1,2,3,null,4,null,5], x = 5, y = 4
Output: true
Example 3:



Input: root = [1,2,3,null,4], x = 2, y = 3
Output: false
 

Note:

The number of nodes in the tree will be between 2 and 100.
Each node has a unique integer value from 1 to 100.
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from queue import Queue

class Solution(object):

    # BFS
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        """
        :type root: TreeNode
        :type x: int
        :type y: int
        :rtype: bool
        """
        
        q=Queue()
        q.put(root)

        while not q.empty():
            
            x_exist = False
            y_exist = False
            new_q = Queue()

            while not q.empty():
                node = q.get()
                if node.left and node.right:
                    if node.left.val == x and node.right.val == y:
                        return False
                    elif node.left.val == y and node.right.val == x:
                        return False
                
                if node.val == x:
                    x_exist = True
                
                if node.val == y:
                    y_exist = True
                
                if node.left:
                    new_q.put(node.left)
                if node.right:
                    new_q.put(node.right)
            
            if x_exist and y_exist:
                return True
            
            q = new_q
        
        return False


    def _isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        """
        DFS Solution
        :type root: TreeNode
        :type x: int
        :type y: int
        :rtype: bool
        """

        return True if self.findDepth(root, x, 1) == self.findDepth(root, y, 1) and not self.checkParent(root, x, y) else False
    
    def checkParent(self, root: TreeNode, x: int, y: int) -> bool:
        # return True if common parent, else False
        if not root:
            return False
        
        if root.left and root.right:
            if root.left.val == x and root.right.val == y:
                return True
            if root.left.val == y and root.right.val == x:
                return True
        
        left = self.checkParent(root.left, x, y)
        right = self.checkParent(root.right, x, y)

        return left or right

    def findDepth(self, root: TreeNode, target: int, level: int) -> bool:
        if root is None:
            return None
        
        if root.val == target:
            return level

        left = self.findDepth(root.left, target,  level + 1)
        right = self.findDepth(root.right, target, level + 1)

        if left:
            return left
        elif right:
            return right
        else:
            return None
        
import BuildATree

testCase1 = BuildATree.BuildTree([1,2,None,None,3,None,4,5])
root = testCase1.build()
testCase1.printTree(root)

test = Solution()
print(test.isCousins(root, 3, 4))