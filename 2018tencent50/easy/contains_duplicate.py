# 存在重复元素
# https://leetcode-cn.com/problems/contains-duplicate/


class Solution:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums or len(nums) < 2:
            return False
        nums = sorted(nums)
        index1 = 0
        index2 = 1

        while index2 < len(nums):
            if nums[index1] == nums[index2]:
                return True
            index1 += 1
            index2 += 1
        return False

s = Solution()
print(s.containsDuplicate([1,1,1,3,3,4,3,2,4,2]))
