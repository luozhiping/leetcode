# 491. 递增子序列
# https://leetcode-cn.com/problems/increasing-subsequences/

class Solution(object):
    def findSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # nums = sorted(nums)
        if not nums:
            return []
        result = []


        # for i in range(len(nums)):
        self.addSubSeq(result, nums, 0, len(nums), [])
        return result

    def addSubSeq(self, result, nums, start, end, prefix):
        if len(prefix) > 1:
            # if prefix not in result:
            result.append(prefix)
        used = set()
        for i in range(start, end):
            if (not prefix or nums[i] >= prefix[-1]) and nums[i] not in used:
                self.addSubSeq(result, nums, i + 1, end, prefix+[nums[i]])
            used.add(nums[i])

class Solution2(object):
    def findSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # 回溯/DFS
        r = []
        self.backtrack(r, [], nums, 0)

        return r

    def backtrack(self, r, subs, nums, start):
        if not nums:
            return
        if len(subs) > 1:
            r.append(subs[:])
        used = set()
        for i in range(start, len(nums)):
            if (not subs or subs[-1] <= nums[i]) and nums[i] not in used:
                self.backtrack(r, subs + [nums[i]], nums, i + 1)
            used.add(nums[i])

s = Solution()
print(s.findSubsequences([4, 6, 7, 7, 9]))
