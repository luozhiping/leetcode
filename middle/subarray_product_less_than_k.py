# 713. 乘积小于K的子数组
# https://leetcode-cn.com/problems/subarray-product-less-than-k/
import time
class Solution2(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # print(nums, k)
        if not nums:
            return 0
        # begin = time.time()
        bp = [1 for _ in range(len(nums))]
        # print(time.time() - begin)
        result = 0
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if i == j:
                    bp[j] = nums[i]
                else:
                    bp[j] = bp[j-1] * nums[j]
                if bp[j] < k:
                    result += 1
                    # print(nums[i: j+1])
                else:
                    break
        return result

class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        if not nums:
            return 0
        startIndex = 0
        endIndex = 0
        currentResult = 1
        result = 0
        print(nums, k)
        while startIndex < len(nums) and endIndex < len(nums):
            # print(nums[startIndex], nums[endIndex])
            currentResult = currentResult * nums[endIndex]
            if currentResult < k:
                result += 1
                result += endIndex - startIndex
                endIndex += 1
            else:
                # currentResult = currentResult * nums[endIndex]
                for i in range(startIndex, endIndex):
                    currentResult /= nums[i]
                    if currentResult < k:
                        result += 1
                        result += endIndex - (i + 1)
                        startIndex = i + 1
                        endIndex += 1
                        break
                if currentResult > k:
                    startIndex = endIndex + 1
                    endIndex = endIndex + 1
                    currentResult = 1

        # print(startIndex, endIndex)
        return result
s = Solution()
# print(s.numSubarrayProductLessThanK([10,5,2,6], 100))
# assert s.numSubarrayProductLessThanK([6, 9, 7, 10, 19, 16, 18, 18, 7, 17, 12, 13, 12, 3, 7, 11, 16, 10, 19, 13, 6, 20, 11, 6, 20, 6, 8, 15, 13, 13, 9, 15, 17, 18, 20, 16, 3, 13, 12, 2, 9, 18, 5, 8, 17, 19, 10, 9, 10, 8, 19, 8, 3, 2, 20, 9, 3, 5, 6, 13, 16, 6, 12, 3, 19, 20, 16, 13, 11, 14, 4, 12, 5, 14, 15, 16, 20, 13, 3, 7, 7, 5, 7, 8, 16, 18, 20, 20, 2, 1, 4, 19, 20, 19, 12, 13, 8, 11, 12, 11]
# ,50) == 127
import random
test = []
# for i in range(100):
#     test.append(random.randint(1, 20))
# print(s.numSubarrayProductLessThanK(test, random.randint(0, 500)))
for i in range(45000):
    test.append(random.randint(1, 999))
print('begin')
print(s.numSubarrayProductLessThanK(test, random.randint(0, 10**6-1)))