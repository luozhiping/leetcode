# 子集
# https://leetcode-cn.com/problems/subsets/description/

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = [[]]
        max = (1 << len(nums))-1
        i = 1
        while i <= max:
            tmp = i
            tmp_one = []
            index = 0
            while tmp != 0:
                if tmp & 1 == 1:
                    tmp_one.append(nums[index])
                tmp = tmp >> 1
                index += 1
            result.append(tmp_one)
            i += 1
        return result


s = Solution()
print(s.subsets([1,2,3]))