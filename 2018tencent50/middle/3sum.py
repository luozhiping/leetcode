# 三数之和
# https://leetcode-cn.com/problems/3sum/description/

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) < 3:
            return []
        nums.sort()
        result = []
        p1 = 0
        p2 = 1
        p3 = 2
        num = nums[p1] + nums[p2] + nums[p3]
        move = 3
        while num <= 0:
            if num == 0:
                result.append([nums[p1], nums[p2], nums[p3]])
            else:
                if move == 3:
                    if p3 == len(nums) - 1:
                        pass


        return nums

s = Solution()
print(s.threeSum([-1, 0, 1, 2, -1, -4]))