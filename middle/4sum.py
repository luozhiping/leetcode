# 18. 四数之和
# https://leetcode-cn.com/problems/4sum/
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if not nums:
            return []
        nums = sorted(nums)
        print(nums)
        length = len(nums)
        result = []
        for i in range(length - 3):
            # if nums[i] > target:
            #     break
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, length - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                two = nums[i] + nums[j]
                need = target - two
                start = j+1
                end = len(nums) - 1
                while start < end:
                    start1 = nums[start]
                    end1 = nums[end]
                    if nums[start] + nums[end] == need:
                        result.append([nums[i], nums[j], nums[start], nums[end]])
                        while start < end and nums[start] == nums[start + 1]:
                            start += 1
                        while start < end and nums[end] == nums[end - 1]:
                            end -= 1
                        start += 1
                        end -= 1
                        continue
                    elif nums[start] + nums[end] < need:
                        start += 1
                    else:
                        end -= 1

        return result
s = Solution()
# print(s.fourSum([1, 0, -1, 0, -2, 2], 0))
# print(s.fourSum([0,1,5,0,1,5,5,-4]
# ,11))
# print(s.fourSum([0,0,0,0], 0))
# print(s.fourSum([-3,-2,-1,0,0,1,2,3],
# 0))
print(s.fourSum([0,4,-5,2,-2,4,2,-1,4]
,12))