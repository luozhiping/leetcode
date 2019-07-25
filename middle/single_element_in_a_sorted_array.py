# 540. 有序数组中的单一元素
# https://leetcode-cn.com/problems/single-element-in-a-sorted-array/

class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start = 0
        end = len(nums) - 1
        while start < end:
            middle = (start + end) // 2
            if middle > 0 and middle < len(nums) and nums[middle] != nums[middle-1] and nums[middle] != nums[middle+1]:
                return nums[middle]
            if middle & 0x01 == 0:
                # 偶数
                if nums[middle] == nums[middle+1]:
                    start = middle + 1
                else:
                    end = middle - 1
            else:
                if nums[middle] == nums[middle+1]:
                    end = middle - 1
                else:
                    start = middle + 1
        return nums[start]


s = Solution()
assert s.singleNonDuplicate([2,2,3,3,4,4,8]) == 8
assert s.singleNonDuplicate([3,3,7,7,10,11,11]) == 10
assert s.singleNonDuplicate([1,1,2,3,3]) == 2