"""Serialization is the process of converting a data structure or object into a sequence of bits so that it can be
stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the
same or another computer environment.

Design an algorithm to serialize and deserialize a binary search tree. There is no restriction on how your
serialization/deserialization algorithm should work. You just need to ensure that a binary search tree can be
serialized to a string and this string can be deserialized to the original tree structure.

The encoded string should be as compact as possible.

"""
"""
If the given Binary Tree is Binary Search Tree, we can store it by either storing preorder or postorder traversal.
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
import collections


class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        preorder = []

        def preOrder(node):
            if node:
                preorder.append(node.val)
                preOrder(node.left)
                preOrder(node.right)

        preOrder(root)
        return " ".join(map(str, preorder))

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        deque = collections.deque(int(val) for val in data.split())

        def build(floor, ceiling):
            if deque and floor < deque[0] < ceiling:
                val = deque.popleft()
                node = TreeNode(val)
                node.left = build(floor, val)
                node.right = build(val, ceiling)
                return node

        return build(-float('inf'), float('inf'))