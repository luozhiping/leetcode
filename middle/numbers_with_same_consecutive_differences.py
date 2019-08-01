# 967. 连续差相同的数字
# https://leetcode-cn.com/problems/numbers-with-same-consecutive-differences/

class Solution:
    def numsSameConsecDiff(self, N, K):
        """
        :type N: int
        :type K: int
        :rtype: List[int]
        """
        result = []
        if N <= 1:
            result.append(0)

        def dfs(all, current, step):
            if step == N:
                result.append(all)
                return
            n = current - K
            if n >= 0:
                dfs(all*10+n, n, step+1)
            if K == 0:
                return
            n = current + K
            if n <= 9:
                dfs(all*10+n, n, step+1)

        for i in range(1, 10):
            dfs(i, i, 1)
        return result

s = Solution()
print(s.numsSameConsecDiff(3, 7))
assert sorted(s.numsSameConsecDiff(2, 1)) == [10,12,21,23,32,34,43,45,54,56,65,67,76,78,87,89,98]