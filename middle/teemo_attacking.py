# 495. 提莫攻击
# https://leetcode-cn.com/problems/teemo-attacking/

class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        if not timeSeries or duration == 0:
            return 0
        result = 0
        for i in range(1, len(timeSeries)):
            result += min(timeSeries[i] - timeSeries[i - 1], duration)
        result += duration
        return result

s = Solution()
print(s.findPoisonedDuration([1, 2], 2))