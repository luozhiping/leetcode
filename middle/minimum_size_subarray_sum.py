# 209. 长度最小的子数组
# https://leetcode-cn.com/problems/minimum-size-subarray-sum/


class Solution2(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        result = len(nums) + 1
        for i in range(len(nums)):
            tmp = 0
            for j in range(i, len(nums)):
                tmp += nums[j]
                if tmp >= s:
                    result = min(result, j + 1 - i)
                    if result == 1:
                        return result
                    break
        return result if result != len(nums) + 1 else 0

class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        result = len(nums) + 1
        left = 0
        right = 0
        tmp = nums[left]
        while True:
            if tmp >= s:
                if left == right:
                    return 1
                result = min(result, right + 1 - left)
                tmp -= nums[left]
                left += 1
                if left == len(nums):
                    break
            else:
                right += 1
                if right == len(nums):
                    break
                tmp += nums[right]

        return result if result != len(nums) + 1 else 0


s = Solution()
print(s.minSubArrayLen(7, [2,3,1,2,4,3]))