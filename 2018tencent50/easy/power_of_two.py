# 2的幂
# https://leetcode-cn.com/problems/power-of-two/


class Solution:
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 0:
            return False
        return n & n-1 == 0

s = Solution()
print(s.isPowerOfTwo(255))