# 31. 下一个排列
# https://leetcode-cn.com/problems/next-permutation/

class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return []
        index = -1
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                index = i
                break
        if index != -1:
            index2 = nums[index]
            for i in range(index + 1, len(nums)):
                if nums[index] < nums[i]:
                    index2 = i
                else:
                    break
            nums[index], nums[index2] = nums[index2], nums[index]
            tmp = sorted(nums[index+1:])
            nums[index+1:] = tmp
            # nums.extend(tmp)
        else:
            nums.sort()
        print(nums)


s = Solution()
# print(s.nextPermutation([1,5,8,4,7,6,5,3,1]))
print(s.nextPermutation([3, 2, 1]))
# print(s.nextPermutation([1,1,5]))