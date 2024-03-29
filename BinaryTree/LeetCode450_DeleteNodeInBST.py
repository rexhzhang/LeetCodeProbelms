"""
Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return the root node reference (possibly updated) of the BST.

Basically, the deletion can be divided into two stages:

Search for a node to remove.
If the node is found, delete the node.
Note: Time complexity should be O(height of tree).

Example:

root = [5,3,6,2,4,null,7]
key = 3

    5
   / \
  3   6
 / \   \
2   4   7

Given key to delete is 3. So we find the node with value 3 and delete it.

One valid answer is [5,4,6,2,null,null,7], shown in the following BST.

    5
   / \
  4   6
 /     \
2       7

Another valid answer is [5,2,6,null,4,null,7].

    5
   / \
  2   6
   \   \
    4   7

"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None



class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        if root is None:
            return None

        if root.val < key:
            root.right = self.deleteNode(root.right, key)


        elif root.val > key:
            root.left = self.deleteNode(root.left, key)

        else:  # root.val == key
            root = self.removeRoot(root, key)
        return root

    def removeRoot(self, root, key):

        pre = []

        def preorder(node):
            if node:
                pre.append(node.val)
                preorder(node.left)
                preorder(node.right)

        # pre.reverse()
        preorder(root)
        pre.remove(key)

        def constractBST(floor, ceiling):

            if pre and floor < pre[0] < ceiling:
                val = pre.pop(0)
                node = TreeNode(val)
                node.left = constractBST(floor, val)
                node.right = constractBST(val, ceiling)
                return node

        return constractBST(-float('inf'), float('inf'))
