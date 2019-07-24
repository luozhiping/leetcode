# 525. 连续数组
# https://leetcode-cn.com/problems/contiguous-array/

class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        dicts = {0:-1}
        last = 0
        for i in range(len(nums)):
            last += 1 if nums[i] == 1 else -1

            if last in dicts:
                result = max(result, i-dicts[last])
            else:
                dicts[last] = i
        # print(result)
        return result


s = Solution()
assert s.findMaxLength([0, 1]) == 2
assert s.findMaxLength([0, 1, 0]) == 2

import random
test = []
for i in range(random.randint(40000, 50000)):
    test.append(random.randint(0, 1))
# print(test)
print(s.findMaxLength(test))