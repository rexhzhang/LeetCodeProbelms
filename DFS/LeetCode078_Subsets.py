"""
Subset I
Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

For example,
If nums = [1,2,3], a solution is:

[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]

SubsetII
Given a list of numbers that may has duplicate numbers, return all possible subsets
Example
If S = [1,2,2], a solution is:

[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
"""


class Solution:
    def subsetsI(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if nums is None: return []
        elif len(nums) == 0: return [[]]

        result = []
        def helper(nums, index, resultList):
            result.append(resultList)
            for i in range(index, len(nums)):
                helper(nums, i+ 1, resultList + [nums[i]])
        helper(nums, 0, [])
        return result

    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if nums is None: return []
        elif len(nums) == 0: return [[]]

        result = []
        def helper(nums, index, subList):
            result.append(subList)
            for i in range(index, len(nums)):
                if i > index and nums[i-1] == nums[i]:
                    continue
                helper(nums, i+1, subList + [nums[i]])

        helper(nums, 0, [])
        return result

obj = Solution()
print(obj.subsets([1,2,3]))
