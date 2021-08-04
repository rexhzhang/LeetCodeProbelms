"""
Given a collection of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

Each number in C may only be used once in the combination.

Note:
All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
For example, given candidate set [10, 1, 2, 7, 6, 1, 5] and target 8,
A solution set is:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
"""


class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.answer = []
        candidates.sort()
        print(candidates)
        self.helper(candidates, 0, [], target)
        return self.answer

    def helper(self, candidates, start, valuelist, target):
        if target == 0:
            self.answer.append(valuelist)
            return

        length = len(candidates)
        for i in range(start, length):

            if candidates[i] > target:
                return
            if i > start and candidates[i] == candidates[i-1]:
                continue
            self.helper(candidates, i + 1, valuelist + [candidates[i]], target - candidates[i])



test = Solution()
candidates = [10, 1, 2, 7, 6, 1, 5]
target = 8
result = test.combinationSum2(candidates, target)
print(result)