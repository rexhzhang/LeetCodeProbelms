"""
Write a function that takes a string as input and reverse only the vowels of a string.

Example 1:

Input: "hello"
Output: "holle"
Example 2:

Input: "leetcode"
Output: "leotcede"
Note:
The vowels does not include the letter "y".
"""

class Solution:
    def reverseVowels(self, s: str) -> str:
        # 相向双指针操作
        # Python知识点：1. 建立set
        #               2. 如何将String转成list of chars
        #                3. 如何将list of chars 转回string
        
        if not s:
            return s
        
        a = list(s)
        start, end = 0, len(a)-1
        vowels = set('AEIOUaeiou')
        
        while start < end:
            while start < end and a[start] not in vowels:
                start += 1
            while start < end and a[end] not in vowels:
                end -= 1
            
            a[start], a[end] = a[end], a[start]
            
            start += 1
            end -= 1
        
        return "".join(a)