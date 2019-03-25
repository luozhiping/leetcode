# 347. 前K个高频元素
# https://leetcode-cn.com/problems/top-k-frequent-elements/

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if not nums:
            return []
        nums_d = {}
        for num in nums:
            if num in nums_d:
                nums_d[num] += 1
            else:
                nums_d[num] = 1
        result = sorted(nums_d.items(), key=lambda x:x[1], reverse=True)
        result = [result[i][0] for i in range(k)]
        return result

s = Solution()
print(s.topKFrequent([1], 1))