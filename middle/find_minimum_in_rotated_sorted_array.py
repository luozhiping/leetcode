# 153. 寻找旋转排序数组中的最小值
# https://leetcode-cn.com/problems/find-minimum-in-rotated-sorted-array/
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start = 0
        end = len(nums) - 1
        while start < end:
            mid = (end + start) // 2
            if nums[mid] > nums[end]:
                start = mid+1
            elif nums[mid] < nums[end]:
                end = mid
            # print(start, end, mid)


        return nums[start]

s = Solution()
print(s.findMin([4,5,6,7,0,1,2]))

import random
test = [i for i in range(random.randint(1, 1000))]
cut = random.randint(1, len(test))
test = test[-cut:] + test[:cut]
print(test)
print(s.findMin(test))