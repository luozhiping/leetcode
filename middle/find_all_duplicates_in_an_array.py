# 442. 数组中重复的数据
# https://leetcode-cn.com/problems/find-all-duplicates-in-an-array/

class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []
        for num in nums:
            n = abs(num)
            if nums[n - 1] < 0:
                result.append(n)
            else:
                nums[n - 1] *= -1
        return result


s = Solution()
print(s.findDuplicates([4,3,2,7,8,2,3,1]))