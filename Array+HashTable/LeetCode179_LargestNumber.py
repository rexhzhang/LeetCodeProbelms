"""
Given a list of non negative integers, arrange them such that they form the largest number.

For example, given [3, 30, 34, 5, 9], the largest formed number is 9534330.

Note: The result may be very large, so you need to return a string instead of an integer.
"""

from functools import cmp_to_key


class Solution:
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """

        def comp(x, y):
            # 返回负数表示小于，0表示等于，正数表示大于
            if x + y < y + x:
                return 1
            elif x + y > y + x:
                return -1
            else:
                return 0

        temp = [str(x) for x in nums]
        temp.sort(key=cmp_to_key(comp))
        return "".join(temp).lstrip("0") or "0"


obj = Solution()
answer = obj.largestNumber([3, 30, 34, 5, 9])
print(answer)
