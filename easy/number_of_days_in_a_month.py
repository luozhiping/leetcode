# 1118. 一月有多少天
# https://leetcode-cn.com/problems/number-of-days-in-a-month/

class Solution(object):
    def numberOfDays(self, Y, M):
        """
        :type Y: int
        :type M: int
        :rtype: int
        """
        days = [0,
                31, 30, 31, 30,
                31, 30, 31, 31,
                30, 31, 30, 31]
        if M != 2:
            return days[M]
        if Y % 400 == 0 or (Y % 4 == 0 and Y % 100 != 0):
            return 29
        else:
            return 28