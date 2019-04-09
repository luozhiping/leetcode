# 503. 下一个更大元素 II
# https://leetcode-cn.com/problems/next-greater-element-ii/

class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []
        result = [-1 for _ in range(len(nums))]
        stack = []
        max_pos = 0
        max_value = nums[0]
        for i in range(len(nums)):
            num = nums[i]
            if num > max_value:
                max_pos = i
                max_value = num
            while stack and nums[stack[-1]] < num:
                result[stack.pop(-1)] = num
            # if i < len(nums):
            stack.append(i)
        if len(stack) > 1:
            for i in range(stack[-1] + 1, max_pos + 1 + len(nums)):
                if len(stack) == 1:
                    break
                num = nums[i % len(nums)]
                while len(stack) > 1 and nums[stack[-1]] < num:
                    result[stack.pop(-1)] = num
        return result


s = Solution()
print(s.nextGreaterElements(
[-3,-2,-2,-3]))