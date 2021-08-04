"""
Rotate an array of n elements to the right by k steps.

For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4].

Note:
Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.

[show hint]

Hint:
Could you do it in-place with O(1) extra space?
Related problem: Reverse Words in a String II
"""


class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n <= 1: return
        k = k % n

        nums = reversed(nums)
        nums[:k] = reversed(nums[:k])
        nums[k:] = reversed(nums[k:])

"""
Explaination:
1. "I love Seattle"
2. 'elttaeS evol I'
3. " ".join(list(map(lambda x: x[::-1],'elttaeS evol I'.split())))
"""


"""
******************************* Recover Roated Sorted Array ******************************************8
Given a rotated sorted array, recover it to sorted array in-place.

Have you met this question in a real interview? Yes
Clarification
What is rotated array?

For example, the orginal array is [1,2,3,4], The rotated array of it can be [1,2,3,4], [2,3,4,1], [3,4,1,2], [4,1,2,3]
Example
[4, 5, 1, 2, 3] -> [1, 2, 3, 4, 5]

Challenge 
In-place, O(1) extra space and O(n) time.

"""


class Solution2:
    """
    @param nums: The rotated sorted array
    @return: nothing
    """

    def recoverRotatedSortedArray(self, nums):
        # write your code here
        k = 0
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                k = i
                break

        # print(k)
        nums[:k+1] = reversed(nums[:k+1])
        nums[k+1:] = reversed(nums[k+1:])
        nums.reverse()
        # print(nums)

obj = Solution2()
obj.recoverRotatedSortedArray([4, 5, 1, 2, 3])