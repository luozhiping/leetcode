# 162. 寻找峰值
# https://leetcode-cn.com/problems/find-peak-element/

class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        start = 0
        end = len(nums) - 1
        while start < end:
            mid = (start + end) // 2
            if nums[mid] > nums[mid+1]:
                end = mid
            else:
                start = mid + 1
        return start


s = Solution()
print(s.findPeakElement([1,2,1,3,5,6,4]))