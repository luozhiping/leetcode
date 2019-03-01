# 365. 水壶问题
# https://leetcode-cn.com/problems/water-and-jug-problem/

class Solution(object):
    def canMeasureWater(self, x, y, z):
        """
        :type x: int
        :type y: int
        :type z: int
        :rtype: bool
        """
        if z == 0:
            return True
        if x == 0:
            return y == z
        if y == 0:
            return x == z
        if z > x + y:
            return False
        while x % y != 0:
            x, y = y, (x % y)

        if z % y == 0:
            return True
        return False
s = Solution()
print(s.canMeasureWater(2, 6, 10))