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


# 2019-06-23 Redo
class Solution2:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        需要去重，因为题目要unique combinations
        需要提前排序，因为需要依靠排序来做判断提前终止
        每个数字可以重复利用，所以startIndex传入下一层不+1
        """
        result = []
        candidates = sorted(list(set(candidates))) # 去重+排序
        self.DFS(candidates, target, 0, [], result)
        return result
    

    def DFS(self, candidates, target, start, combination, result):
        if target == 0:
            result.append(list(combination)) # deepcopy
            return
        
        for i in range(start, len(candidates)):
            if candidates[i] > target:
                return
            
            combination.append(candidates[i])
            self.DFS(candidates, target - candidates[i], i, combination, result)
            combination.pop() # backtracking
