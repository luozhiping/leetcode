# 56. 合并区间
# https://leetcode-cn.com/problems/merge-intervals/

# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if not intervals:
            return []
        intervals.sort(key = lambda x:(x.start, x.end))
        inter = intervals[0]
        result = []
        for i in range(1, len(intervals)):
            interval = intervals[i]
            if inter.start == interval.start or inter.end >= interval.start:
                inter.end = max(interval.end, inter.end)
            elif inter.end < interval.start:
                result.append(inter)
                inter = interval
        result.append(inter)
        # for re in result:
        #     print(re.start, re.end)
        return result


s = Solution()
print(s.merge([Interval(1, 3) ,Interval(1, 5) ,Interval(2, 4) ,Interval(2, 6) ,Interval(8, 10) ,]))