"""
The set [1,2,3,...,n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order, we get the following sequence for n = 3:

"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence.

Note:

Given n will be between 1 and 9 inclusive.
Given k will be between 1 and n! inclusive.
Example 1:

Input: n = 3, k = 3
Output: "213"
Example 2:

Input: n = 4, k = 9
Output: "2314"
"""

class Solution(object):
    
    def getPermutation(self, n: int, k: int) -> str:
        
        if n < 1 or n > 9: return
        
        numbers = [i for i in range(1,n+1)]
        
        permutations = self.permutation(numbers)
        
        return permutations[k-1]
    
    def permutation(self, l: list) -> list:
        
        if len(l) == 0:
            return []
        
        elif len(l) == 1:
            return [str(l[0])]

        else:
            numbers = []
            
            for i in range(len(l)):
                remaining = self.permutation(l[:i]+l[i+1:])
                for items in remaining:
                    numbers.append(str(l[i])+items)
            
            
            return numbers


a = Solution()
print(a.getPermutation(3,3))