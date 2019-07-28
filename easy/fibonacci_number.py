# 509. 斐波那契数
# https://leetcode-cn.com/problems/fibonacci-number/

class Solution(object):
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N == 0:
            return 0
        if N == 1:
            return 1

        last2 = 0
        last1 = 1

        for _ in range(2, N+1):
            # current = last1 + last2
            last2,last1 = last1,last1 + last2
        return last1

s = Solution()
print(s.fib(30))