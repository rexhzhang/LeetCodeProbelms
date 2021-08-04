class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        '''
        len_a = len(a)
        len_b = len(b)

        if len_a < len_b:
            a = (len(b) - len(a))*'0' + a

        if len_a > len_b:
            b = (len_a - len_b)*'0' + b



        i = max(len_a, len_b)-1
        ans = ''
        carry = False
        while i >= 0 :

            if a[i] == '1' and b[i] == '1':
                c = '0' + c
                carry = True

        '''
        i = len(a) - 1
        j = len(b) - 1
        a_num = 0
        b_num = 0

        while i >= 0:
            if a[i] == '1':
                a_num += 1 * 2 ** (len(a) - 1 - i)
            elif a[i] == '0':
                a_num += 0 * 2 ** (len(a) - 1 - i)
            i -= 1

        while j >= 0:
            if b[j] == '1':
                b_num += 1 * 2 ** (len(b) - 1 - j)
            elif b[j] == '0':
                b_num += 0 * 2 ** (len(b) - 1 - j)
            j -= 1

        answer = a_num + b_num
        print(a_num)
        print(b_num)
        print(answer)

        returnValue = ''
        while answer > 2:
            reminder = answer % 2
            answer = answer / 2
            if reminder == 0:
                returnValue = '0' + returnValue
            if reminder == 1:
                returnValue = '1' + returnValue

        returnValue = str(answer % 2) + returnValue
        return returnValue

test = Solution()
test.addBinary('10','11')