# 462. 最少移动次数使数组元素相等 II
# https://leetcode-cn.com/problems/minimum-moves-to-equal-array-elements-ii/

class Solution(object):
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return 0
        nums = sorted(nums)
        # if len(nums) & 0x1 == 1:
        result = 0
        middle = nums[len(nums)//2]
        for i in range(len(nums)):
            result += abs(nums[i] - middle)
        return result
        # else:
        #     result1 = 0
        #     result2 = 0
        #     middle1 = nums[len(nums)//2]
        #     middle2 = nums[len(nums)//2-1]
        #     for i in range(len(nums)):
        #         result1 += abs(nums[i] - middle1)
        #         result2 += abs(nums[i] - middle2)
        #     print(result1, result2)
        #     return min(result1, result2)




s = Solution()
print(s.minMoves2([1, 2,3, 9]))

import random
test = []
for i in range(random.randint(1, 10000)):
    test.append(random.randint(1, 100))

print(test)
print(s.minMoves2(test))