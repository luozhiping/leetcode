# 字符串转整数
# https://leetcode-cn.com/problems/string-to-integer-atoi/description/

class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        if str is None or len(str) == 0:
            return 0
        begin = False
        negative = False
        number = 0
        for c in str:
            if not begin:
                if c == ' ':
                    continue
                if c == "-":
                    negative = True
                    begin = True
                    continue
                if c == "+":
                    negative = False
                    begin = True
                    continue
                if c.isdigit():
                    number = number*10 + int(c)
                    begin = True
                    continue
                return 0
            else:
                if c.isdigit():
                    number = number * 10 + int(c)
                else:
                    break
        if negative:
            number = -number
        if number > 2**31 - 1:
            number = 2**31 - 1
        elif number < -2**31:
            number = -2**31
        return number

s = Solution()
print(s.myAtoi("+-2"))