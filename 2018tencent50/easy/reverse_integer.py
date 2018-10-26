# 反转整数
# https://leetcode-cn.com/problems/reverse-integer/

class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        result = 0
        negative = x < 0
        if negative:
            x = -x
        while x > 0:
            result = result * 10 + x % 10
            x = x // 10
        if negative:
            result = -result
            if result < -2 ** 31:
                result = 0
        else:
            if result > 2 ** 31 - 1:
                result = 0
        return result


s = Solution()
print(s.reverse(-123))
