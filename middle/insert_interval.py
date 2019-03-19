# 57. 插入区间
# https://leetcode-cn.com/problems/insert-interval/
# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    def insert(self, intervals, newInterval) :
        intervals.append(newInterval)
        if len(intervals) == 0:
            return []
        intervals = sorted(intervals,key = lambda x:x.start)
        res = []
        start  = intervals[0].start
        end = intervals[0].end
        for i in range(1,len(intervals)):
            if intervals[i].start>end:  # 不重叠
                res.append([start,end])
                start = intervals[i].start
                end = intervals[i].end
            else:                       #有重叠
                end = max(intervals[i].end,end)
        res.append([start,end])         #最后一个也要加进去
        return res

s = Solution()
test = [Interval(1,2), Interval(3, 5), Interval(6, 7), Interval(8, 10), Interval(12, 16)]
print(s.insert(test, Interval(4, 8)))