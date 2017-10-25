"""
Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

Note:
You may assume k is always valid, 1 ≤ k ≤ BST's total elements.

Follow up:
What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently? How would you optimize the kthSmallest routine?

Credits:
Special thanks to @ts for adding this problem and creating all test cases.

"""

"""
Perform an inorder traversal k times
Time: O(k)
SpaceL O(1)

"""
def kthSmallest(self, root, k):
    """
    :type root: TreeNode
    :type k: int
    :rtype: int
    """
    ans = None
    counter = k
    stack = []
    current = root
    while counter > 0:
        while current:
            stack.append(current)
            current = current.left

        current = stack.pop()
        ans = current.val
        current = current.right
        counter -= 1

    return ans