# 搜索旋转排列数组
# https://leetcode-cn.com/problems/search-in-rotated-sorted-array/

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 0:
            return -1
        return self.search_offset(nums, target, 0)

    def search_offset(self, nums, target, offset):
        left = 0
        right = len(nums) - 1
        middle = len(nums) // 2

        if target == nums[middle]:
            return middle + offset
        elif target == nums[left]:
            return left + offset
        elif target == nums[right]:
            return right + offset
        else:
            if len(nums) <= 3:
                return -1

        if nums[middle] > nums[left]:
            # 左边都是升序
            if nums[middle] > target > nums[left]:
                result = self.search_offset(nums[left:middle], target, 0)
                return result if result == -1 else result + offset
            else:
                result = self.search_offset(nums[middle:right], target, middle)
                return result if result == -1 else result + offset
        else:
            # 左边有部分已经不是升序了
            if nums[right] > target > nums[middle]:
                result = self.search_offset(nums[middle:right], target, middle)
                return result if result == -1 else result + offset
            else:
                result = self.search_offset(nums[left:middle], target, 0)
                return result if result == -1 else result + offset


s = Solution()
print(s.search(
    [9, 1, 2, 3, 4, 5, 6, 7, 8], 5))
