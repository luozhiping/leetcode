# 253. 会议室 II
# https://leetcode-cn.com/problems/meeting-rooms-ii/

import heapq

class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        if not intervals:
            return 0
        intervals = sorted(intervals)
        rooms = []
        for interval in intervals:
            added = False
            for i, room in enumerate(rooms):
                if room <= interval[0]:
                    rooms.pop(i)
                    heapq.heappush(rooms, interval[1])
                    added = True
                    break
            if not added:
                heapq.heappush(rooms, interval[1])
        return len(rooms)


s = Solution()
print(s.minMeetingRooms([[0, 30],[5, 10],[15, 20]]))


import random
test = []
for i in range(random.randint(10, 100)):
    start = random.randint(1, 100)
    end = random.randint(start+1, start+1+50)
    test.append([start, end])
print(test)
# test = [[50, 92], [81, 110], [8, 56], [10, 45], [53, 60], [81, 132], [97, 121], [62, 82], [32, 42], [66, 72], [40, 81], [75, 102], [82, 109], [83, 121], [64, 66], [79, 87], [64, 89], [69, 106], [28, 42], [94, 111], [11, 22], [49, 79], [12, 30], [12, 16], [66, 113], [100, 104], [56, 85], [92, 135], [28, 29], [11, 15], [67, 94], [65, 68], [72, 106], [9, 58], [97, 100], [78, 92], [7, 15], [24, 57], [12, 57], [97, 115], [16, 35], [32, 36]]
print(s.minMeetingRooms(test))