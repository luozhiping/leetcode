# 34. 在排序数组中查找元素的第一个和最后一个位置
# https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array/

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return [-1, -1]
        start = 0
        end = len(nums) - 1
        index = -1
        while start <= end:
            mid = (end + start) // 2
            if nums[mid] > target:
                end = mid - 1
            elif nums[mid] < target:
                start = mid + 1
            else:
                index = mid
                break
        if index == -1:
            return [-1, -1]
        start = index
        end = index
        for i in range(index - 1, -1, -1):
            if nums[i] == target:
                start = i
            else:
                break
        for i in range(index + 1, len(nums)):
            if nums[i] == target:
                end = i
            else:
                break
        return [start, end]

s = Solution()
print(s.searchRange([1], 1))