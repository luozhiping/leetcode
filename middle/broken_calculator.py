# 991. 坏了的计算器
# https://leetcode-cn.com/problems/broken-calculator/

class Solution(object):
    def brokenCalc(self, X, Y):
        """
        :type X: int
        :type Y: int
        :rtype: int
        """
        if X >= Y:
            return X - Y
        count = 0
        while X < Y:
            if Y % 2 == 0:
                Y = Y / 2
            else:
                Y = Y + 1
            count += 1
        return int(count + X - Y)

s = Solution()
print(s.brokenCalc(5, 8))