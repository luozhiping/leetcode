# 673. 最长递增子序列的个数
# https://leetcode-cn.com/problems/number-of-longest-increasing-subsequence/

class Solution(object):
    def findNumberOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [1 for _ in range(len(nums))]
        cnt = [1 for _ in range(len(nums))]
        maxLen = 1
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[j] >= nums[i]:
                    continue
                if dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
                    cnt[i] = cnt[j]
                elif dp[j] + 1 == dp[i]:
                    cnt[i] += cnt[j]
            maxLen = max(maxLen, dp[i])
        result = 0
        for i, d in enumerate(dp):
            if d == maxLen:
                result += cnt[i]
        return result

s = Solution()
print(s.findNumberOfLIS([2,2,2,2,2]))