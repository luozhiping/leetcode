# 300. 最长上升子序列
# https://leetcode-cn.com/problems/longest-increasing-subsequence/

class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        dp = [0 for _ in range(len(nums))]
        dp[0] = 1
        result = 0
        for i in range(len(nums)):
            tmpMax = 0
            for j in range(i):
                if nums[j] < nums[i]:
                    tmpMax = max(dp[j], tmpMax)
            dp[i] = tmpMax + 1
            result = max(result, dp[i])
        return result

s = Solution()
print(s.lengthOfLIS([10,9,2,5,3,7,101,18]))