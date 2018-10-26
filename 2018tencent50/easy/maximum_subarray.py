# 最大子序列和
# https://leetcode-cn.com/problems/maximum-subarray/

class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        now = 0
        max = -2**31
        for i in nums:
            now += i
            if now > max:
                max = now
            if now < 0:
                now = 0
        return max



s = Solution()
# print(-2**31)
print(s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
