# 数组中的第K个最大元素
# https://leetcode-cn.com/problems/kth-largest-element-in-an-array/description/


class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums = sorted(nums, reverse=True)
        return nums[k - 1]

s = Solution()
print(s.findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))
