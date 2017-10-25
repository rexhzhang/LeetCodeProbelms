class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """

        if s is None:
            return None

        ans = list(s)

        left, right = 0, len(ans) - 1
        dic = "aeiouAEIOU"
        while left < right:
            while left < right and (ans[left] not in dic):
                left += 1

            while left < right and (ans[right] not in dic):
                right -= 1

            temp = ans[left]
            ans[left] = ans[right]
            ans[right] = temp
            left += 1
            right -= 1
        result = "".join(ans)
        return result


test1 = Solution()

print(test1.reverseVowels("hello"))
