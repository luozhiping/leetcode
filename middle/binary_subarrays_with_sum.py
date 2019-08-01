# 930. 和相同的二元子数组
# https://leetcode-cn.com/problems/binary-subarrays-with-sum/

class Solution(object):
    def numSubarraysWithSum(self, A, S):
        """
        :type A: List[int]
        :type S: int
        :rtype: int
        """
        if not A:
            return 0
        prefixSum = {0:[0]}
        currentSum = 0
        result = 0
        for i, num in enumerate(A):
            currentSum += num
            if currentSum in prefixSum:
                prefixSum[currentSum].append(i+1)
            else:
                prefixSum[currentSum] = [i+1]
            if (currentSum - S) in prefixSum:
                result += len(prefixSum[currentSum - S]) - (1 if (currentSum - S) == currentSum else 0)
        # print(result)
        return result


s = Solution()
assert s.numSubarraysWithSum([1,0,1,0,1], 2) == 4
assert s.numSubarraysWithSum([0,0,0,0,0], 0) == 15
assert s.numSubarraysWithSum([0,0,0,0,0,0,1,0,0,0], 0) == 27
import random
test = []
for i in range(random.randint(2000, 30000)):
    test.append(random.randint(0, 1))
print(test)