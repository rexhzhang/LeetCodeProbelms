"""
Given a collection of distinct numbers, return all possible permutations.

For example,
[1,2,3] have the following permutations:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
"""
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if nums is None:
            return []
        if len(nums) == 0:
            return []
        if len(nums) == 1:
            return [nums]
        Solution.result = []
        self.DFS(nums, [])
        return Solution.result

    def DFS(self, RemainingNums, valuelist):
        if len(RemainingNums) == 0:
            Solution.result.append(valuelist)
            return

        for i in range(len(RemainingNums)):
            self.DFS(RemainingNums[:i] + RemainingNums[i+1:], valuelist + [RemainingNums[i]])

test = Solution()
result = test.permute([1,2,3])
print(result)


# 2019-06-23 Redo

class Solution2:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        self.DFS(nums, [], result)
        return result
    
    def DFS(self, remaining_elements, permutation, result):
        
        if not remaining_elements:
            return result.append(list(permutation))
        
        for i in range(len(remaining_elements)):
            permutation.append(remaining_elements[i])
            self.DFS(remaining_elements[:i]+remaining_elements[i+1:], permutation, result)
            permutation.pop()
        
        