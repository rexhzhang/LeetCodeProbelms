"""
Remove the minimum number of invalid parentheses in order to make the input string valid. Return all possible results.

Note: The input string may contain letters other than the parentheses ( and ).

Example 1:

Input: "()())()"
Output: ["()()()", "(())()"]
Example 2:

Input: "(a)())()"
Output: ["(a)()()", "(a())()"]
Example 3:

Input: ")("
Output: [""]
"""

"""
Time Complexity:
On the first level, there's only one string which is the input string s, let's say the length of it is n, 
to check whether it's valid, we need O(n) time. On the second level, we remove one ( or ) from the first level, 
so there are C(n, n-1) new strings, each of them has n-1 characters, and for each string, 
we need to check whether it's valid or not, thus the total time complexity on this level is (n-1) x C(n, n-1). 
Come to the third level, total time complexity is (n-2) x C(n, n-2), so on and so forth...

Finally we have this formula:

T(n) = n x C(n, n) + (n-1) x C(n, n-1) + ... + 1 x C(n, 1) = n x 2^(n-1).
"""

from collections import deque

class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        q = deque([s])
        visited = set()
        result = []
        found = False
        while q:
            
            current = q.popleft()
            
            if self._is_valid(current):
                result.append(current)
                found = True
                
            if not found: # 每层移去一个括号
                for i in range(len(current)):
                    if current[i] == "(" or current[i] == ")":
                        t = current[:i] + current[i+1:]
                        if t not in visited:
                            visited.add(t)
                            q.append(t)
        
        return result
    
    def _is_valid(self, s):
        
        count = 0
        for c in s:
            if c == "(":
                count += 1
            
            elif c == ")":
                count -= 1
                if count < 0:
                    return False
        
        return count == 0