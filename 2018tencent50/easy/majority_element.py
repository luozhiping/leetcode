# 求众数
# https://leetcode-cn.com/problems/majority-element/


class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        return nums[int(len(nums)/2)]

s = Solution()
print(s.majorityElement([2,2,1,1,1,2,2]))