# 703. 数据流中的第K大元素
# https://leetcode-cn.com/problems/kth-largest-element-in-a-stream/

import heapq


class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """

        self.pool = heapq.nlargest(k, nums)
        heapq.heapify(self.pool)
        self.k = k
    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        if len(self.pool) < self.k:
            heapq.heappush(self.pool, val)
        else:
            heapq.heappushpop(self.pool, val)
        return self.pool[0]
# Your KthLargest object will be instantiated and called as such:
obj = KthLargest(3, [4,5,8,2])
assert obj.add(3) == 4
assert obj.add(5) == 5
assert obj.add(10) == 5
assert obj.add(9) == 8
assert obj.add(4) == 8