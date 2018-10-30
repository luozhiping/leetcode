# 爬楼梯
# https://leetcode-cn.com/problems/climbing-stairs/


class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = []
        result.append(1)
        result.append(2)
        for i in range(2, n):
            result.append(result[i - 1] + result[i - 2])
        return result[n - 1]


s = Solution()
print(s.climbStairs(35))