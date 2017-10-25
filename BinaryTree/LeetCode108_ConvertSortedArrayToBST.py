"""
Given an array where elements are sorted in ascending order, convert it to a height balanced BST.
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode

        1) Get the Middle of the array and make it root.
        2) Recursively do same for left half and right half.
          a) Get the middle of left half and make it left child of the root
              created in step 1.
          b) Get the middle of right half and make it right child of the
              root created in step 1.

        """
        # pass index is preferred
        start, end = 0, len(nums) - 1

        def helper(start, end):
            if start > end:
                return None

            mid = (start + end) / 2
            node = TreeNode(nums[mid])
            node.left = helper(start, mid - 1)
            node.right = helper(mid + 1, end)
            return node

        return helper(start, end)

        #         if not nums:
        #             return None

        #         mid = len(nums)//2
        #         root = TreeNode(nums[mid])
        #         root.left = self.sortedArrayToBST(nums[:mid])
        #         root.right = self.sortedArrayToBST(nums[mid+1:])

        #         return root