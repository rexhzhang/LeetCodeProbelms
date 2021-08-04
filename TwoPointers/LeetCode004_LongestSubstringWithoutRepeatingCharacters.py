"""
Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s: return 0
        
        longest, j = 0, 0
        bag = set()
        for i in range(len(s)):

            while j < len(s) and s[j] not in bag:
                bag.add(s[j])
                j += 1
            
            longest = max(longest, len(bag))
            bag.remove(s[i])
        
        return longest
