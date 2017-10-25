"""
Given a set of candidate numbers (C) (without duplicates) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

The same repeated number may be chosen from C unlimited number of times.

Note:
All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
For example, given candidate set [2, 3, 6, 7] and target 7,
A solution set is:
[
  [7],
  [2, 2, 3]
]
"""

class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.answer = []
        candidates.sort()
        self.helper(target, 0, [], candidates)

        return self.answer

    def helper(self, target, start, valuelist, candidates):
        if target == 0:
            self.answer.append(valuelist)

        length = len(candidates)
        for i in range(start, length):
            if candidates[i] > target:
                return
            self.helper(target - candidates[i], i, valuelist + [candidates[i]], candidates)

test = Solution()
candidates = [2, 3, 6, 7]
target = 7
result = test.combinationSum(candidates, target)
print(result)