from collections import deque


class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        """
        解题思路：用stack保存从左开始的每一位
        遇到当前位比stack最上层的小时，pop stack并压入当前数, 直到pop k 次
        如果num一直递增，则干掉stack最后的k位
        """
        if k == 0:
            return num

        stack = deque([])
        for char in num:
            # if k == 0:
            #   return ''.join(str(num) for num in stack)

            if len(stack) == 0:
                stack.append(int(char))

            elif int(char) >= stack[-1]:
                stack.append(int(char))

            elif int(char) < stack[-1]:
                while k > 0 and len(stack) > 0 and int(char) < stack[-1]:
                    stack.pop()
                    k -= 1

                stack.append(int(char))

        while k > 0:
            stack.pop()
            k -= 1

        if len(stack) != 0 and stack[0] != 0:
            return ''.join(str(num) for num in stack)
        else:
            while len(stack) > 1 and stack[0] == 0:
                stack.popleft()
            return "0" if len(stack) == 0 else ''.join(str(num) for num in stack)
