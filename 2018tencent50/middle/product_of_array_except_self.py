# 除自身以外数组的乘积
# https://leetcode-cn.com/problems/product-of-array-except-self/

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        length = len(nums)
        array1 = [1] * length
        for i, num in enumerate(nums[:-1]):
            array1[i+1] = array1[i] * num

        right = 1
        for i in range(length-1, -1, -1):
            array1[i] *= right
            right *= nums[i]
        return array1

s = Solution()
print(s.productExceptSelf([1, 2, 3, 4]))