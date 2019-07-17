# 50. Pow(x, n)
# https://leetcode-cn.com/problems/powx-n/

class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        return pow(x, n)

s = Solution()
print(s.myPow(2, 10))