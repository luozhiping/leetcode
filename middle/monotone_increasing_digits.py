# 738. 单调递增的数字
# https://leetcode-cn.com/problems/monotone-increasing-digits/

class Solution(object):
    def monotoneIncreasingDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        last = 10
        result = []
        while N:
            cur = N % 10
            if cur > last:
                result = [9] * len(result)
                last = cur - 1
                result.insert(0, cur - 1)
            else:
                result.insert(0, cur)
                last = cur
            N = N // 10
        # print(result)
        r = 0
        for i in range(len(result)):
            r = r * 10 + result[i]
        return r

s = Solution()
print(s.monotoneIncreasingDigits(332))

import random
test = random.randint(100, 10**9)
print(test)
print(s.monotoneIncreasingDigits(test))