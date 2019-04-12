# 260. 只出现一次的数字 III
# https://leetcode-cn.com/problems/single-number-iii/

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums or len(nums) < 2:
            return []
        xor = 0
        for n in nums:
            xor ^= n
        num1 = 0
        num2 = 0
        n = len(bin(xor)) - 3
        a, b = 0, 0
        for i in nums:
            if i >> n & 1:
                a ^= i
            else:
                b ^= i
        return [b, a]
s = Solution()
print(s.singleNumber([1,2,1,3,2,5]))