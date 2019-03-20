# 81. 搜索旋转排序数组 II
# https://leetcode-cn.com/problems/search-in-rotated-sorted-array-ii/

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        if not nums:
            return False
        if len(nums) == 1:
            return nums[0] == target
        left = 0
        right = len(nums) - 1
        mid = len(nums) // 2
        while left <= right:
            if nums[mid] == target:
                return True
            if nums[mid] > nums[left]:
                if nums[mid] > target >= nums[left]:
                    right = mid - 1
                else:
                    left = mid + 1
            elif nums[mid] < nums[right]:
                if nums[right] >= target > nums[mid]:
                    left = mid + 1
                else:
                    right = mid - 1
            elif nums[mid] == nums[left] or nums[mid] == nums[right]:
                if nums[mid] == nums[left]:
                    left += 1
                if nums[mid] == nums[right]:
                    right -= 1
            mid = (right + left) // 2
        return False
s = Solution()
print(s.search([1,3,1,1,1], 3))