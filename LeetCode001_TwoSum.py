"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

"""


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        if len(nums) <= 1:
            return False

        map = {}
        for i in range(len(nums)):
            if nums[i] in map:
                return [map[nums[i]], i]
            else:
                map[target - nums[i]] = i
                # [2,7,11,15]
                # 1st iteration: buff_dict = {7:0}
                # 2nd iteration: since 7 is already in the dictionary, return the key of 7 (which is the index of first number)
                # and return the current index


test = Solution()
result = test.twoSum([2, 11, 15, 7], 9)
print(result)