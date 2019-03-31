# 80. 删除排序数组中的重复项 II
# https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array-ii/

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums or len(nums) < 3:
            return len(nums)
        index = 2
        while index < len(nums):
            if nums[index] == nums[index - 1] == nums[index - 2]:
                nums.remove(nums[index])
            index += 1
        return len(nums)

s = Solution()
print(s.removeDuplicates([]))