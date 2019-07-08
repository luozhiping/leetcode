# 64. 最小路径和
# https://leetcode-cn.com/problems/minimum-path-sum/
import sys

class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 0
        board = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        board[-1][-1] = grid[-1][-1]
        for i in range(len(grid) - 1, -1, -1):
            for j in range(len(grid[0]) - 1, -1, -1):
                if j == len(grid[0]) - 1 and i == len(grid) - 1:
                    continue
                right = sys.maxsize
                bottom = sys.maxsize
                if j < len(grid[0]) - 1:
                    right = board[i][j + 1]
                if i < len(grid) - 1:
                    bottom = board[i + 1][j]
                board[i][j] = grid[i][j] + min(right, bottom)
        return board[0][0]

s = Solution()
print(s.minPathSum([
  [1,3,1],
  [1,5,1],
  [4,2,0]
]))