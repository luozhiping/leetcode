# 371. 两整数之和
# https://leetcode-cn.com/problems/comments/

class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """

        while b != 0:
            carry = a & b
            a = (a ^ b) % 0x100000000
            b = (carry << 1) % 0x100000000
        return a if a <= 0x7FFFFFFF else a | (~0x100000000 + 1)

s = Solution()
print(s.getSum(-1, 1))