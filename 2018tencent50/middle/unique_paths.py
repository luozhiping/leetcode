# 不同路径
# https://leetcode-cn.com/problems/unique-paths/

class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        paths = [[0 for _ in range(n+1)] for i in range(m+1)]
        for i in range(1, m+1):
            for j in range(1, n+1):
                if i == 1 and j == 1:
                    paths[i][j] = 1
                else:
                    paths[i][j] = paths[i-1][j] + paths[i][j-1]
        return paths[m][n]



s = Solution()
print(s.uniquePaths(23, 12))