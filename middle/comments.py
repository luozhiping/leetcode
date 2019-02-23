# 371. 两整数之和
# https://leetcode-cn.com/problems/comments/

class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        return a if b == 0 else self.getSum(a^b, (a&b)<<1)

s = Solution()
print(s.getSum(1, 20))