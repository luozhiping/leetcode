# 最接近的三数之和
# https://leetcode-cn.com/problems/3sum-closest/

class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        sum = nums[0] + nums[1] + nums[2]
        min_off = abs(sum - target)
        for i in range(len(nums)):
            start = i + 1
            end = len(nums) - 1
            while start < end:
                tmp = nums[i] + nums[start] + nums[end]
                off = tmp - target

                if abs(off) < min_off:
                    min_off = abs(off)
                    sum = tmp

                if off < 0:
                    start += 1
                elif off > 0:
                    end -= 1
                else:
                    return target
        return sum


s = Solution()
print(s.threeSumClosest([-1, 2, 1, -4, -8, -10, 22], 3))
