# 704. 二分查找
# https://leetcode-cn.com/problems/binary-search/

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        start = 0
        end = len(nums) - 1
        while start <= end:
            middle = (start + end) >> 1
            if nums[middle] == target:
                return middle
            if nums[middle] < target:
                start += 1
            else:
                end -= 1
        return -1


s = Solution()
print(s.search([-1,0,3,5,9,12], 2))

import random

test = set()
for i in range(random.randint(1, 10000)):
    test.add(random.randint(-9999, 9999))
test = sorted(list(test))
target = test[random.randint(0, len(test)-1)]
print(test, target)
print(s.search(test, target))