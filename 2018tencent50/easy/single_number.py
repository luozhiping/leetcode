# 只出现一次的数字
# https://leetcode-cn.com/problems/single-number/

class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num = nums[0]
        for i in range(1, len(nums)):
            num ^= nums[i]
        return num


s = Solution()
print(s.singleNumber([[4,1,2,1,2]]))