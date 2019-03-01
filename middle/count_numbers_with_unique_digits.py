# 357. 计算各个位数不同的数字个数
# https://leetcode-cn.com/problems/count-numbers-with-unique-digits/

class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 1

        res = 10
        t = 9
        for i in range(n):
            t *= (10 - i)
            res += t
        return res;

s = Solution()
print(s.countNumbersWithUniqueDigits(2))