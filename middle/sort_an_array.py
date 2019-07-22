# 912. 排序数组
# https://leetcode-cn.com/problems/sort-an-array/

class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        def partition(start, end):
            if start >= len(nums) or end <= 0 or start >= end:
                return

            oriStart = int(start)
            oriEnd = int(end)
            cur = nums[start]
            downEnd = True
            while start < end:
                if downEnd:
                    if nums[end] >= cur:
                        end -= 1
                    else:
                        nums[start] = nums[end]
                        nums[end] = cur
                        downEnd = not downEnd
                else:
                    if nums[start] <= cur:
                        start += 1
                    else:
                        nums[end] = nums[start]
                        nums[start] = cur
                        downEnd = not downEnd
            # print(nums, start)
            partition(oriStart, start-1)
            partition(start+1, oriEnd)


        partition(0, len(nums) - 1)
        return nums


s = Solution()
print(s.sortArray([5,1,1,2,0,0]))

import random
test = []

for i in range(random.randint(1000, 10000)):
    test.append(random.randint(-50000,50000))
print(test)
test = []
assert s.sortArray(test) == sorted(test)