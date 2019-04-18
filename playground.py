# s = "Bob hit a ball, the hit BALL flew far after it was hit."
# banned_set = set(["hit"])
# d = {}
# for item in [item.lower().strip("!?',;.") for item in s.split()]:
#         if item not in banned_set:
#                 if item not in d:
#                         d[item] = 1
#                 else:
#                         d[item] += 1

# print(d)

# v = 1
# ans = None
# for k in d:
#         if d[k] > v:
#                 ans = k

# print(ans)

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
a.right = b
b.left = c

class Solution(object):
    res = []
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.helper(root)
        return self.res
        
    
    def helper(self, root):
        if root is not None:
            self.helper(root.left)
            self.res.append(root.val)
            print(self.res)
            self.helper(root.right)
        
    
o = Solution()
o.inorderTraversal(a)
print(o.res)