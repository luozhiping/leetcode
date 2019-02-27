# 994. 腐烂的橘子
# https://leetcode-cn.com/problems/rotting-oranges/

class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return -1
        rotting = []
        depth = {}

        fresh = []

        row = len(grid)
        col = len(grid[0])
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 2:
                    rotting.append((i, j))
                    depth[(i, j)] = 0
                elif grid[i][j] == 1:
                    fresh.append((i, j))
        direction = [(0, -1), (0, 1), (-1, 0), (1, 0)]

        result = 0
        while len(rotting) > 0:
            orange = rotting.pop(0)
            d = depth[orange]
            result = d
            for dir in direction:
                target = (orange[0] + dir[0], orange[1] + dir[1])
                if 0 <= target[0] < row and 0 <= target[1] < col and grid[target[0]][target[1]] == 1:
                    grid[target[0]][target[1]] = 2
                    rotting.append(target)
                    depth[target] = d+1
                    fresh.remove(target)
                    result = d + 1
        return result if len(fresh) == 0 else -1

s = Solution()
print(s.orangesRotting(
    [[0]]))