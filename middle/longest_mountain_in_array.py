# 845. 数组中的最长山脉
# https://leetcode-cn.com/problems/longest-mountain-in-array/

class Solution(object):
    def longestMountain(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if not A:
            return 0
        bpUp = [1 for _ in range(len(A))]
        bpDown = [1 for _ in range(len(A))]
        result = 0
        for i in range(1, len(A)):
            upIndex = i
            downIndex = len(A) - 1 - i
            if A[upIndex] > A[upIndex - 1]:
                bpUp[upIndex] = bpUp[upIndex - 1] + 1
            if A[downIndex] > A[downIndex + 1]:
                bpDown[downIndex] = bpDown[downIndex + 1] + 1
        for i in range(1, len(A) - 1):
            if bpUp[i] > 1 and bpDown[i] > 1:
                result = max(result, bpUp[i]+bpDown[i] - 1)
        # print(bpUp)
        # print(bpDown)
        print(A)
        return result



s = Solution()
# print(s.longestMountain([2,1,4,7,3,2,5]))
print(s.longestMountain([0,1,0]))
import random
test = []
for i in range(random.randint(0, 10000)):
    test.append(random.randint(0, 10000))
print(s.longestMountain(test))