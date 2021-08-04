"""
Given a string which contains only lowercase letters, remove duplicate letters so that every letter appear once and only once. You must make sure your result is the smallest in lexicographical order among all possible results.

Example:
Given "bcabc"
Return "abc"

Given "cbacdcbc"
Return "acdb"

Given "bbcaac"
Return "bac"

Given "ccacbaba"
Return "acb"

"""

import collections


class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str

        :rtype: str
        """
        hashMap = collections.defaultdict(int)
        for char in s:
            hashMap[char] += 1

        stack = collections.deque([])

        for char in s:
            if len(stack) == 0:
                stack.append(char)

            elif ord(char) < ord(stack[-1]) and hashMap[stack[-1]] > 1 and char not in stack: # cb 并后面还有c
                while len(stack) > 0 and ord(char) < ord(stack[-1]) and hashMap[stack[-1]] > 1:
                    hashMap[stack[-1]] -= 1
                    stack.pop()
                stack.append(char)


            elif char in stack and hashMap[char] > 1:
                hashMap[char] -= 1 #非常重要
                continue
            else:
                stack.append(char)

            # print(stack) # for debug
        return "".join(stack)

test = Solution()
print(test.removeDuplicateLetters("ccacbaba"))
