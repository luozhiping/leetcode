# 287. 寻找重复数
# https://leetcode-cn.com/problems/find-the-duplicate-number/

class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        slow = 0
        fast = 0
        t = 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        while True:
            slow = nums[slow]
            t = nums[t]
            if slow == t:
                break
        return slow

s = Solution()
print(s.findDuplicate([1,3,4,2,2]))