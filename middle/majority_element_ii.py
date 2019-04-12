# 229. 求众数 II
# https://leetcode-cn.com/problems/majority-element-ii/

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []
        num1 = 0
        num2 = 0
        count1 = 0
        count2 = 0

        for n in nums:
            if count1 != 0 and n == num1:
                count1 += 1
            elif count2 != 0 and n == num2:
                count2 += 1
            elif count1 == 0:
                num1 = n
                count1 = 1
            elif count2 == 0:
                num2 = n
                count2 = 1
            else:
                count1 = max(count1 - 1, 0)
                count2 = max(count2 - 1, 0)
        count1 = 0
        count2 = 0
        for n in nums:
            if n == num1:
                count1 += 1
            elif n == num2:
                count2 += 1
        result = []
        if count1 > len(nums) // 3:
            result.append(num1)
        if count2 > len(nums) // 3:
            result.append(num2)
        return result

s = Solution()
print(s.majorityElement([1,1,1,3,3,2,2,2]))