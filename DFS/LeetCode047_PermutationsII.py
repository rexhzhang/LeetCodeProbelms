"""
Given a collection of numbers that might contain duplicates, return all possible unique permutations.

For example,
[1,1,2] have the following unique permutations:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]

"""


class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if nums is None:
            return []
        if len(nums) == 0:
            return [[]]
        if len(nums) == 1:
            return [nums]
        Solution.result = []
        self.DFS(sorted(nums), [])
        return Solution.result

    def DFS(self, RemainingNums, valuelist):
        if len(RemainingNums) == 0:
            Solution.result.append(valuelist)

        for i in range(len(RemainingNums)):
            if i >= 1 and RemainingNums[i] == RemainingNums[i-1]:
                continue
            self.DFS(RemainingNums[:i] + RemainingNums[i+1:], valuelist+[RemainingNums[i]])

test = Solution()
result = test.permuteUnique([1,1,2])
print(result)