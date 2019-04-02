# 945. 使数组唯一的最小增量
# https://leetcode-cn.com/problems/minimum-increment-to-make-array-unique/

class Solution(object):
    def minIncrementForUnique(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if not A:
            return 0
        A = sorted(A)
        target = A[0] + 1
        result = 0
        for i in range(1, len(A)):
            result += max(target, A[i]) - A[i]
            target = max(target, A[i]) + 1
        return result



s = Solution()
print(s.minIncrementForUnique([3,2,1,2,1,7]))