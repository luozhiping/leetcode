# 650. 只有两个键的键盘
# https://leetcode-cn.com/problems/2-keys-keyboard/

class Solution(object):
    def minSteps(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = 0
        minResult = {}
        while n > 1:
            for i in range(2, n+1):
                if n % i == 0:
                    result += i
                    n //= i
                    break
                if i == n:
                    return n
        return result
s = Solution()
assert s.minSteps(18) == 8