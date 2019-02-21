# 75. 颜色分类
# https://leetcode-cn.com/problems/sort-colors/

class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        self.quickSort(nums, 0, len(nums) - 1)
        print(nums)


    def quickSort(self, nums, left, right):
        if left < right:
            center = self.sortA(nums, left, right)
            self.quickSort(nums, left, center - 1)
            self.quickSort(nums, center + 1, right)

    def sortA(self, nums, left, right):
        base = nums[left]
        goRight = True
        while left < right:
            if goRight:
                if nums[right] < base:
                    nums[left] = nums[right]
                    goRight = False
                else:
                    right -= 1
            else:
                if nums[left] > base:
                    nums[right] = nums[left]
                    goRight = True
                else:
                    left += 1
        nums[left] = base
        return left


s = Solution()
print(s.sortColors([2,0,2,1,1,0]))