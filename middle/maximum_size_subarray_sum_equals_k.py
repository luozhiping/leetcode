# 325. 和等于 k 的最长子数组长度
# https://leetcode-cn.com/problems/maximum-size-subarray-sum-equals-k/

class Solution(object):
    def maxSubArrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if not nums:
            return 0
        tmpSum = {0:0}
        preSum = 0
        result = 0
        for i, num in enumerate(nums):
            preSum += num
            if preSum not in tmpSum:
                tmpSum[preSum] = i + 1
            if preSum - k in tmpSum:
                result = max(result, i + 1 - tmpSum[preSum - k])
        return result
s = Solution()
assert s.maxSubArrayLen( [1, -1, 5, -2, 3], 3) == 4
assert s.maxSubArrayLen([-2, -1, 2, 1], 1) == 2