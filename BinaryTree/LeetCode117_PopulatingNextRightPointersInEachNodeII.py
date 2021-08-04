"""

Follow up for problem "Populating Next Right Pointers in Each Node".

What if the given tree could be any binary tree? Would your previous solution still work?

Note:

You may only use constant extra space.
For example,
Given the following binary tree,
         1
       /  \
      2    3
     / \    \
    4   5    7
After calling your function, the tree should look like:
         1 -> NULL
       /  \
      2 -> 3 -> NULL
     / \    \
    4-> 5 -> 7 -> NULL

"""


# Definition for binary tree with next pointer.
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        pNode = nxtLevelNode = TreeLinkNode(0)

        while root:
            if root.left:
                pNode.next = root.left
                pNode = pNode.next

            if root.right:
                pNode.next = root.right
                pNode = pNode.next

            root = root.next

            if root is None:
                pNode = nxtLevelNode
                root = nxtLevelNode.next
                nxtLevelNode.next = None



# 2019-06-20 Redo

class Solution2:
    def connect(self, root: 'Node') -> 'Node':
        # Time: O(n)
        # Space: O(1)
        
        left = root
        
        while left:
            
            cur = left
            
            d = Node(0, None, None, None)
            p = d
            
            while cur:
                
                if cur.left:
                    p.next = cur.left
                    p = cur.left
                
                if cur.right:
                    p.next = cur.right
                    p = cur.right
                
                cur = cur.next
            
            left = d.next # 因为d.next 保存的是下level的第一个点
        
        return root